#include <Python.h>
#include <stdlib.h>
#include <string.h>

#if defined(_WIN32)
#include <windows.h>
#define PYOPENMP_EXPORT __declspec(dllexport)
#define PATH_SEP '\\'
#else
#include <dlfcn.h>
#include <limits.h>
#define PYOPENMP_EXPORT __attribute__((visibility("default")))
#define PATH_SEP '/'
#endif

#define PYOPENMP_STR_(x) #x
#define PYOPENMP_STR(x) PYOPENMP_STR_(x)
#define PYOPENMP_PYVER \
    PYOPENMP_STR(PY_MAJOR_VERSION) "." PYOPENMP_STR(PY_MINOR_VERSION)

static int g_started = 0;
static PyThreadState* g_saved = NULL;

static void promote_python_symbols(void)
{
#if !defined(_WIN32)
    const char* names[] = {
        "libpython" PYOPENMP_PYVER ".so.1.0",
        "libpython" PYOPENMP_PYVER ".so",
        NULL,
    };
    for (int i = 0; names[i]; i++)
    {
        if (dlopen(names[i], RTLD_NOW | RTLD_GLOBAL))
        {
            return;
        }
    }
    fprintf(stderr, "[pyopenmp] warning: could not promote libpython symbols\n");
#endif
}

static void self_path(char* out, size_t n)
{
    out[0] = 0;
#if defined(_WIN32)
    HMODULE mod = NULL;
    if (GetModuleHandleExA(
            GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS
                | GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT,
            (LPCSTR)&self_path, &mod))
    {
        GetModuleFileNameA(mod, out, (DWORD)n);
    }
#else
    Dl_info info;
    if (dladdr((void*)&self_path, &info) && info.dli_fname)
    {
        char resolved[PATH_MAX];
        if (realpath(info.dli_fname, resolved))
        {
            strncpy(out, resolved, n - 1);
        }
        else
        {
            strncpy(out, info.dli_fname, n - 1);
        }
        out[n - 1] = 0;
    }
#endif
}

static void server_root(char* out, size_t n)
{
    self_path(out, n);
    if (!out[0])
    {
        return;
    }
    char* p = strrchr(out, PATH_SEP);
    if (!p)
    {
        out[0] = 0;
        return;
    }
    *p = 0;
    p = strrchr(out, PATH_SEP);
    if (!p)
    {
        out[0] = 0;
        return;
    }
    *p = 0;
}

static void export_root(const char* root)
{
    if (!root[0])
    {
        return;
    }
#if defined(_WIN32)
    _putenv_s("PYOPENMP_ROOT", root);
#else
    setenv("PYOPENMP_ROOT", root, 1);
#endif
}

static void insert_path(const char* dir)
{
    if (!dir[0])
    {
        return;
    }
    PyObject* sys_path = PySys_GetObject("path");
    if (sys_path)
    {
        PyObject* entry = PyUnicode_FromString(dir);
        if (entry)
        {
            PyList_Insert(sys_path, 0, entry);
            Py_DECREF(entry);
        }
    }
}

static void component_dir(char* out, size_t n)
{
    self_path(out, n);
    if (!out[0])
    {
        return;
    }
    char* p = strrchr(out, PATH_SEP);
    if (p)
    {
        *p = 0;
    }
    else
    {
        out[0] = 0;
    }
}

static void setup_paths(const char* root)
{
    char cdir[4096];
    component_dir(cdir, sizeof(cdir));
    insert_path(cdir);
    insert_path(root);
    PyRun_SimpleString(
        "import os, sys\n_cwd = os.getcwd()\n"
        "(_cwd in sys.path) or sys.path.insert(0, _cwd)\n");
}

static void* run_bootstrap(void)
{
    void* component = NULL;

    PyObject* module = PyImport_ImportModule("pyopenmp._bootstrap");
    if (!module)
    {
        fprintf(stderr, "[pyopenmp] failed to import pyopenmp._bootstrap\n");
        PyErr_Print();
        return NULL;
    }

    PyObject* start = PyObject_GetAttrString(module, "start");
    if (start && PyCallable_Check(start))
    {
        PyObject* result = PyObject_CallObject(start, NULL);
        if (!result)
        {
            PyErr_Print();
        }
        else
        {
            if (result != Py_None)
            {
                component = PyLong_AsVoidPtr(result);
            }
            Py_DECREF(result);
        }
    }
    else
    {
        PyErr_Print();
    }

    Py_XDECREF(start);
    Py_DECREF(module);
    return component;
}

PYOPENMP_EXPORT void* ComponentEntryPoint(void)
{
    if (g_started)
    {
        return NULL;
    }
    g_started = 1;

    char root[4096];
    server_root(root, sizeof(root));
    export_root(root);

    promote_python_symbols();
    Py_Initialize();
    setup_paths(root);
    void* component = run_bootstrap();
    g_saved = PyEval_SaveThread();
    return component;
}

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

static int g_started = 0;
static PyThreadState* g_saved = NULL;

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

static void print_diagnostics(void)
{
    PyRun_SimpleString(
        "import os, sys\n"
        "_r = os.environ.get('PYOPENMP_ROOT') or os.getcwd()\n"
        "print('[pyopenmp] cwd =', os.getcwd(), file=sys.stderr)\n"
        "print('[pyopenmp] PYOPENMP_ROOT =', os.environ.get('PYOPENMP_ROOT'), file=sys.stderr)\n"
        "print('[pyopenmp] sys.path[:6] =', sys.path[:6], file=sys.stderr)\n"
        "print('[pyopenmp] has', os.path.join(_r, 'pyopenmp', '__init__.py'), '=', os.path.exists(os.path.join(_r, 'pyopenmp', '__init__.py')), file=sys.stderr)\n"
        "print('[pyopenmp] has', os.path.join(_r, 'pyopenmp', '_bootstrap.py'), '=', os.path.exists(os.path.join(_r, 'pyopenmp', '_bootstrap.py')), file=sys.stderr)\n");
}

static void run_bootstrap(void)
{
    PyObject* module = PyImport_ImportModule("pyopenmp._bootstrap");
    if (!module)
    {
        fprintf(stderr, "[pyopenmp] failed to import pyopenmp._bootstrap\n");
        print_diagnostics();
        PyErr_Print();
        return;
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
            Py_DECREF(result);
        }
    }
    else
    {
        PyErr_Print();
    }

    Py_XDECREF(start);
    Py_DECREF(module);
}

PYOPENMP_EXPORT void ComponentEntryPoint(void)
{
    if (g_started)
    {
        return;
    }
    g_started = 1;

    fprintf(stderr, "[pyopenmp] component starting\n");

    char root[4096];
    server_root(root, sizeof(root));
    fprintf(stderr, "[pyopenmp] detected server root = %s\n", root[0] ? root : "(none)");
    export_root(root);

    Py_Initialize();
    setup_paths(root);
    run_bootstrap();
    g_saved = PyEval_SaveThread();
}

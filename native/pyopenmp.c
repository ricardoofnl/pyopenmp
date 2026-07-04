#include <Python.h>

#if defined(_WIN32)
#define PYOPENMP_EXPORT __declspec(dllexport)
#else
#define PYOPENMP_EXPORT __attribute__((visibility("default")))
#endif

static int g_started = 0;
static PyThreadState* g_saved = NULL;

static void run_bootstrap(void)
{
    PyRun_SimpleString("import sys, os\nsys.path.insert(0, os.getcwd())\n");

    PyObject* module = PyImport_ImportModule("pyopenmp._bootstrap");
    if (!module)
    {
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

    Py_Initialize();
    run_bootstrap();
    g_saved = PyEval_SaveThread();
}

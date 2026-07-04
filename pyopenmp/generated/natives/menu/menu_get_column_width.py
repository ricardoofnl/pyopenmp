import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_GetColumnWidth", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def menu_get_column_width(menu):
    column1_width = ctypes.c_float()
    column2_width = ctypes.c_float()
    __ret = _fn(menu, ctypes.byref(column1_width), ctypes.byref(column2_width))
    if __ret:
        return (column1_width.value, column2_width.value)
    return None

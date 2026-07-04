import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_GetColumnHeader", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView)])


def menu_get_column_header(menu, column):
    header = _capi.CAPIStringView()
    __ret = _fn(menu, column, ctypes.byref(header))
    if __ret:
        return _capi.read_view(header)
    return None

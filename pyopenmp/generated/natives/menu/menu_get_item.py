import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_GetItem", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView)])


def menu_get_item(menu, column, row):
    item = _capi.CAPIStringView()
    __ret = _fn(menu, column, row, ctypes.byref(item))
    if __ret:
        return _capi.read_view(item)
    return None

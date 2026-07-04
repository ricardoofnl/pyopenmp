import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Menu_Create", ctypes.c_void_p, [ctypes.c_char_p, ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.POINTER(ctypes.c_int)])


def menu_create(title, columns, x, y, column1_width, column2_width):
    id = ctypes.c_int()
    __ret = _fn(_capi.enc(title), columns, x, y, column1_width, column2_width, ctypes.byref(id))
    return (__ret, id.value)

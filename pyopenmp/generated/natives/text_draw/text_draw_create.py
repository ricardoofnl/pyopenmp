import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_Create", ctypes.c_void_p, [ctypes.c_float, ctypes.c_float, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)])


def text_draw_create(x, y, text):
    id = ctypes.c_int()
    __ret = _fn(x, y, _capi.enc(text), ctypes.byref(id))
    return (__ret, id.value)

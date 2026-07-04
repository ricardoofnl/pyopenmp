import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_Create", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_char_p, ctypes.POINTER(ctypes.c_int)])


def player_text_draw_create(player, x, y, text):
    id = ctypes.c_int()
    __ret = _fn(player, x, y, _capi.enc(text), ctypes.byref(id))
    return (__ret, id.value)

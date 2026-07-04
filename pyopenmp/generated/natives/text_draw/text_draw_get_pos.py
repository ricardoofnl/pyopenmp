import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def text_draw_get_pos(textdraw):
    x = ctypes.c_float()
    y = ctypes.c_float()
    __ret = _fn(textdraw, ctypes.byref(x), ctypes.byref(y))
    if __ret:
        return (x.value, y.value)
    return None

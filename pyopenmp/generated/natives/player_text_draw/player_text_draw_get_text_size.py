import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_GetTextSize", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_text_draw_get_text_size(player, textdraw):
    x = ctypes.c_float()
    y = ctypes.c_float()
    __ret = _fn(player, textdraw, ctypes.byref(x), ctypes.byref(y))
    if __ret:
        return (x.value, y.value)
    return None

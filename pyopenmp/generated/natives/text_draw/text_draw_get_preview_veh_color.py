import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetPreviewVehColor", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def text_draw_get_preview_veh_color(textdraw):
    color1 = ctypes.c_int()
    color2 = ctypes.c_int()
    __ret = _fn(textdraw, ctypes.byref(color1), ctypes.byref(color2))
    if __ret:
        return (color1.value, color2.value)
    return None

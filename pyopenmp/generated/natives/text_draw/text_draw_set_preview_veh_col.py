import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetPreviewVehCol", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def text_draw_set_preview_veh_col(textdraw, color1, color2):
    return _fn(textdraw, color1, color2)

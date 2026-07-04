import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetPreviewVehCol", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def player_text_draw_set_preview_veh_col(player, textdraw, color1, color2):
    return _fn(player, textdraw, color1, color2)

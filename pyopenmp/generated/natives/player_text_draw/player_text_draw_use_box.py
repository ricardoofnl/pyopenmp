import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_UseBox", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool])


def player_text_draw_use_box(player, textdraw, use):
    return _fn(player, textdraw, use)

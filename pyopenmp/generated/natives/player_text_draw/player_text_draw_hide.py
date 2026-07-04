import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_Hide", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_draw_hide(player, textdraw):
    return _fn(player, textdraw)

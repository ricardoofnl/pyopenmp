import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_IsBox", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_draw_is_box(player, textdraw):
    return _fn(player, textdraw)

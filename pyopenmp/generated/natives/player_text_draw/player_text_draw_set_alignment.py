import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetAlignment", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_text_draw_set_alignment(player, textdraw, alignment):
    return _fn(player, textdraw, alignment)

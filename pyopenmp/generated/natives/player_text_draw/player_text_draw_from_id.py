import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_FromID", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_int])


def player_text_draw_from_id(player, textdrawid):
    return _fn(player, textdrawid)

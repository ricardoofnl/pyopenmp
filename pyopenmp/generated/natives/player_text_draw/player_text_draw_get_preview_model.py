import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_GetPreviewModel", ctypes.c_int, [ctypes.c_void_p, ctypes.c_void_p])


def player_text_draw_get_preview_model(player, textdraw):
    return _fn(player, textdraw)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetPreviewModel", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_text_draw_set_preview_model(player, textdraw, model):
    return _fn(player, textdraw, model)

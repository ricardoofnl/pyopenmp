import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_SetPreviewRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def player_text_draw_set_preview_rot(player, textdraw, rx, ry, rz, zoom):
    return _fn(player, textdraw, rx, ry, rz, zoom)

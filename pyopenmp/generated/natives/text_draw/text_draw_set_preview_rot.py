import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetPreviewRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def text_draw_set_preview_rot(textdraw, rotation_x, rotation_y, rotation_z, zoom):
    return _fn(textdraw, rotation_x, rotation_y, rotation_z, zoom)

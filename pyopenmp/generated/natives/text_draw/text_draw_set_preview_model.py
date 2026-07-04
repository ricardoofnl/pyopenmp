import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_SetPreviewModel", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def text_draw_set_preview_model(textdraw, model):
    return _fn(textdraw, model)

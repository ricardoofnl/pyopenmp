import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetLetterSize", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def text_draw_get_letter_size(textdraw):
    size_x = ctypes.c_float()
    size_y = ctypes.c_float()
    __ret = _fn(textdraw, ctypes.byref(size_x), ctypes.byref(size_y))
    if __ret:
        return (size_x.value, size_y.value)
    return None

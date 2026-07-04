import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetString", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def text_draw_get_string(textdraw):
    text = _capi.CAPIStringView()
    __ret = _fn(textdraw, ctypes.byref(text))
    if __ret:
        return _capi.read_view(text)
    return None

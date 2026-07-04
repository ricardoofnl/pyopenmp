import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextDraw_GetPreviewRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def text_draw_get_preview_rot(textdraw):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    zoom = ctypes.c_float()
    __ret = _fn(textdraw, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z), ctypes.byref(zoom))
    if __ret:
        return (x.value, y.value, z.value, zoom.value)
    return None

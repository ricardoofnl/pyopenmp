import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def text_label_get_pos(textlabel):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    __ret = _fn(textlabel, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    if __ret:
        return (x.value, y.value, z.value)
    return None

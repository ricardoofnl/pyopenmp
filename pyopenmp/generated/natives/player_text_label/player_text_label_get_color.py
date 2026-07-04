import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_GetColor", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_uint32)])


def player_text_label_get_color(player, textlabel):
    color = ctypes.c_uint32()
    __ret = _fn(player, textlabel, ctypes.byref(color))
    if __ret:
        return color.value
    return None

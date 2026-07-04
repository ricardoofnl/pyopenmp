import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_IsValid", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_bool)])


def player_text_label_is_valid(player, textlabel):
    valid = ctypes.c_bool()
    __ret = _fn(player, textlabel, ctypes.byref(valid))
    if __ret:
        return valid.value
    return None

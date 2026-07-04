import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetAttachedData", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def text_label_get_attached_data(textlabel):
    attached_player = ctypes.c_int()
    attached_vehicle = ctypes.c_int()
    __ret = _fn(textlabel, ctypes.byref(attached_player), ctypes.byref(attached_vehicle))
    if __ret:
        return (attached_player.value, attached_vehicle.value)
    return None

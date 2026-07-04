import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_AttachToPlayer", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def text_label_attach_to_player(textlabel, player, offset_x, offset_y, offset_z):
    return _fn(textlabel, player, offset_x, offset_y, offset_z)

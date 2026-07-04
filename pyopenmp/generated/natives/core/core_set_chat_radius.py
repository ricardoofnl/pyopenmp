import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetChatRadius", ctypes.c_bool, [ctypes.c_float])


def core_set_chat_radius(global_chat_radius):
    return _fn(global_chat_radius)

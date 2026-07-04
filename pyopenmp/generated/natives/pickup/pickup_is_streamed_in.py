import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_IsStreamedIn", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def pickup_is_streamed_in(player, pickup):
    return _fn(player, pickup)

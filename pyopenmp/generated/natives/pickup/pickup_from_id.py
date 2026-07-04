import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Pickup_FromID", ctypes.c_void_p, [ctypes.c_int])


def pickup_from_id(pickupid):
    return _fn(pickupid)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_ChangePaintjob", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def vehicle_change_paintjob(vehicle, paintjobid):
    return _fn(vehicle, paintjobid)

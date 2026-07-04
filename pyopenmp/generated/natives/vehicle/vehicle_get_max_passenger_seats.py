import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetMaxPassengerSeats", ctypes.c_int, [ctypes.c_int])


def vehicle_get_max_passenger_seats(modelid):
    return _fn(modelid)

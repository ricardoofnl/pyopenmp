import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_SetNumberPlate", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p])


def vehicle_set_number_plate(vehicle, number_plate):
    return _fn(vehicle, _capi.enc(number_plate))

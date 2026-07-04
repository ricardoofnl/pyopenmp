import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_GetNumberPlate", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def vehicle_get_number_plate(vehicle):
    number_plate = _capi.CAPIStringView()
    __ret = _fn(vehicle, ctypes.byref(number_plate))
    if __ret:
        return _capi.read_view(number_plate)
    return None

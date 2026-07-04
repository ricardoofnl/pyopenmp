import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_ColorIndexToColor", ctypes.c_int, [ctypes.c_int, ctypes.c_int])


def vehicle_color_index_to_color(color_index, alpha):
    return _fn(color_index, alpha)

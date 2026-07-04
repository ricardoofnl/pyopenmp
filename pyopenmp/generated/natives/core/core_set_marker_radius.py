import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetMarkerRadius", ctypes.c_bool, [ctypes.c_float])


def core_set_marker_radius(player_marker_radius):
    return _fn(player_marker_radius)

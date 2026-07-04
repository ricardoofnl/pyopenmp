import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_ShowPlayerMarkers", ctypes.c_bool, [ctypes.c_int])


def core_show_player_markers(mode):
    return _fn(mode)

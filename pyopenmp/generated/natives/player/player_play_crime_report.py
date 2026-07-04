import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_PlayCrimeReport", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def player_play_crime_report(player, suspect, crime):
    return _fn(player, suspect, crime)

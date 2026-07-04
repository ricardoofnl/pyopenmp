import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Recording_Start", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_char_p])


def recording_start(player, type, file):
    return _fn(player, type, _capi.enc(file))

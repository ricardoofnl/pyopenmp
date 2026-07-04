import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SendRconCommand", ctypes.c_bool, [ctypes.c_char_p])


def core_send_rcon_command(command):
    return _fn(_capi.enc(command))

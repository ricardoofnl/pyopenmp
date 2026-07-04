import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetVersion", ctypes.c_int, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def player_get_version(player):
    version = _capi.CAPIStringView()
    __ret = _fn(player, ctypes.byref(version))
    return _capi.read_view(version)

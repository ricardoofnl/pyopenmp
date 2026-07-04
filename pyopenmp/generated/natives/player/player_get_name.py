import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetName", ctypes.c_int, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def player_get_name(player):
    name = _capi.CAPIStringView()
    __ret = _fn(player, ctypes.byref(name))
    return _capi.read_view(name)

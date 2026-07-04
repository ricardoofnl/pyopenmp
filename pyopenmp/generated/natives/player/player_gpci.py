import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GPCI", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def player_gpci(player):
    gpci = _capi.CAPIStringView()
    __ret = _fn(player, ctypes.byref(gpci))
    if __ret:
        return _capi.read_view(gpci)
    return None

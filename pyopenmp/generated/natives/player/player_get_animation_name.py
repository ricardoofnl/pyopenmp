import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetAnimationName", ctypes.c_bool, [ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView)])


def player_get_animation_name(index):
    lib = _capi.CAPIStringView()
    name = _capi.CAPIStringView()
    __ret = _fn(index, ctypes.byref(lib), ctypes.byref(name))
    if __ret:
        return (_capi.read_view(lib), _capi.read_view(name))
    return None

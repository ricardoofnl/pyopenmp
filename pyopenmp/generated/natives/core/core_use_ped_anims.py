import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_UsePedAnims", ctypes.c_bool, [])


def core_use_ped_anims():
    return _fn()

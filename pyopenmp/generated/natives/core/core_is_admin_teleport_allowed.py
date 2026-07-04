import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_IsAdminTeleportAllowed", ctypes.c_bool, [])


def core_is_admin_teleport_allowed():
    return _fn()

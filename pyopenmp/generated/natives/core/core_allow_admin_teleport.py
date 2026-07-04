import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_AllowAdminTeleport", ctypes.c_bool, [ctypes.c_bool])


def core_allow_admin_teleport(allow):
    return _fn(allow)

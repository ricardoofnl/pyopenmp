import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_DisableEntryExitMarkers", ctypes.c_bool, [])


def core_disable_entry_exit_markers():
    return _fn()

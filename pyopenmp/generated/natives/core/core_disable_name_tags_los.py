import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_DisableNameTagsLOS", ctypes.c_bool, [])


def core_disable_name_tags_los():
    return _fn()

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_ShowNameTags", ctypes.c_bool, [ctypes.c_bool])


def core_show_name_tags(show):
    return _fn(show)

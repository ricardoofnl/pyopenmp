import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_SetNameTagsDrawDistance", ctypes.c_bool, [ctypes.c_float])


def core_set_name_tags_draw_distance(distance):
    return _fn(distance)

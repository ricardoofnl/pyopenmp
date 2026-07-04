import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_GetDrawDistance", ctypes.c_float, [ctypes.c_void_p])


def object_get_draw_distance(object):
    return _fn(object)

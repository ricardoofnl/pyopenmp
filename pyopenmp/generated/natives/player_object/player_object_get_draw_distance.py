import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetDrawDistance", ctypes.c_float, [ctypes.c_void_p, ctypes.c_void_p])


def player_object_get_draw_distance(player, object):
    return _fn(player, object)

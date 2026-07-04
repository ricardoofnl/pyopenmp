import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetMovingTargetPos", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_object_get_moving_target_pos(player, object):
    target_x = ctypes.c_float()
    target_y = ctypes.c_float()
    target_z = ctypes.c_float()
    __ret = _fn(player, object, ctypes.byref(target_x), ctypes.byref(target_y), ctypes.byref(target_z))
    if __ret:
        return (target_x.value, target_y.value, target_z.value)
    return None

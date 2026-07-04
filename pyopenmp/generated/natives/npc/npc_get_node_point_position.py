import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetNodePointPosition", ctypes.c_bool, [ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def npc_get_node_point_position(node_id):
    x = ctypes.c_float()
    y = ctypes.c_float()
    z = ctypes.c_float()
    __ret = _fn(node_id, ctypes.byref(x), ctypes.byref(y), ctypes.byref(z))
    if __ret:
        return (x.value, y.value, z.value)
    return None

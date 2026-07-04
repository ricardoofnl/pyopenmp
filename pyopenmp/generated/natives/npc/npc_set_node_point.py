import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetNodePoint", ctypes.c_bool, [ctypes.c_int, ctypes.c_int])


def npc_set_node_point(node_id, point_id):
    return _fn(node_id, point_id)

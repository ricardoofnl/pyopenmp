import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetNodePointCount", ctypes.c_int, [ctypes.c_int])


def npc_get_node_point_count(node_id):
    return _fn(node_id)

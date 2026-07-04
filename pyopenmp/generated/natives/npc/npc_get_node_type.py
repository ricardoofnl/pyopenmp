import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetNodeType", ctypes.c_int, [ctypes.c_int])


def npc_get_node_type(node_id):
    return _fn(node_id)

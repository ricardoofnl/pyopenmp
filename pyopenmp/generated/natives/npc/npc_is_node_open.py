import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsNodeOpen", ctypes.c_bool, [ctypes.c_int])


def npc_is_node_open(node_id):
    return _fn(node_id)

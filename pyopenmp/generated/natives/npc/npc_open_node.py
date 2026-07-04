import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_OpenNode", ctypes.c_bool, [ctypes.c_int])


def npc_open_node(node_id):
    return _fn(node_id)

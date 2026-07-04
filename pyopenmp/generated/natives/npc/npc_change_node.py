import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_ChangeNode", ctypes.c_int, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def npc_change_node(npc, node_id, link_id):
    return _fn(npc, node_id, link_id)

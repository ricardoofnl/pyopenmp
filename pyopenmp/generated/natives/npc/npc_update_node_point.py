import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_UpdateNodePoint", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_update_node_point(npc, point_id):
    return _fn(npc, point_id)

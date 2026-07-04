import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetNodeInfo", ctypes.c_bool, [ctypes.c_int, ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32), ctypes.POINTER(ctypes.c_uint32)])


def npc_get_node_info(node_id):
    vehicle_nodes = ctypes.c_uint32()
    ped_nodes = ctypes.c_uint32()
    navi_nodes = ctypes.c_uint32()
    __ret = _fn(node_id, ctypes.byref(vehicle_nodes), ctypes.byref(ped_nodes), ctypes.byref(navi_nodes))
    if __ret:
        return (vehicle_nodes.value, ped_nodes.value, navi_nodes.value)
    return None

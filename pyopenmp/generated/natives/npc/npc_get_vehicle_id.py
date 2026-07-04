import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicleID", ctypes.c_int, [ctypes.c_void_p])


def npc_get_vehicle_id(npc):
    return _fn(npc)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetVehicleHealth", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def npc_set_vehicle_health(npc, health):
    return _fn(npc, health)

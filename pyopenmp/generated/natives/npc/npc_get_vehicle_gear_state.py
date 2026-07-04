import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicleGearState", ctypes.c_int, [ctypes.c_void_p])


def npc_get_vehicle_gear_state(npc):
    return _fn(npc)

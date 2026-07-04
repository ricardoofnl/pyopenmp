import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetVehicleGearState", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_vehicle_gear_state(npc, gear_state):
    return _fn(npc, gear_state)

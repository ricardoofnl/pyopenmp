import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetSurfingVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p])


def npc_set_surfing_vehicle(npc, vehicle):
    return _fn(npc, vehicle)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetSurfingVehicle", ctypes.c_int, [ctypes.c_void_p])


def npc_get_surfing_vehicle(npc):
    return _fn(npc)

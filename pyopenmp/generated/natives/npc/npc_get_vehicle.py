import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicle", ctypes.c_void_p, [ctypes.c_void_p])


def npc_get_vehicle(npc):
    return _fn(npc)

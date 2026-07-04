import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicleHealth", ctypes.c_float, [ctypes.c_void_p])


def npc_get_vehicle_health(npc):
    return _fn(npc)

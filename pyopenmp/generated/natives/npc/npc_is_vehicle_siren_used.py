import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsVehicleSirenUsed", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_vehicle_siren_used(npc):
    return _fn(npc)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicleHydraThrusters", ctypes.c_int, [ctypes.c_void_p])


def npc_get_vehicle_hydra_thrusters(npc):
    return _fn(npc)

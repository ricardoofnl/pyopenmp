import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetVehicleHydraThrusters", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int])


def npc_set_vehicle_hydra_thrusters(npc, direction):
    return _fn(npc, direction)

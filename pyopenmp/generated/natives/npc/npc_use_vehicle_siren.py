import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_UseVehicleSiren", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_bool])


def npc_use_vehicle_siren(npc, use):
    return _fn(npc, use)

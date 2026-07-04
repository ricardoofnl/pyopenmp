import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_RemoveFromVehicle", ctypes.c_bool, [ctypes.c_void_p])


def npc_remove_from_vehicle(npc):
    return _fn(npc)

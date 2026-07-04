import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_IsEnteringVehicle", ctypes.c_bool, [ctypes.c_void_p])


def npc_is_entering_vehicle(npc):
    return _fn(npc)

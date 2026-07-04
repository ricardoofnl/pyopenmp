import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicleSeat", ctypes.c_int, [ctypes.c_void_p])


def npc_get_vehicle_seat(npc):
    return _fn(npc)

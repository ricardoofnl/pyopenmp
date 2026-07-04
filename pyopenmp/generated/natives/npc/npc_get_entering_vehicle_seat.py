import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetEnteringVehicleSeat", ctypes.c_int, [ctypes.c_void_p])


def npc_get_entering_vehicle_seat(npc):
    return _fn(npc)

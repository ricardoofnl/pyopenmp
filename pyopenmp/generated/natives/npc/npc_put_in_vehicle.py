import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_PutInVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int])


def npc_put_in_vehicle(npc, vehicle, seat_id):
    return _fn(npc, vehicle, seat_id)

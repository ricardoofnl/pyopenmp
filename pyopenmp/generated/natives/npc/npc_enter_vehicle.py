import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_EnterVehicle", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.c_int])


def npc_enter_vehicle(npc, vehicle, seat_id, move_type):
    return _fn(npc, vehicle, seat_id, move_type)

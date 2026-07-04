import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_SetVehicleTrainSpeed", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_float])


def npc_set_vehicle_train_speed(npc, speed):
    return _fn(npc, speed)

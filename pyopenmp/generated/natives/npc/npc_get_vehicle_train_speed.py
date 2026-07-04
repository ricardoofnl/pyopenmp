import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_GetVehicleTrainSpeed", ctypes.c_float, [ctypes.c_void_p])


def npc_get_vehicle_train_speed(npc):
    return _fn(npc)

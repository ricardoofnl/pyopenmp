import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Vehicle_UseManualEngineAndLights", ctypes.c_bool, [])


def vehicle_use_manual_engine_and_lights():
    return _fn()

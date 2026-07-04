import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("CustomModel_AddSimpleModelTimed", ctypes.c_bool, [ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int])


def custom_model_add_simple_model_timed(virtual_world, baseid, newid, dff, texture_library, time_on, time_off):
    return _fn(virtual_world, baseid, newid, _capi.enc(dff), _capi.enc(texture_library), time_on, time_off)

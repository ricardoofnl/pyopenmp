import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("CustomModel_AddCharModel", ctypes.c_bool, [ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p])


def custom_model_add_char_model(baseid, newid, dff, texture_library):
    return _fn(baseid, newid, _capi.enc(dff), _capi.enc(texture_library))

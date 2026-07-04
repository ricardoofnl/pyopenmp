import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("CustomModel_IsValid", ctypes.c_bool, [ctypes.c_int])


def custom_model_is_valid(model_id):
    return _fn(model_id)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("CustomModel_GetPath", ctypes.c_bool, [ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView)])


def custom_model_get_path(model_id):
    dff_path = _capi.CAPIStringView()
    txd_path = _capi.CAPIStringView()
    __ret = _fn(model_id, ctypes.byref(dff_path), ctypes.byref(txd_path))
    if __ret:
        return (_capi.read_view(dff_path), _capi.read_view(txd_path))
    return None

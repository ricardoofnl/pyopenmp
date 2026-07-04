import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("CustomModel_FindModelFileNameFromCRC", ctypes.c_int, [ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView)])


def custom_model_find_model_file_name_from_crc(crc):
    output = _capi.CAPIStringView()
    __ret = _fn(crc, ctypes.byref(output))
    return _capi.read_view(output)

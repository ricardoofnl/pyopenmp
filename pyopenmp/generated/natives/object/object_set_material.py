import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_SetMaterial", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint32])


def object_set_material(object, material_index, model_id, texture_library, texture_name, material_color):
    return _fn(object, material_index, model_id, _capi.enc(texture_library), _capi.enc(texture_name), material_color)

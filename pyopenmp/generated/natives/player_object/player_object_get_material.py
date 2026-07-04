import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetMaterial", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(ctypes.c_int)])


def player_object_get_material(player, object, material_index):
    modelid = ctypes.c_int()
    texture_library = _capi.CAPIStringView()
    texture_name = _capi.CAPIStringView()
    material_color = ctypes.c_int()
    __ret = _fn(player, object, material_index, ctypes.byref(modelid), ctypes.byref(texture_library), ctypes.byref(texture_name), ctypes.byref(material_color))
    if __ret:
        return (modelid.value, _capi.read_view(texture_library), _capi.read_view(texture_name), material_color.value)
    return None

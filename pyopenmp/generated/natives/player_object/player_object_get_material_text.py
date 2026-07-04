import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerObject_GetMaterialText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_bool), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def player_object_get_material_text(player, object, material_index):
    text = _capi.CAPIStringView()
    material_size = ctypes.c_int()
    font_face = _capi.CAPIStringView()
    font_size = ctypes.c_int()
    bold = ctypes.c_bool()
    font_color = ctypes.c_int()
    background_color = ctypes.c_int()
    text_alignment = ctypes.c_int()
    __ret = _fn(player, object, material_index, ctypes.byref(text), ctypes.byref(material_size), ctypes.byref(font_face), ctypes.byref(font_size), ctypes.byref(bold), ctypes.byref(font_color), ctypes.byref(background_color), ctypes.byref(text_alignment))
    if __ret:
        return (_capi.read_view(text), material_size.value, _capi.read_view(font_face), font_size.value, bold.value, font_color.value, background_color.value, text_alignment.value)
    return None

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Object_SetMaterialText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_bool, ctypes.c_uint32, ctypes.c_uint32, ctypes.c_int])


def object_set_material_text(object, text, material_index, material_size, fontface, fontsize, bold, font_color, background_color, textalignment):
    return _fn(object, _capi.enc(text), material_index, material_size, _capi.enc(fontface), fontsize, bold, font_color, background_color, textalignment)

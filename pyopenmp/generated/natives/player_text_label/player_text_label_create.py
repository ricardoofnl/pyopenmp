import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_Create", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_bool, ctypes.POINTER(ctypes.c_int)])


def player_text_label_create(player, text, color, x, y, z, draw_distance, attached_player, attached_vehicle, los):
    id = ctypes.c_int()
    __ret = _fn(player, _capi.enc(text), color, x, y, z, draw_distance, attached_player, attached_vehicle, los, ctypes.byref(id))
    return (__ret, id.value)

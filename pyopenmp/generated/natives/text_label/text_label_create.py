import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_Create", ctypes.c_void_p, [ctypes.c_char_p, ctypes.c_uint32, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_int, ctypes.c_bool, ctypes.POINTER(ctypes.c_int)])


def text_label_create(text, color, x, y, z, draw_distance, virtual_world, los):
    id = ctypes.c_int()
    __ret = _fn(_capi.enc(text), color, x, y, z, draw_distance, virtual_world, los, ctypes.byref(id))
    return (__ret, id.value)

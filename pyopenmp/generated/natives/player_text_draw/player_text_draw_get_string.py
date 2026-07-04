import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_GetString", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def player_text_draw_get_string(player, textdraw):
    text = _capi.CAPIStringView()
    __ret = _fn(player, textdraw, ctypes.byref(text))
    if __ret:
        return _capi.read_view(text)
    return None

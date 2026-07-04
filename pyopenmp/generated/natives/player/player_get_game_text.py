import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetGameText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_int, ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)])


def player_get_game_text(player, style):
    message = _capi.CAPIStringView()
    time = ctypes.c_int()
    remaining = ctypes.c_int()
    __ret = _fn(player, style, ctypes.byref(message), ctypes.byref(time), ctypes.byref(remaining))
    if __ret:
        return (_capi.read_view(message), time.value, remaining.value)
    return None

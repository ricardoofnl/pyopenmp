import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_HideGameTextForAll", ctypes.c_bool, [ctypes.c_int])


def core_hide_game_text_for_all(style):
    return _fn(style)

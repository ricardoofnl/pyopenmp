import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_ToggleChatTextReplacement", ctypes.c_bool, [ctypes.c_bool])


def core_toggle_chat_text_replacement(enable):
    return _fn(enable)

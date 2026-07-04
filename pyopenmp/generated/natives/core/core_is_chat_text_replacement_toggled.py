import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Core_IsChatTextReplacementToggled", ctypes.c_bool, [])


def core_is_chat_text_replacement_toggled():
    return _fn()

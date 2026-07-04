import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_FromID", ctypes.c_void_p, [ctypes.c_void_p, ctypes.c_int])


def player_text_label_from_id(player, textlabelid):
    return _fn(player, textlabelid)

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextLabel_GetText", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def player_text_label_get_text(player, textlabel):
    output = _capi.CAPIStringView()
    __ret = _fn(player, textlabel, ctypes.byref(output))
    if __ret:
        return _capi.read_view(output)
    return None

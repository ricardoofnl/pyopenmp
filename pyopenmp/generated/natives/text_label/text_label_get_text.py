import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("TextLabel_GetText", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(_capi.CAPIStringView)])


def text_label_get_text(textlabel):
    output = _capi.CAPIStringView()
    __ret = _fn(textlabel, ctypes.byref(output))
    if __ret:
        return _capi.read_view(output)
    return None

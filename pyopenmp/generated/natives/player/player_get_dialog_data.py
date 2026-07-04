import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("Player_GetDialogData", ctypes.c_bool, [ctypes.c_void_p, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView), ctypes.POINTER(_capi.CAPIStringView)])


def player_get_dialog_data(player):
    dialogid = ctypes.c_int()
    style = ctypes.c_int()
    title = _capi.CAPIStringView()
    body = _capi.CAPIStringView()
    button1 = _capi.CAPIStringView()
    button2 = _capi.CAPIStringView()
    __ret = _fn(player, ctypes.byref(dialogid), ctypes.byref(style), ctypes.byref(title), ctypes.byref(body), ctypes.byref(button1), ctypes.byref(button2))
    if __ret:
        return (dialogid.value, style.value, _capi.read_view(title), _capi.read_view(body), _capi.read_view(button1), _capi.read_view(button2))
    return None

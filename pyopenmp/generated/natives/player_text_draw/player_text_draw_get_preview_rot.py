import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("PlayerTextDraw_GetPreviewRot", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_void_p, ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float)])


def player_text_draw_get_preview_rot(player, textdraw):
    rx = ctypes.c_float()
    ry = ctypes.c_float()
    rz = ctypes.c_float()
    zoom = ctypes.c_float()
    __ret = _fn(player, textdraw, ctypes.byref(rx), ctypes.byref(ry), ctypes.byref(rz), ctypes.byref(zoom))
    if __ret:
        return (rx.value, ry.value, rz.value, zoom.value)
    return None

import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("CustomModel_RedirectDownload", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p])


def custom_model_redirect_download(player, url):
    return _fn(player, _capi.enc(url))

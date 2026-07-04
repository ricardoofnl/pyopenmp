import ctypes
import os
import sys

EVENT_PRIORITY_HIGHEST = 0
EVENT_PRIORITY_FAIRLY_HIGH = 1
EVENT_PRIORITY_DEFAULT = 2
EVENT_PRIORITY_FAIRLY_LOW = 3
EVENT_PRIORITY_LOWEST = 4


class CAPIStringView(ctypes.Structure):
    _fields_ = [("len", ctypes.c_uint), ("data", ctypes.c_void_p)]


class CAPIStringBuffer(ctypes.Structure):
    _fields_ = [
        ("capacity", ctypes.c_uint),
        ("len", ctypes.c_uint),
        ("data", ctypes.c_char_p),
    ]


class ComponentVersion(ctypes.Structure):
    _fields_ = [
        ("major", ctypes.c_uint8),
        ("minor", ctypes.c_uint8),
        ("patch", ctypes.c_uint8),
        ("prerel", ctypes.c_uint16),
    ]


class EventArgs_Common(ctypes.Structure):
    _fields_ = [("size", ctypes.c_int), ("list", ctypes.POINTER(ctypes.c_void_p))]


_lib = None


def _default_path():
    name = "$CAPI.dll" if sys.platform.startswith("win") else "$CAPI.so"
    return os.path.join("components", name)


def load():
    global _lib
    if _lib is None:
        _lib = ctypes.CDLL(os.environ.get("PYOPENMP_CAPI", _default_path()))
    return _lib


def lazy(name, restype, argtypes):
    state = {}

    def call(*args):
        fn = state.get("fn")
        if fn is None:
            fn = getattr(load(), name)
            fn.restype = restype
            fn.argtypes = argtypes
            state["fn"] = fn
        return fn(*args)

    return call


def enc(value):
    if isinstance(value, bytes):
        return value
    return value.encode("utf-8")


def read_view(view):
    if not view.data or view.len == 0:
        return ""
    return ctypes.string_at(view.data, view.len).decode("utf-8", "replace")


class OutBuffer:
    def __init__(self, capacity=512):
        self._buf = ctypes.create_string_buffer(capacity)
        self.raw = CAPIStringBuffer(
            capacity, 0, ctypes.cast(self._buf, ctypes.c_char_p)
        )

    def value(self):
        return self._buf.raw[: self.raw.len].decode("utf-8", "replace")


def _deref(lst, index, ctype):
    return ctypes.cast(
        ctypes.c_void_p(lst[index]), ctypes.POINTER(ctype)
    ).contents.value


def deref_handle(lst, index):
    return _deref(lst, index, ctypes.c_void_p)


def deref_int(lst, index):
    return _deref(lst, index, ctypes.c_int)


def deref_float(lst, index):
    return _deref(lst, index, ctypes.c_float)


def deref_bool(lst, index):
    return _deref(lst, index, ctypes.c_bool)


def deref_view(lst, index):
    view = ctypes.cast(
        ctypes.c_void_p(lst[index]), ctypes.POINTER(CAPIStringView)
    ).contents
    return read_view(view)

import ctypes
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def build_stub(tmp):
    out = os.path.join(tmp, "stub.so")
    subprocess.check_call(
        ["gcc", "-shared", "-fPIC", os.path.join(ROOT, "tests", "stub.c"), "-o", out]
    )
    return out


def test_natives():
    from pyopenmp.generated import natives

    assert natives.core_log("hello") is True
    assert natives.player_get_health(0) == 42.5
    assert natives.player_get_name(0) == "Test"
    assert natives.player_send_client_message(0, 0xFF00FF, "hi") is True


def test_event_handle():
    from pyopenmp import _capi
    from pyopenmp.generated import events

    seen = {}

    @events.on_player_connect
    def handler(player):
        seen["ptr"] = player.ptr

    holder = ctypes.c_void_p(0xABCD)
    array = (ctypes.c_void_p * 1)()
    array[0] = ctypes.cast(ctypes.byref(holder), ctypes.c_void_p)
    args = _capi.EventArgs_Common(1, ctypes.cast(array, ctypes.POINTER(ctypes.c_void_p)))

    result = events._tramp_on_player_connect(ctypes.pointer(args))
    assert seen.get("ptr") == 0xABCD
    assert result is True


def test_event_string_and_return():
    from pyopenmp import _capi
    from pyopenmp.generated import events

    seen = {}

    @events.on_player_command_text
    def command(player, text):
        seen["text"] = text
        return True

    holder = ctypes.c_void_p(0x1)
    view = _capi.CAPIStringView()
    buffer = ctypes.create_string_buffer(b"/help")
    view.data = ctypes.cast(buffer, ctypes.c_void_p)
    view.len = 5
    array = (ctypes.c_void_p * 2)()
    array[0] = ctypes.cast(ctypes.byref(holder), ctypes.c_void_p)
    array[1] = ctypes.cast(ctypes.byref(view), ctypes.c_void_p)
    args = _capi.EventArgs_Common(2, ctypes.cast(array, ctypes.POINTER(ctypes.c_void_p)))

    result = events._tramp_on_player_command_text(ctypes.pointer(args))
    assert seen.get("text") == "/help"
    assert result is True


def main():
    with tempfile.TemporaryDirectory() as tmp:
        os.environ["PYOPENMP_CAPI"] = build_stub(tmp)
        test_natives()
        test_event_handle()
        test_event_string_and_return()
    print("ALL TESTS PASSED")


if __name__ == "__main__":
    main()

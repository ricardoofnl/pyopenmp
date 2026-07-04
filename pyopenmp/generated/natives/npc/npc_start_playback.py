import ctypes

from pyopenmp import _capi

_fn = _capi.lazy("NPC_StartPlayback", ctypes.c_bool, [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_bool, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float, ctypes.c_float])


def npc_start_playback(npc, record_name, auto_unload, start_pos_x, start_pos_y, start_pos_z, start_rot_x, start_rot_y, start_rot_z):
    return _fn(npc, _capi.enc(record_name), auto_unload, start_pos_x, start_pos_y, start_pos_z, start_rot_x, start_rot_y, start_rot_z)

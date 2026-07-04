import ctypes

from pyopenmp import _capi
from pyopenmp import event
from pyopenmp.generated import entities

_EVENT_CB = ctypes.CFUNCTYPE(ctypes.c_bool, ctypes.POINTER(_capi.EventArgs_Common))
_trampolines = []


def _tramp_on_actor_stream_in(args):
    list_ = args.contents.list
    actor = entities.Actor(_capi.deref_handle(list_, 0))
    for_player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onActorStreamIn", (actor, for_player), True)


def _tramp_on_actor_stream_out(args):
    list_ = args.contents.list
    actor = entities.Actor(_capi.deref_handle(list_, 0))
    for_player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onActorStreamOut", (actor, for_player), True)


def _tramp_on_client_check_response(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    action_type = _capi.deref_int(list_, 1)
    address = _capi.deref_int(list_, 2)
    result = _capi.deref_int(list_, 3)
    return event.dispatch("onClientCheckResponse", (player, action_type, address, result), True)


def _tramp_on_console_text(args):
    list_ = args.contents.list
    command = _capi.deref_view(list_, 0)
    parameters = _capi.deref_view(list_, 1)
    return event.dispatch("onConsoleText", (command, parameters), False)


def _tramp_on_dialog_response(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    dialog_id = _capi.deref_int(list_, 1)
    response = _capi.deref_int(list_, 2)
    list_item = _capi.deref_int(list_, 3)
    input_text = _capi.deref_view(list_, 4)
    return event.dispatch("onDialogResponse", (player, dialog_id, response, list_item, input_text), True)


def _tramp_on_enter_exit_mod_shop(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    enterexit = _capi.deref_int(list_, 1)
    interior_id = _capi.deref_int(list_, 2)
    return event.dispatch("onEnterExitModShop", (player, enterexit, interior_id), True)


def _tramp_on_incoming_connection(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    ip_address = _capi.deref_view(list_, 1)
    port = _capi.deref_int(list_, 2)
    return event.dispatch("onIncomingConnection", (player, ip_address, port), True)


def _tramp_on_npc_change_node(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    new_node_id = _capi.deref_int(list_, 1)
    old_node_id = _capi.deref_int(list_, 2)
    return event.dispatch("onNPCChangeNode", (npc, new_node_id, old_node_id), True)


def _tramp_on_npc_create(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    return event.dispatch("onNPCCreate", (npc,), True)


def _tramp_on_npc_death(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    killer = entities.Player(_capi.deref_handle(list_, 1))
    reason = _capi.deref_int(list_, 2)
    return event.dispatch("onNPCDeath", (npc, killer, reason), True)


def _tramp_on_npc_destroy(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    return event.dispatch("onNPCDestroy", (npc,), True)


def _tramp_on_npc_finish_move(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    return event.dispatch("onNPCFinishMove", (npc,), True)


def _tramp_on_npc_finish_move_path(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    path_id = _capi.deref_int(list_, 1)
    return event.dispatch("onNPCFinishMovePath", (npc, path_id), True)


def _tramp_on_npc_finish_move_path_point(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    path_id = _capi.deref_int(list_, 1)
    point_id = _capi.deref_int(list_, 2)
    return event.dispatch("onNPCFinishMovePathPoint", (npc, path_id, point_id), True)


def _tramp_on_npc_finish_node(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    node_id = _capi.deref_int(list_, 1)
    return event.dispatch("onNPCFinishNode", (npc, node_id), True)


def _tramp_on_npc_finish_node_point(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    node_id = _capi.deref_int(list_, 1)
    point_id = _capi.deref_int(list_, 2)
    return event.dispatch("onNPCFinishNodePoint", (npc, node_id, point_id), True)


def _tramp_on_npc_give_damage(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    damaged = _capi.deref_handle(list_, 1)
    damage = _capi.deref_float(list_, 2)
    weapon = _capi.deref_int(list_, 3)
    body_part = _capi.deref_int(list_, 4)
    return event.dispatch("onNPCGiveDamage", (npc, damaged, damage, weapon, body_part), False)


def _tramp_on_npc_playback_end(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    record_id = _capi.deref_int(list_, 1)
    return event.dispatch("onNPCPlaybackEnd", (npc, record_id), True)


def _tramp_on_npc_playback_start(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    record_id = _capi.deref_int(list_, 1)
    return event.dispatch("onNPCPlaybackStart", (npc, record_id), True)


def _tramp_on_npc_respawn(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    return event.dispatch("onNPCRespawn", (npc,), True)


def _tramp_on_npc_shot_missed(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    weapon = _capi.deref_int(list_, 1)
    offset_x = _capi.deref_float(list_, 2)
    offset_y = _capi.deref_float(list_, 3)
    offset_z = _capi.deref_float(list_, 4)
    return event.dispatch("onNPCShotMissed", (npc, weapon, offset_x, offset_y, offset_z), True)


def _tramp_on_npc_shot_npc(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    npc_target = _capi.deref_handle(list_, 1)
    weapon = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    return event.dispatch("onNPCShotNPC", (npc, npc_target, weapon, offset_x, offset_y, offset_z), True)


def _tramp_on_npc_shot_object(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    object = entities.Object(_capi.deref_handle(list_, 1))
    weapon = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    return event.dispatch("onNPCShotObject", (npc, object, weapon, offset_x, offset_y, offset_z), True)


def _tramp_on_npc_shot_player(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    player = entities.Player(_capi.deref_handle(list_, 1))
    weapon = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    return event.dispatch("onNPCShotPlayer", (npc, player, weapon, offset_x, offset_y, offset_z), True)


def _tramp_on_npc_shot_player_object(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    player_object = _capi.deref_handle(list_, 1)
    weapon = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    return event.dispatch("onNPCShotPlayerObject", (npc, player_object, weapon, offset_x, offset_y, offset_z), True)


def _tramp_on_npc_shot_vehicle(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    weapon = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    return event.dispatch("onNPCShotVehicle", (npc, vehicle, weapon, offset_x, offset_y, offset_z), True)


def _tramp_on_npc_spawn(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    return event.dispatch("onNPCSpawn", (npc,), True)


def _tramp_on_npc_take_damage(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    damager = entities.Player(_capi.deref_handle(list_, 1))
    damage = _capi.deref_float(list_, 2)
    weapon = _capi.deref_int(list_, 3)
    body_part = _capi.deref_int(list_, 4)
    return event.dispatch("onNPCTakeDamage", (npc, damager, damage, weapon, body_part), True)


def _tramp_on_npc_weapon_state_change(args):
    list_ = args.contents.list
    npc = entities.Npc(_capi.deref_handle(list_, 0))
    new_state = _capi.deref_int(list_, 1)
    old_state = _capi.deref_int(list_, 2)
    return event.dispatch("onNPCWeaponStateChange", (npc, new_state, old_state), True)


def _tramp_on_object_move(args):
    list_ = args.contents.list
    object = entities.Object(_capi.deref_handle(list_, 0))
    return event.dispatch("onObjectMove", (object,), True)


def _tramp_on_player_cancel_player_text_draw_selection(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerCancelPlayerTextDrawSelection", (player,), True)


def _tramp_on_player_cancel_text_draw_selection(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerCancelTextDrawSelection", (player,), True)


def _tramp_on_player_click_gang_zone(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    zone = _capi.deref_handle(list_, 1)
    return event.dispatch("onPlayerClickGangZone", (player, zone), True)


def _tramp_on_player_click_map(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    x = _capi.deref_float(list_, 1)
    y = _capi.deref_float(list_, 2)
    z = _capi.deref_float(list_, 3)
    return event.dispatch("onPlayerClickMap", (player, x, y, z), True)


def _tramp_on_player_click_player(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    clicked = _capi.deref_handle(list_, 1)
    source = _capi.deref_int(list_, 2)
    return event.dispatch("onPlayerClickPlayer", (player, clicked, source), True)


def _tramp_on_player_click_player_text_draw(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    textdraw = entities.TextDraw(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerClickPlayerTextDraw", (player, textdraw), True)


def _tramp_on_player_click_text_draw(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    textdraw = entities.TextDraw(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerClickTextDraw", (player, textdraw), True)


def _tramp_on_player_command_text(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    command = _capi.deref_view(list_, 1)
    return event.dispatch("onPlayerCommandText", (player, command), False)


def _tramp_on_player_connect(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerConnect", (player,), True)


def _tramp_on_player_death(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    killer = entities.Player(_capi.deref_handle(list_, 1))
    reason = _capi.deref_int(list_, 2)
    return event.dispatch("onPlayerDeath", (player, killer, reason), True)


def _tramp_on_player_disconnect(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    reason = _capi.deref_int(list_, 1)
    return event.dispatch("onPlayerDisconnect", (player, reason), True)


def _tramp_on_player_edit_attached_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    saved = _capi.deref_bool(list_, 1)
    index = _capi.deref_int(list_, 2)
    model = _capi.deref_int(list_, 3)
    bone = _capi.deref_int(list_, 4)
    offset_x = _capi.deref_float(list_, 5)
    offset_y = _capi.deref_float(list_, 6)
    offset_z = _capi.deref_float(list_, 7)
    rotation_x = _capi.deref_float(list_, 8)
    rotation_y = _capi.deref_float(list_, 9)
    rotation_z = _capi.deref_float(list_, 10)
    scale_x = _capi.deref_float(list_, 11)
    scale_y = _capi.deref_float(list_, 12)
    scale_z = _capi.deref_float(list_, 13)
    return event.dispatch("onPlayerEditAttachedObject", (player, saved, index, model, bone, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, scale_x, scale_y, scale_z), True)


def _tramp_on_player_edit_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    object = entities.Object(_capi.deref_handle(list_, 1))
    response = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    rotation_x = _capi.deref_float(list_, 6)
    rotation_y = _capi.deref_float(list_, 7)
    rotation_z = _capi.deref_float(list_, 8)
    return event.dispatch("onPlayerEditObject", (player, object, response, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z), True)


def _tramp_on_player_edit_player_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    object = entities.Object(_capi.deref_handle(list_, 1))
    response = _capi.deref_int(list_, 2)
    offset_x = _capi.deref_float(list_, 3)
    offset_y = _capi.deref_float(list_, 4)
    offset_z = _capi.deref_float(list_, 5)
    rotation_x = _capi.deref_float(list_, 6)
    rotation_y = _capi.deref_float(list_, 7)
    rotation_z = _capi.deref_float(list_, 8)
    return event.dispatch("onPlayerEditPlayerObject", (player, object, response, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z), True)


def _tramp_on_player_enter_checkpoint(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerEnterCheckpoint", (player,), True)


def _tramp_on_player_enter_gang_zone(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    zone = _capi.deref_handle(list_, 1)
    return event.dispatch("onPlayerEnterGangZone", (player, zone), True)


def _tramp_on_player_enter_race_checkpoint(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerEnterRaceCheckpoint", (player,), True)


def _tramp_on_player_enter_vehicle(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    passenger = _capi.deref_bool(list_, 2)
    return event.dispatch("onPlayerEnterVehicle", (player, vehicle, passenger), True)


def _tramp_on_player_exit_vehicle(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerExitVehicle", (player, vehicle), True)


def _tramp_on_player_exited_menu(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerExitedMenu", (player,), True)


def _tramp_on_player_finished_downloading(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vw = _capi.deref_int(list_, 1)
    return event.dispatch("onPlayerFinishedDownloading", (player, vw), True)


def _tramp_on_player_give_damage(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    to = _capi.deref_handle(list_, 1)
    amount = _capi.deref_float(list_, 2)
    weapon = _capi.deref_int(list_, 3)
    bodypart = _capi.deref_int(list_, 4)
    return event.dispatch("onPlayerGiveDamage", (player, to, amount, weapon, bodypart), True)


def _tramp_on_player_give_damage_actor(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    actor = entities.Actor(_capi.deref_handle(list_, 1))
    amount = _capi.deref_float(list_, 2)
    weapon = _capi.deref_int(list_, 3)
    part = _capi.deref_int(list_, 4)
    return event.dispatch("onPlayerGiveDamageActor", (player, actor, amount, weapon, part), True)


def _tramp_on_player_interior_change(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    new_interior = _capi.deref_int(list_, 1)
    old_interior = _capi.deref_int(list_, 2)
    return event.dispatch("onPlayerInteriorChange", (player, new_interior, old_interior), True)


def _tramp_on_player_key_state_change(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    new_keys = _capi.deref_int(list_, 1)
    old_keys = _capi.deref_int(list_, 2)
    return event.dispatch("onPlayerKeyStateChange", (player, new_keys, old_keys), True)


def _tramp_on_player_leave_checkpoint(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerLeaveCheckpoint", (player,), True)


def _tramp_on_player_leave_gang_zone(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    zone = _capi.deref_handle(list_, 1)
    return event.dispatch("onPlayerLeaveGangZone", (player, zone), True)


def _tramp_on_player_leave_race_checkpoint(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerLeaveRaceCheckpoint", (player,), True)


def _tramp_on_player_object_move(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    object = entities.Object(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerObjectMove", (player, object), True)


def _tramp_on_player_pick_up_pickup(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    pickup = entities.Pickup(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerPickUpPickup", (player, pickup), True)


def _tramp_on_player_request_class(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    class_id = _capi.deref_int(list_, 1)
    return event.dispatch("onPlayerRequestClass", (player, class_id), True)


def _tramp_on_player_request_download(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    type = _capi.deref_int(list_, 1)
    checksum = _capi.deref_int(list_, 2)
    return event.dispatch("onPlayerRequestDownload", (player, type, checksum), True)


def _tramp_on_player_request_spawn(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerRequestSpawn", (player,), True)


def _tramp_on_player_select_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    object = entities.Object(_capi.deref_handle(list_, 1))
    model = _capi.deref_int(list_, 2)
    x = _capi.deref_float(list_, 3)
    y = _capi.deref_float(list_, 4)
    z = _capi.deref_float(list_, 5)
    return event.dispatch("onPlayerSelectObject", (player, object, model, x, y, z), True)


def _tramp_on_player_select_player_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    object = entities.Object(_capi.deref_handle(list_, 1))
    model = _capi.deref_int(list_, 2)
    x = _capi.deref_float(list_, 3)
    y = _capi.deref_float(list_, 4)
    z = _capi.deref_float(list_, 5)
    return event.dispatch("onPlayerSelectPlayerObject", (player, object, model, x, y, z), True)


def _tramp_on_player_selected_menu_row(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    row = _capi.deref_int(list_, 1)
    return event.dispatch("onPlayerSelectedMenuRow", (player, row), True)


def _tramp_on_player_shot_missed(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    weapon = _capi.deref_int(list_, 1)
    x = _capi.deref_float(list_, 2)
    y = _capi.deref_float(list_, 3)
    z = _capi.deref_float(list_, 4)
    return event.dispatch("onPlayerShotMissed", (player, weapon, x, y, z), True)


def _tramp_on_player_shot_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    target = _capi.deref_handle(list_, 1)
    weapon = _capi.deref_int(list_, 2)
    x = _capi.deref_float(list_, 3)
    y = _capi.deref_float(list_, 4)
    z = _capi.deref_float(list_, 5)
    return event.dispatch("onPlayerShotObject", (player, target, weapon, x, y, z), True)


def _tramp_on_player_shot_player(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    target = _capi.deref_handle(list_, 1)
    weapon = _capi.deref_int(list_, 2)
    x = _capi.deref_float(list_, 3)
    y = _capi.deref_float(list_, 4)
    z = _capi.deref_float(list_, 5)
    return event.dispatch("onPlayerShotPlayer", (player, target, weapon, x, y, z), True)


def _tramp_on_player_shot_player_object(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    target = _capi.deref_handle(list_, 1)
    weapon = _capi.deref_int(list_, 2)
    x = _capi.deref_float(list_, 3)
    y = _capi.deref_float(list_, 4)
    z = _capi.deref_float(list_, 5)
    return event.dispatch("onPlayerShotPlayerObject", (player, target, weapon, x, y, z), True)


def _tramp_on_player_shot_vehicle(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    target = _capi.deref_handle(list_, 1)
    weapon = _capi.deref_int(list_, 2)
    x = _capi.deref_float(list_, 3)
    y = _capi.deref_float(list_, 4)
    z = _capi.deref_float(list_, 5)
    return event.dispatch("onPlayerShotVehicle", (player, target, weapon, x, y, z), True)


def _tramp_on_player_spawn(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerSpawn", (player,), True)


def _tramp_on_player_state_change(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    new_state = _capi.deref_int(list_, 1)
    old_state = _capi.deref_int(list_, 2)
    return event.dispatch("onPlayerStateChange", (player, new_state, old_state), True)


def _tramp_on_player_stream_in(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    for_player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerStreamIn", (player, for_player), True)


def _tramp_on_player_stream_out(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    for_player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onPlayerStreamOut", (player, for_player), True)


def _tramp_on_player_take_damage(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    from_ = _capi.deref_handle(list_, 1)
    amount = _capi.deref_float(list_, 2)
    weapon = _capi.deref_int(list_, 3)
    bodypart = _capi.deref_int(list_, 4)
    return event.dispatch("onPlayerTakeDamage", (player, from_, amount, weapon, bodypart), True)


def _tramp_on_player_text(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    text = _capi.deref_view(list_, 1)
    return event.dispatch("onPlayerText", (player, text), True)


def _tramp_on_player_update(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    return event.dispatch("onPlayerUpdate", (player,), True)


def _tramp_on_rcon_login_attempt(args):
    list_ = args.contents.list
    address = _capi.deref_view(list_, 0)
    password = _capi.deref_view(list_, 1)
    success = _capi.deref_bool(list_, 2)
    return event.dispatch("onRconLoginAttempt", (address, password, success), False)


def _tramp_on_tick(args):
    list_ = args.contents.list
    elapsed = _capi.deref_int(list_, 0)
    return event.dispatch("onTick", (elapsed,), True)


def _tramp_on_trailer_update(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    trailer = _capi.deref_handle(list_, 1)
    return event.dispatch("onTrailerUpdate", (player, trailer), True)


def _tramp_on_unoccupied_vehicle_update(args):
    list_ = args.contents.list
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 0))
    player = entities.Player(_capi.deref_handle(list_, 1))
    seat = _capi.deref_int(list_, 2)
    pos_x = _capi.deref_float(list_, 3)
    pos_y = _capi.deref_float(list_, 4)
    pos_z = _capi.deref_float(list_, 5)
    velocity_x = _capi.deref_float(list_, 6)
    velocity_y = _capi.deref_float(list_, 7)
    velocity_z = _capi.deref_float(list_, 8)
    return event.dispatch("onUnoccupiedVehicleUpdate", (vehicle, player, seat, pos_x, pos_y, pos_z, velocity_x, velocity_y, velocity_z), True)


def _tramp_on_vehicle_damage_status_update(args):
    list_ = args.contents.list
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 0))
    player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onVehicleDamageStatusUpdate", (vehicle, player), True)


def _tramp_on_vehicle_death(args):
    list_ = args.contents.list
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 0))
    player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onVehicleDeath", (vehicle, player), True)


def _tramp_on_vehicle_mod(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    component = _capi.deref_int(list_, 2)
    return event.dispatch("onVehicleMod", (player, vehicle, component), True)


def _tramp_on_vehicle_paint_job(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    paint_job = _capi.deref_int(list_, 2)
    return event.dispatch("onVehiclePaintJob", (player, vehicle, paint_job), True)


def _tramp_on_vehicle_respray(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    color1 = _capi.deref_int(list_, 2)
    color2 = _capi.deref_int(list_, 3)
    return event.dispatch("onVehicleRespray", (player, vehicle, color1, color2), True)


def _tramp_on_vehicle_siren_state_change(args):
    list_ = args.contents.list
    player = entities.Player(_capi.deref_handle(list_, 0))
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 1))
    siren_state = _capi.deref_int(list_, 2)
    return event.dispatch("onVehicleSirenStateChange", (player, vehicle, siren_state), True)


def _tramp_on_vehicle_spawn(args):
    list_ = args.contents.list
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 0))
    return event.dispatch("onVehicleSpawn", (vehicle,), True)


def _tramp_on_vehicle_stream_in(args):
    list_ = args.contents.list
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 0))
    player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onVehicleStreamIn", (vehicle, player), True)


def _tramp_on_vehicle_stream_out(args):
    list_ = args.contents.list
    vehicle = entities.Vehicle(_capi.deref_handle(list_, 0))
    player = entities.Player(_capi.deref_handle(list_, 1))
    return event.dispatch("onVehicleStreamOut", (vehicle, player), True)


_TABLE = [
    ("onActorStreamIn", _tramp_on_actor_stream_in),
    ("onActorStreamOut", _tramp_on_actor_stream_out),
    ("onClientCheckResponse", _tramp_on_client_check_response),
    ("onConsoleText", _tramp_on_console_text),
    ("onDialogResponse", _tramp_on_dialog_response),
    ("onEnterExitModShop", _tramp_on_enter_exit_mod_shop),
    ("onIncomingConnection", _tramp_on_incoming_connection),
    ("onNPCChangeNode", _tramp_on_npc_change_node),
    ("onNPCCreate", _tramp_on_npc_create),
    ("onNPCDeath", _tramp_on_npc_death),
    ("onNPCDestroy", _tramp_on_npc_destroy),
    ("onNPCFinishMove", _tramp_on_npc_finish_move),
    ("onNPCFinishMovePath", _tramp_on_npc_finish_move_path),
    ("onNPCFinishMovePathPoint", _tramp_on_npc_finish_move_path_point),
    ("onNPCFinishNode", _tramp_on_npc_finish_node),
    ("onNPCFinishNodePoint", _tramp_on_npc_finish_node_point),
    ("onNPCGiveDamage", _tramp_on_npc_give_damage),
    ("onNPCPlaybackEnd", _tramp_on_npc_playback_end),
    ("onNPCPlaybackStart", _tramp_on_npc_playback_start),
    ("onNPCRespawn", _tramp_on_npc_respawn),
    ("onNPCShotMissed", _tramp_on_npc_shot_missed),
    ("onNPCShotNPC", _tramp_on_npc_shot_npc),
    ("onNPCShotObject", _tramp_on_npc_shot_object),
    ("onNPCShotPlayer", _tramp_on_npc_shot_player),
    ("onNPCShotPlayerObject", _tramp_on_npc_shot_player_object),
    ("onNPCShotVehicle", _tramp_on_npc_shot_vehicle),
    ("onNPCSpawn", _tramp_on_npc_spawn),
    ("onNPCTakeDamage", _tramp_on_npc_take_damage),
    ("onNPCWeaponStateChange", _tramp_on_npc_weapon_state_change),
    ("onObjectMove", _tramp_on_object_move),
    ("onPlayerCancelPlayerTextDrawSelection", _tramp_on_player_cancel_player_text_draw_selection),
    ("onPlayerCancelTextDrawSelection", _tramp_on_player_cancel_text_draw_selection),
    ("onPlayerClickGangZone", _tramp_on_player_click_gang_zone),
    ("onPlayerClickMap", _tramp_on_player_click_map),
    ("onPlayerClickPlayer", _tramp_on_player_click_player),
    ("onPlayerClickPlayerTextDraw", _tramp_on_player_click_player_text_draw),
    ("onPlayerClickTextDraw", _tramp_on_player_click_text_draw),
    ("onPlayerCommandText", _tramp_on_player_command_text),
    ("onPlayerConnect", _tramp_on_player_connect),
    ("onPlayerDeath", _tramp_on_player_death),
    ("onPlayerDisconnect", _tramp_on_player_disconnect),
    ("onPlayerEditAttachedObject", _tramp_on_player_edit_attached_object),
    ("onPlayerEditObject", _tramp_on_player_edit_object),
    ("onPlayerEditPlayerObject", _tramp_on_player_edit_player_object),
    ("onPlayerEnterCheckpoint", _tramp_on_player_enter_checkpoint),
    ("onPlayerEnterGangZone", _tramp_on_player_enter_gang_zone),
    ("onPlayerEnterRaceCheckpoint", _tramp_on_player_enter_race_checkpoint),
    ("onPlayerEnterVehicle", _tramp_on_player_enter_vehicle),
    ("onPlayerExitVehicle", _tramp_on_player_exit_vehicle),
    ("onPlayerExitedMenu", _tramp_on_player_exited_menu),
    ("onPlayerFinishedDownloading", _tramp_on_player_finished_downloading),
    ("onPlayerGiveDamage", _tramp_on_player_give_damage),
    ("onPlayerGiveDamageActor", _tramp_on_player_give_damage_actor),
    ("onPlayerInteriorChange", _tramp_on_player_interior_change),
    ("onPlayerKeyStateChange", _tramp_on_player_key_state_change),
    ("onPlayerLeaveCheckpoint", _tramp_on_player_leave_checkpoint),
    ("onPlayerLeaveGangZone", _tramp_on_player_leave_gang_zone),
    ("onPlayerLeaveRaceCheckpoint", _tramp_on_player_leave_race_checkpoint),
    ("onPlayerObjectMove", _tramp_on_player_object_move),
    ("onPlayerPickUpPickup", _tramp_on_player_pick_up_pickup),
    ("onPlayerRequestClass", _tramp_on_player_request_class),
    ("onPlayerRequestDownload", _tramp_on_player_request_download),
    ("onPlayerRequestSpawn", _tramp_on_player_request_spawn),
    ("onPlayerSelectObject", _tramp_on_player_select_object),
    ("onPlayerSelectPlayerObject", _tramp_on_player_select_player_object),
    ("onPlayerSelectedMenuRow", _tramp_on_player_selected_menu_row),
    ("onPlayerShotMissed", _tramp_on_player_shot_missed),
    ("onPlayerShotObject", _tramp_on_player_shot_object),
    ("onPlayerShotPlayer", _tramp_on_player_shot_player),
    ("onPlayerShotPlayerObject", _tramp_on_player_shot_player_object),
    ("onPlayerShotVehicle", _tramp_on_player_shot_vehicle),
    ("onPlayerSpawn", _tramp_on_player_spawn),
    ("onPlayerStateChange", _tramp_on_player_state_change),
    ("onPlayerStreamIn", _tramp_on_player_stream_in),
    ("onPlayerStreamOut", _tramp_on_player_stream_out),
    ("onPlayerTakeDamage", _tramp_on_player_take_damage),
    ("onPlayerText", _tramp_on_player_text),
    ("onPlayerUpdate", _tramp_on_player_update),
    ("onRconLoginAttempt", _tramp_on_rcon_login_attempt),
    ("onTick", _tramp_on_tick),
    ("onTrailerUpdate", _tramp_on_trailer_update),
    ("onUnoccupiedVehicleUpdate", _tramp_on_unoccupied_vehicle_update),
    ("onVehicleDamageStatusUpdate", _tramp_on_vehicle_damage_status_update),
    ("onVehicleDeath", _tramp_on_vehicle_death),
    ("onVehicleMod", _tramp_on_vehicle_mod),
    ("onVehiclePaintJob", _tramp_on_vehicle_paint_job),
    ("onVehicleRespray", _tramp_on_vehicle_respray),
    ("onVehicleSirenStateChange", _tramp_on_vehicle_siren_state_change),
    ("onVehicleSpawn", _tramp_on_vehicle_spawn),
    ("onVehicleStreamIn", _tramp_on_vehicle_stream_in),
    ("onVehicleStreamOut", _tramp_on_vehicle_stream_out),
]


on_actor_stream_in = event.decorator("onActorStreamIn")
on_actor_stream_out = event.decorator("onActorStreamOut")
on_client_check_response = event.decorator("onClientCheckResponse")
on_console_text = event.decorator("onConsoleText")
on_dialog_response = event.decorator("onDialogResponse")
on_enter_exit_mod_shop = event.decorator("onEnterExitModShop")
on_incoming_connection = event.decorator("onIncomingConnection")
on_npc_change_node = event.decorator("onNPCChangeNode")
on_npc_create = event.decorator("onNPCCreate")
on_npc_death = event.decorator("onNPCDeath")
on_npc_destroy = event.decorator("onNPCDestroy")
on_npc_finish_move = event.decorator("onNPCFinishMove")
on_npc_finish_move_path = event.decorator("onNPCFinishMovePath")
on_npc_finish_move_path_point = event.decorator("onNPCFinishMovePathPoint")
on_npc_finish_node = event.decorator("onNPCFinishNode")
on_npc_finish_node_point = event.decorator("onNPCFinishNodePoint")
on_npc_give_damage = event.decorator("onNPCGiveDamage")
on_npc_playback_end = event.decorator("onNPCPlaybackEnd")
on_npc_playback_start = event.decorator("onNPCPlaybackStart")
on_npc_respawn = event.decorator("onNPCRespawn")
on_npc_shot_missed = event.decorator("onNPCShotMissed")
on_npc_shot_npc = event.decorator("onNPCShotNPC")
on_npc_shot_object = event.decorator("onNPCShotObject")
on_npc_shot_player = event.decorator("onNPCShotPlayer")
on_npc_shot_player_object = event.decorator("onNPCShotPlayerObject")
on_npc_shot_vehicle = event.decorator("onNPCShotVehicle")
on_npc_spawn = event.decorator("onNPCSpawn")
on_npc_take_damage = event.decorator("onNPCTakeDamage")
on_npc_weapon_state_change = event.decorator("onNPCWeaponStateChange")
on_object_move = event.decorator("onObjectMove")
on_player_cancel_player_text_draw_selection = event.decorator("onPlayerCancelPlayerTextDrawSelection")
on_player_cancel_text_draw_selection = event.decorator("onPlayerCancelTextDrawSelection")
on_player_click_gang_zone = event.decorator("onPlayerClickGangZone")
on_player_click_map = event.decorator("onPlayerClickMap")
on_player_click_player = event.decorator("onPlayerClickPlayer")
on_player_click_player_text_draw = event.decorator("onPlayerClickPlayerTextDraw")
on_player_click_text_draw = event.decorator("onPlayerClickTextDraw")
on_player_command_text = event.decorator("onPlayerCommandText")
on_player_connect = event.decorator("onPlayerConnect")
on_player_death = event.decorator("onPlayerDeath")
on_player_disconnect = event.decorator("onPlayerDisconnect")
on_player_edit_attached_object = event.decorator("onPlayerEditAttachedObject")
on_player_edit_object = event.decorator("onPlayerEditObject")
on_player_edit_player_object = event.decorator("onPlayerEditPlayerObject")
on_player_enter_checkpoint = event.decorator("onPlayerEnterCheckpoint")
on_player_enter_gang_zone = event.decorator("onPlayerEnterGangZone")
on_player_enter_race_checkpoint = event.decorator("onPlayerEnterRaceCheckpoint")
on_player_enter_vehicle = event.decorator("onPlayerEnterVehicle")
on_player_exit_vehicle = event.decorator("onPlayerExitVehicle")
on_player_exited_menu = event.decorator("onPlayerExitedMenu")
on_player_finished_downloading = event.decorator("onPlayerFinishedDownloading")
on_player_give_damage = event.decorator("onPlayerGiveDamage")
on_player_give_damage_actor = event.decorator("onPlayerGiveDamageActor")
on_player_interior_change = event.decorator("onPlayerInteriorChange")
on_player_key_state_change = event.decorator("onPlayerKeyStateChange")
on_player_leave_checkpoint = event.decorator("onPlayerLeaveCheckpoint")
on_player_leave_gang_zone = event.decorator("onPlayerLeaveGangZone")
on_player_leave_race_checkpoint = event.decorator("onPlayerLeaveRaceCheckpoint")
on_player_object_move = event.decorator("onPlayerObjectMove")
on_player_pick_up_pickup = event.decorator("onPlayerPickUpPickup")
on_player_request_class = event.decorator("onPlayerRequestClass")
on_player_request_download = event.decorator("onPlayerRequestDownload")
on_player_request_spawn = event.decorator("onPlayerRequestSpawn")
on_player_select_object = event.decorator("onPlayerSelectObject")
on_player_select_player_object = event.decorator("onPlayerSelectPlayerObject")
on_player_selected_menu_row = event.decorator("onPlayerSelectedMenuRow")
on_player_shot_missed = event.decorator("onPlayerShotMissed")
on_player_shot_object = event.decorator("onPlayerShotObject")
on_player_shot_player = event.decorator("onPlayerShotPlayer")
on_player_shot_player_object = event.decorator("onPlayerShotPlayerObject")
on_player_shot_vehicle = event.decorator("onPlayerShotVehicle")
on_player_spawn = event.decorator("onPlayerSpawn")
on_player_state_change = event.decorator("onPlayerStateChange")
on_player_stream_in = event.decorator("onPlayerStreamIn")
on_player_stream_out = event.decorator("onPlayerStreamOut")
on_player_take_damage = event.decorator("onPlayerTakeDamage")
on_player_text = event.decorator("onPlayerText")
on_player_update = event.decorator("onPlayerUpdate")
on_rcon_login_attempt = event.decorator("onRconLoginAttempt")
on_tick = event.decorator("onTick")
on_trailer_update = event.decorator("onTrailerUpdate")
on_unoccupied_vehicle_update = event.decorator("onUnoccupiedVehicleUpdate")
on_vehicle_damage_status_update = event.decorator("onVehicleDamageStatusUpdate")
on_vehicle_death = event.decorator("onVehicleDeath")
on_vehicle_mod = event.decorator("onVehicleMod")
on_vehicle_paint_job = event.decorator("onVehiclePaintJob")
on_vehicle_respray = event.decorator("onVehicleRespray")
on_vehicle_siren_state_change = event.decorator("onVehicleSirenStateChange")
on_vehicle_spawn = event.decorator("onVehicleSpawn")
on_vehicle_stream_in = event.decorator("onVehicleStreamIn")
on_vehicle_stream_out = event.decorator("onVehicleStreamOut")


def register_all():
    lib = _capi.load()
    add = lib.Event_AddHandler
    add.restype = ctypes.c_bool
    add.argtypes = [ctypes.c_char_p, ctypes.c_int, ctypes.c_void_p]
    _trampolines.clear()
    for name, func in _TABLE:
        cb = _EVENT_CB(func)
        _trampolines.append(cb)
        add(name.encode(), _capi.EVENT_PRIORITY_DEFAULT, ctypes.cast(cb, ctypes.c_void_p))

__all__ = ["register_all", "on_actor_stream_in", "on_actor_stream_out", "on_client_check_response", "on_console_text", "on_dialog_response", "on_enter_exit_mod_shop", "on_incoming_connection", "on_npc_change_node", "on_npc_create", "on_npc_death", "on_npc_destroy", "on_npc_finish_move", "on_npc_finish_move_path", "on_npc_finish_move_path_point", "on_npc_finish_node", "on_npc_finish_node_point", "on_npc_give_damage", "on_npc_playback_end", "on_npc_playback_start", "on_npc_respawn", "on_npc_shot_missed", "on_npc_shot_npc", "on_npc_shot_object", "on_npc_shot_player", "on_npc_shot_player_object", "on_npc_shot_vehicle", "on_npc_spawn", "on_npc_take_damage", "on_npc_weapon_state_change", "on_object_move", "on_player_cancel_player_text_draw_selection", "on_player_cancel_text_draw_selection", "on_player_click_gang_zone", "on_player_click_map", "on_player_click_player", "on_player_click_player_text_draw", "on_player_click_text_draw", "on_player_command_text", "on_player_connect", "on_player_death", "on_player_disconnect", "on_player_edit_attached_object", "on_player_edit_object", "on_player_edit_player_object", "on_player_enter_checkpoint", "on_player_enter_gang_zone", "on_player_enter_race_checkpoint", "on_player_enter_vehicle", "on_player_exit_vehicle", "on_player_exited_menu", "on_player_finished_downloading", "on_player_give_damage", "on_player_give_damage_actor", "on_player_interior_change", "on_player_key_state_change", "on_player_leave_checkpoint", "on_player_leave_gang_zone", "on_player_leave_race_checkpoint", "on_player_object_move", "on_player_pick_up_pickup", "on_player_request_class", "on_player_request_download", "on_player_request_spawn", "on_player_select_object", "on_player_select_player_object", "on_player_selected_menu_row", "on_player_shot_missed", "on_player_shot_object", "on_player_shot_player", "on_player_shot_player_object", "on_player_shot_vehicle", "on_player_spawn", "on_player_state_change", "on_player_stream_in", "on_player_stream_out", "on_player_take_damage", "on_player_text", "on_player_update", "on_rcon_login_attempt", "on_tick", "on_trailer_update", "on_unoccupied_vehicle_update", "on_vehicle_damage_status_update", "on_vehicle_death", "on_vehicle_mod", "on_vehicle_paint_job", "on_vehicle_respray", "on_vehicle_siren_state_change", "on_vehicle_spawn", "on_vehicle_stream_in", "on_vehicle_stream_out"]

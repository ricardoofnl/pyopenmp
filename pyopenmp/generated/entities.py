from pyopenmp.generated import natives


class Actor:
    def __init__(self, ptr):
        self.ptr = ptr

    def apply_animation(self, name, library, delta, loop, lock_x, lock_y, freeze, time):
        return natives.actor_apply_animation(self.ptr, name, library, delta, loop, lock_x, lock_y, freeze, time)

    def clear_animations(self):
        return natives.actor_clear_animations(self.ptr)

    @classmethod
    def create(cls, model, x, y, z, rot):
        result = natives.actor_create(model, x, y, z, rot)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.actor_destroy(self.ptr)

    @classmethod
    def from_id(cls, actorid):
        result = natives.actor_from_id(actorid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_animation(self):
        return natives.actor_get_animation(self.ptr)

    def get_facing_angle(self):
        return natives.actor_get_facing_angle(self.ptr)

    def get_health(self):
        return natives.actor_get_health(self.ptr)

    def get_id(self):
        return natives.actor_get_id(self.ptr)

    def get_pos(self):
        return natives.actor_get_pos(self.ptr)

    def get_skin(self):
        return natives.actor_get_skin(self.ptr)

    def get_spawn_info(self):
        return natives.actor_get_spawn_info(self.ptr)

    def get_virtual_world(self):
        return natives.actor_get_virtual_world(self.ptr)

    def is_invulnerable(self):
        return natives.actor_is_invulnerable(self.ptr)

    def is_streamed_in_for(self, player):
        return natives.actor_is_streamed_in_for(self.ptr, player)

    def is_valid(self):
        return natives.actor_is_valid(self.ptr)

    def set_facing_angle(self, angle):
        return natives.actor_set_facing_angle(self.ptr, angle)

    def set_health(self, hp):
        return natives.actor_set_health(self.ptr, hp)

    def set_invulnerable(self, toggle):
        return natives.actor_set_invulnerable(self.ptr, toggle)

    def set_pos(self, x, y, z):
        return natives.actor_set_pos(self.ptr, x, y, z)

    def set_skin(self, skin):
        return natives.actor_set_skin(self.ptr, skin)

    def set_virtual_world(self, vw):
        return natives.actor_set_virtual_world(self.ptr, vw)


class Player:
    def __init__(self, ptr):
        self.ptr = ptr

    def allow_teleport(self, allow):
        return natives.player_allow_teleport(self.ptr, allow)

    def allow_weapons(self, allow):
        return natives.player_allow_weapons(self.ptr, allow)

    def apply_animation(self, animlib, animname, delta, loop, lock_x, lock_y, freeze, time, sync):
        return natives.player_apply_animation(self.ptr, animlib, animname, delta, loop, lock_x, lock_y, freeze, time, sync)

    def are_weapons_allowed(self):
        return natives.player_are_weapons_allowed(self.ptr)

    def attach_camera_to_object(self, object):
        return natives.player_attach_camera_to_object(self.ptr, object)

    def attach_camera_to_player_object(self, object):
        return natives.player_attach_camera_to_player_object(self.ptr, object)

    def ban(self):
        return natives.player_ban(self.ptr)

    def ban_ex(self, reason):
        return natives.player_ban_ex(self.ptr, reason)

    def cancel_select_text_draw(self):
        return natives.player_cancel_select_text_draw(self.ptr)

    def clear_animations(self, sync_type):
        return natives.player_clear_animations(self.ptr, sync_type)

    def clear_world_bounds(self):
        return natives.player_clear_world_bounds(self.ptr)

    def create_explosion(self, x, y, z, type, radius):
        return natives.player_create_explosion(self.ptr, x, y, z, type, radius)

    def disable_remote_vehicle_collisions(self, disable):
        return natives.player_disable_remote_vehicle_collisions(self.ptr, disable)

    def edit_attached_object(self, index):
        return natives.player_edit_attached_object(self.ptr, index)

    def enable_camera_target(self, enable):
        return natives.player_enable_camera_target(self.ptr, enable)

    def enable_stunt_bonus(self, enable):
        return natives.player_enable_stunt_bonus(self.ptr, enable)

    def force_class_selection(self):
        return natives.player_force_class_selection(self.ptr)

    @classmethod
    def from_id(cls, playerid):
        result = natives.player_from_id(playerid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def gpci(self):
        return natives.player_gpci(self.ptr)

    def get_animation_flags(self):
        return natives.player_get_animation_flags(self.ptr)

    def get_animation_index(self):
        return natives.player_get_animation_index(self.ptr)

    @classmethod
    def get_animation_name(cls, index):
        return natives.player_get_animation_name(index)

    def get_armor(self):
        return natives.player_get_armor(self.ptr)

    def get_attached_object(self, index):
        return natives.player_get_attached_object(self.ptr, index)

    def get_buildings_removed(self):
        return natives.player_get_buildings_removed(self.ptr)

    def get_camera_aspect_ratio(self):
        return natives.player_get_camera_aspect_ratio(self.ptr)

    def get_camera_front_vector(self):
        return natives.player_get_camera_front_vector(self.ptr)

    def get_camera_mode(self):
        return natives.player_get_camera_mode(self.ptr)

    def get_camera_pos(self):
        return natives.player_get_camera_pos(self.ptr)

    def get_camera_target_actor(self):
        return natives.player_get_camera_target_actor(self.ptr)

    def get_camera_target_object(self):
        return natives.player_get_camera_target_object(self.ptr)

    def get_camera_target_player(self):
        return natives.player_get_camera_target_player(self.ptr)

    def get_camera_target_player_object(self):
        return natives.player_get_camera_target_player_object(self.ptr)

    def get_camera_target_vehicle(self):
        return natives.player_get_camera_target_vehicle(self.ptr)

    def get_camera_zoom(self):
        return natives.player_get_camera_zoom(self.ptr)

    def get_color(self):
        return natives.player_get_color(self.ptr)

    def get_custom_skin(self):
        return natives.player_get_custom_skin(self.ptr)

    def get_default_color(self):
        return natives.player_get_default_color(self.ptr)

    def get_dialog(self):
        return natives.player_get_dialog(self.ptr)

    def get_dialog_data(self):
        return natives.player_get_dialog_data(self.ptr)

    def get_distance_from_point(self, x, y, z):
        return natives.player_get_distance_from_point(self.ptr, x, y, z)

    def get_drunk_level(self):
        return natives.player_get_drunk_level(self.ptr)

    def get_facing_angle(self):
        return natives.player_get_facing_angle(self.ptr)

    def get_fighting_style(self):
        return natives.player_get_fighting_style(self.ptr)

    def get_game_text(self, style):
        return natives.player_get_game_text(self.ptr, style)

    def get_ghost_mode(self):
        return natives.player_get_ghost_mode(self.ptr)

    def get_gravity(self):
        return natives.player_get_gravity(self.ptr)

    def get_health(self):
        return natives.player_get_health(self.ptr)

    def get_hydra_reactor_angle(self):
        return natives.player_get_hydra_reactor_angle(self.ptr)

    def get_id(self):
        return natives.player_get_id(self.ptr)

    def get_interior(self):
        return natives.player_get_interior(self.ptr)

    def get_ip(self):
        return natives.player_get_ip(self.ptr)

    def get_keys(self):
        return natives.player_get_keys(self.ptr)

    def get_landing_gear_state(self):
        return natives.player_get_landing_gear_state(self.ptr)

    def get_last_shot_vectors(self):
        return natives.player_get_last_shot_vectors(self.ptr)

    def get_marker_for_player(self, other):
        return natives.player_get_marker_for_player(self.ptr, other)

    def get_menu(self):
        return natives.player_get_menu(self.ptr)

    def get_money(self):
        return natives.player_get_money(self.ptr)

    def get_name(self):
        return natives.player_get_name(self.ptr)

    def get_network_stats(self):
        return natives.player_get_network_stats(self.ptr)

    def get_ping(self):
        return natives.player_get_ping(self.ptr)

    def get_player_ammo(self):
        return natives.player_get_player_ammo(self.ptr)

    def get_player_spectate_id(self):
        return natives.player_get_player_spectate_id(self.ptr)

    def get_pos(self):
        return natives.player_get_pos(self.ptr)

    def get_raw_ip(self):
        return natives.player_get_raw_ip(self.ptr)

    def get_rotation_quat(self):
        return natives.player_get_rotation_quat(self.ptr)

    def get_score(self):
        return natives.player_get_score(self.ptr)

    def get_siren_state(self):
        return natives.player_get_siren_state(self.ptr)

    def get_skill_level(self, skill):
        return natives.player_get_skill_level(self.ptr, skill)

    def get_skin(self):
        return natives.player_get_skin(self.ptr)

    def get_spawn_info(self):
        return natives.player_get_spawn_info(self.ptr)

    def get_special_action(self):
        return natives.player_get_special_action(self.ptr)

    def get_spectate_type(self):
        return natives.player_get_spectate_type(self.ptr)

    def get_state(self):
        return natives.player_get_state(self.ptr)

    def get_surfing_object(self):
        return natives.player_get_surfing_object(self.ptr)

    def get_surfing_offsets(self):
        return natives.player_get_surfing_offsets(self.ptr)

    def get_surfing_player_object(self):
        return natives.player_get_surfing_player_object(self.ptr)

    def get_surfing_vehicle(self):
        return natives.player_get_surfing_vehicle(self.ptr)

    def get_target_actor(self):
        return natives.player_get_target_actor(self.ptr)

    def get_target_player(self):
        return natives.player_get_target_player(self.ptr)

    def get_team(self):
        return natives.player_get_team(self.ptr)

    def get_time(self):
        return natives.player_get_time(self.ptr)

    def get_train_speed(self):
        return natives.player_get_train_speed(self.ptr)

    def get_vehicle_id(self):
        return natives.player_get_vehicle_id(self.ptr)

    def get_vehicle_seat(self):
        return natives.player_get_vehicle_seat(self.ptr)

    def get_velocity(self):
        return natives.player_get_velocity(self.ptr)

    def get_version(self):
        return natives.player_get_version(self.ptr)

    def get_virtual_world(self):
        return natives.player_get_virtual_world(self.ptr)

    def get_wanted_level(self):
        return natives.player_get_wanted_level(self.ptr)

    def get_weapon(self):
        return natives.player_get_weapon(self.ptr)

    def get_weapon_data(self, slot):
        return natives.player_get_weapon_data(self.ptr, slot)

    def get_weapon_state(self):
        return natives.player_get_weapon_state(self.ptr)

    def get_weather(self):
        return natives.player_get_weather(self.ptr)

    def get_world_bounds(self):
        return natives.player_get_world_bounds(self.ptr)

    def get_z_aim(self):
        return natives.player_get_z_aim(self.ptr)

    def give_money(self, amount):
        return natives.player_give_money(self.ptr, amount)

    def give_weapon(self, weapon, ammo):
        return natives.player_give_weapon(self.ptr, weapon, ammo)

    def has_clock(self):
        return natives.player_has_clock(self.ptr)

    def has_game_text(self, style):
        return natives.player_has_game_text(self.ptr, style)

    def hide_game_text(self, style):
        return natives.player_hide_game_text(self.ptr, style)

    def interpolate_camera_look_at(self, from_x, from_y, from_z, to_x, to_y, to_z, time, cut):
        return natives.player_interpolate_camera_look_at(self.ptr, from_x, from_y, from_z, to_x, to_y, to_z, time, cut)

    def interpolate_camera_pos(self, from_x, from_y, from_z, to_x, to_y, to_z, time, cut):
        return natives.player_interpolate_camera_pos(self.ptr, from_x, from_y, from_z, to_x, to_y, to_z, time, cut)

    def is_admin(self):
        return natives.player_is_admin(self.ptr)

    def is_camera_target_enabled(self):
        return natives.player_is_camera_target_enabled(self.ptr)

    def is_controllable(self):
        return natives.player_is_controllable(self.ptr)

    def is_cuffed(self):
        return natives.player_is_cuffed(self.ptr)

    def is_in_any_vehicle(self):
        return natives.player_is_in_any_vehicle(self.ptr)

    def is_in_drive_by_mode(self):
        return natives.player_is_in_drive_by_mode(self.ptr)

    def is_in_mod_shop(self):
        return natives.player_is_in_mod_shop(self.ptr)

    def is_in_range_of_point(self, range, x, y, z):
        return natives.player_is_in_range_of_point(self.ptr, range, x, y, z)

    def is_in_vehicle(self, target_vehicle):
        return natives.player_is_in_vehicle(self.ptr, target_vehicle)

    def is_npc(self):
        return natives.player_is_npc(self.ptr)

    def is_player_attached_object_slot_used(self, index):
        return natives.player_is_player_attached_object_slot_used(self.ptr, index)

    def is_player_using_official_client(self):
        return natives.player_is_player_using_official_client(self.ptr)

    def is_spawned(self):
        return natives.player_is_spawned(self.ptr)

    def is_streamed_in(self, other):
        return natives.player_is_streamed_in(self.ptr, other)

    def is_teleport_allowed(self):
        return natives.player_is_teleport_allowed(self.ptr)

    def is_using_omp(self):
        return natives.player_is_using_omp(self.ptr)

    def is_widescreen_toggled(self):
        return natives.player_is_widescreen_toggled(self.ptr)

    def kick(self):
        return natives.player_kick(self.ptr)

    def net_stats_bytes_received(self):
        return natives.player_net_stats_bytes_received(self.ptr)

    def net_stats_bytes_sent(self):
        return natives.player_net_stats_bytes_sent(self.ptr)

    def net_stats_connection_status(self):
        return natives.player_net_stats_connection_status(self.ptr)

    def net_stats_get_connected_time(self):
        return natives.player_net_stats_get_connected_time(self.ptr)

    def net_stats_get_ip_port(self):
        return natives.player_net_stats_get_ip_port(self.ptr)

    def net_stats_messages_received(self):
        return natives.player_net_stats_messages_received(self.ptr)

    def net_stats_messages_recv_per_second(self):
        return natives.player_net_stats_messages_recv_per_second(self.ptr)

    def net_stats_messages_sent(self):
        return natives.player_net_stats_messages_sent(self.ptr)

    def net_stats_packet_loss_percent(self):
        return natives.player_net_stats_packet_loss_percent(self.ptr)

    def play_audio_stream(self, url, x, y, z, distance, use_pos):
        return natives.player_play_audio_stream(self.ptr, url, x, y, z, distance, use_pos)

    def play_crime_report(self, suspect, crime):
        return natives.player_play_crime_report(self.ptr, suspect, crime)

    def play_game_sound(self, sound, x, y, z):
        return natives.player_play_game_sound(self.ptr, sound, x, y, z)

    def put_in_vehicle(self, vehicle, seat):
        return natives.player_put_in_vehicle(self.ptr, vehicle, seat)

    def remove_attached_object(self, index):
        return natives.player_remove_attached_object(self.ptr, index)

    def remove_building(self, model, x, y, z, radius):
        return natives.player_remove_building(self.ptr, model, x, y, z, radius)

    def remove_from_vehicle(self, force):
        return natives.player_remove_from_vehicle(self.ptr, force)

    def remove_map_icon(self, icon):
        return natives.player_remove_map_icon(self.ptr, icon)

    def remove_weapon(self, weapon):
        return natives.player_remove_weapon(self.ptr, weapon)

    def reset_money(self):
        return natives.player_reset_money(self.ptr)

    def reset_weapons(self):
        return natives.player_reset_weapons(self.ptr)

    def select_text_draw(self, hover_colour):
        return natives.player_select_text_draw(self.ptr, hover_colour)

    def send_client_check(self, action_type, address, offset, count):
        return natives.player_send_client_check(self.ptr, action_type, address, offset, count)

    def send_client_message(self, color, text):
        return natives.player_send_client_message(self.ptr, color, text)

    def send_death_message(self, killer, killee, weapon):
        return natives.player_send_death_message(self.ptr, killer, killee, weapon)

    def send_message_to_player(self, sender, message):
        return natives.player_send_message_to_player(self.ptr, sender, message)

    def set_admin(self, set):
        return natives.player_set_admin(self.ptr, set)

    def set_ammo(self, id, ammo):
        return natives.player_set_ammo(self.ptr, id, ammo)

    def set_armed_weapon(self, weapon):
        return natives.player_set_armed_weapon(self.ptr, weapon)

    def set_armor(self, armor):
        return natives.player_set_armor(self.ptr, armor)

    def set_attached_object(self, index, modelid, bone, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, scale_x, scale_y, scale_z, materialcolor1, materialcolor2):
        return natives.player_set_attached_object(self.ptr, index, modelid, bone, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, scale_x, scale_y, scale_z, materialcolor1, materialcolor2)

    def set_camera_behind(self):
        return natives.player_set_camera_behind(self.ptr)

    def set_camera_look_at(self, x, y, z, cut_type):
        return natives.player_set_camera_look_at(self.ptr, x, y, z, cut_type)

    def set_camera_pos(self, x, y, z):
        return natives.player_set_camera_pos(self.ptr, x, y, z)

    def set_chat_bubble(self, text, color, drawdistance, expiretime):
        return natives.player_set_chat_bubble(self.ptr, text, color, drawdistance, expiretime)

    def set_color(self, color):
        return natives.player_set_color(self.ptr, color)

    def set_drunk_level(self, level):
        return natives.player_set_drunk_level(self.ptr, level)

    def set_facing_angle(self, angle):
        return natives.player_set_facing_angle(self.ptr, angle)

    def set_fighting_style(self, style):
        return natives.player_set_fighting_style(self.ptr, style)

    def set_gravity(self, gravity):
        return natives.player_set_gravity(self.ptr, gravity)

    def set_health(self, health):
        return natives.player_set_health(self.ptr, health)

    def set_interior(self, interior):
        return natives.player_set_interior(self.ptr, interior)

    def set_map_icon(self, icon_id, x, y, z, type, color, style):
        return natives.player_set_map_icon(self.ptr, icon_id, x, y, z, type, color, style)

    def set_marker_for_player(self, other, color):
        return natives.player_set_marker_for_player(self.ptr, other, color)

    def set_name(self, name):
        return natives.player_set_name(self.ptr, name)

    def set_pos(self, x, y, z):
        return natives.player_set_pos(self.ptr, x, y, z)

    def set_pos_find_z(self, x, y, z):
        return natives.player_set_pos_find_z(self.ptr, x, y, z)

    def set_score(self, score):
        return natives.player_set_score(self.ptr, score)

    def set_shop_name(self, name):
        return natives.player_set_shop_name(self.ptr, name)

    def set_skill_level(self, weapon, level):
        return natives.player_set_skill_level(self.ptr, weapon, level)

    def set_skin(self, skin):
        return natives.player_set_skin(self.ptr, skin)

    def set_spawn_info(self, team, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3):
        return natives.player_set_spawn_info(self.ptr, team, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3)

    def set_special_action(self, action):
        return natives.player_set_special_action(self.ptr, action)

    def set_team(self, team):
        return natives.player_set_team(self.ptr, team)

    def set_time(self, hour, minute):
        return natives.player_set_time(self.ptr, hour, minute)

    def set_velocity(self, x, y, z):
        return natives.player_set_velocity(self.ptr, x, y, z)

    def set_virtual_world(self, vw):
        return natives.player_set_virtual_world(self.ptr, vw)

    def set_wanted_level(self, level):
        return natives.player_set_wanted_level(self.ptr, level)

    def set_weather(self, weather):
        return natives.player_set_weather(self.ptr, weather)

    def set_world_bounds(self, x_max, x_min, y_max, y_min):
        return natives.player_set_world_bounds(self.ptr, x_max, x_min, y_max, y_min)

    def show_game_text(self, text, time, style):
        return natives.player_show_game_text(self.ptr, text, time, style)

    def show_name_tag_for_player(self, other, enable):
        return natives.player_show_name_tag_for_player(self.ptr, other, enable)

    def spawn(self):
        return natives.player_spawn(self.ptr)

    def spectate_player(self, target, mode):
        return natives.player_spectate_player(self.ptr, target, mode)

    def spectate_vehicle(self, target, mode):
        return natives.player_spectate_vehicle(self.ptr, target, mode)

    def stop_audio_stream(self):
        return natives.player_stop_audio_stream(self.ptr)

    def toggle_clock(self, enable):
        return natives.player_toggle_clock(self.ptr, enable)

    def toggle_controllable(self, enable):
        return natives.player_toggle_controllable(self.ptr, enable)

    def toggle_ghost_mode(self, toggle):
        return natives.player_toggle_ghost_mode(self.ptr, toggle)

    def toggle_spectating(self, enable):
        return natives.player_toggle_spectating(self.ptr, enable)

    def toggle_widescreen(self, enable):
        return natives.player_toggle_widescreen(self.ptr, enable)


class Vehicle:
    def __init__(self, ptr):
        self.ptr = ptr

    def add_component(self, componentid):
        return natives.vehicle_add_component(self.ptr, componentid)

    @classmethod
    def add_static(cls, modelid, x, y, z, angle, color1, color2):
        return natives.vehicle_add_static(modelid, x, y, z, angle, color1, color2)

    @classmethod
    def add_static_ex(cls, modelid, x, y, z, angle, color1, color2, respawn_delay, add_siren):
        return natives.vehicle_add_static_ex(modelid, x, y, z, angle, color1, color2, respawn_delay, add_siren)

    def attach_trailer(self, vehicle):
        return natives.vehicle_attach_trailer(self.ptr, vehicle)

    @classmethod
    def can_have_component(cls, modelid, componentid):
        return natives.vehicle_can_have_component(modelid, componentid)

    def change_color(self, color1, color2):
        return natives.vehicle_change_color(self.ptr, color1, color2)

    def change_paintjob(self, paintjobid):
        return natives.vehicle_change_paintjob(self.ptr, paintjobid)

    @classmethod
    def color_index_to_color(cls, color_index, alpha):
        return natives.vehicle_color_index_to_color(color_index, alpha)

    def count_occupants(self):
        return natives.vehicle_count_occupants(self.ptr)

    @classmethod
    def create(cls, modelid, x, y, z, rotation, color1, color2, respawn_delay, add_siren):
        result = natives.vehicle_create(modelid, x, y, z, rotation, color1, color2, respawn_delay, add_siren)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.vehicle_destroy(self.ptr)

    def detach_trailer(self):
        return natives.vehicle_detach_trailer(self.ptr)

    @classmethod
    def enable_friendly_fire(cls):
        return natives.vehicle_enable_friendly_fire()

    @classmethod
    def from_id(cls, vehicleid):
        result = natives.vehicle_from_id(vehicleid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_cab(self):
        return natives.vehicle_get_cab(self.ptr)

    def get_color(self):
        return natives.vehicle_get_color(self.ptr)

    def get_component_in_slot(self, slot):
        return natives.vehicle_get_component_in_slot(self.ptr, slot)

    @classmethod
    def get_component_type(cls, componentid):
        return natives.vehicle_get_component_type(componentid)

    def get_damage_status(self):
        return natives.vehicle_get_damage_status(self.ptr)

    def get_distance_from_point(self, x, y, z):
        return natives.vehicle_get_distance_from_point(self.ptr, x, y, z)

    def get_driver(self):
        return natives.vehicle_get_driver(self.ptr)

    def get_health(self):
        return natives.vehicle_get_health(self.ptr)

    def get_hydra_reactor_angle(self):
        return natives.vehicle_get_hydra_reactor_angle(self.ptr)

    def get_id(self):
        return natives.vehicle_get_id(self.ptr)

    def get_interior(self):
        return natives.vehicle_get_interior(self.ptr)

    def get_landing_gear_state(self):
        return natives.vehicle_get_landing_gear_state(self.ptr)

    def get_last_driver(self):
        return natives.vehicle_get_last_driver(self.ptr)

    def get_matrix(self):
        return natives.vehicle_get_matrix(self.ptr)

    @classmethod
    def get_max_passenger_seats(cls, modelid):
        return natives.vehicle_get_max_passenger_seats(modelid)

    def get_model(self):
        return natives.vehicle_get_model(self.ptr)

    @classmethod
    def get_model_count(cls, modelid):
        return natives.vehicle_get_model_count(modelid)

    @classmethod
    def get_model_info(cls, vehiclemodel, infotype):
        return natives.vehicle_get_model_info(vehiclemodel, infotype)

    @classmethod
    def get_models_used(cls):
        return natives.vehicle_get_models_used()

    def get_number_plate(self):
        return natives.vehicle_get_number_plate(self.ptr)

    def get_occupant(self, seat):
        return natives.vehicle_get_occupant(self.ptr, seat)

    def get_occupied_tick(self):
        return natives.vehicle_get_occupied_tick(self.ptr)

    def get_paintjob(self):
        return natives.vehicle_get_paintjob(self.ptr)

    def get_params_car_doors(self):
        return natives.vehicle_get_params_car_doors(self.ptr)

    def get_params_car_windows(self):
        return natives.vehicle_get_params_car_windows(self.ptr)

    def get_params_ex(self):
        return natives.vehicle_get_params_ex(self.ptr)

    def get_params_siren_state(self):
        return natives.vehicle_get_params_siren_state(self.ptr)

    def get_pos(self):
        return natives.vehicle_get_pos(self.ptr)

    @classmethod
    def get_random_color_pair(cls, modelid):
        return natives.vehicle_get_random_color_pair(modelid)

    def get_respawn_delay(self):
        return natives.vehicle_get_respawn_delay(self.ptr)

    def get_respawn_tick(self):
        return natives.vehicle_get_respawn_tick(self.ptr)

    def get_rotation_quat(self):
        return natives.vehicle_get_rotation_quat(self.ptr)

    def get_siren_state(self):
        return natives.vehicle_get_siren_state(self.ptr)

    def get_spawn_info(self):
        return natives.vehicle_get_spawn_info(self.ptr)

    def get_tower(self):
        return natives.vehicle_get_tower(self.ptr)

    def get_trailer(self):
        return natives.vehicle_get_trailer(self.ptr)

    def get_train_speed(self):
        return natives.vehicle_get_train_speed(self.ptr)

    def get_velocity(self):
        return natives.vehicle_get_velocity(self.ptr)

    def get_virtual_world(self):
        return natives.vehicle_get_virtual_world(self.ptr)

    def get_z_angle(self):
        return natives.vehicle_get_z_angle(self.ptr)

    def has_been_occupied(self):
        return natives.vehicle_has_been_occupied(self.ptr)

    def is_dead(self):
        return natives.vehicle_is_dead(self.ptr)

    def is_occupied(self):
        return natives.vehicle_is_occupied(self.ptr)

    def is_siren_enabled(self):
        return natives.vehicle_is_siren_enabled(self.ptr)

    def is_streamed_in(self, player):
        return natives.vehicle_is_streamed_in(self.ptr, player)

    def is_trailer_attached(self):
        return natives.vehicle_is_trailer_attached(self.ptr)

    def is_valid(self):
        return natives.vehicle_is_valid(self.ptr)

    def link_to_interior(self, interiorid):
        return natives.vehicle_link_to_interior(self.ptr, interiorid)

    def remove_component(self, componentid):
        return natives.vehicle_remove_component(self.ptr, componentid)

    def repair(self):
        return natives.vehicle_repair(self.ptr)

    def set_angular_velocity(self, x, y, z):
        return natives.vehicle_set_angular_velocity(self.ptr, x, y, z)

    def set_health(self, health):
        return natives.vehicle_set_health(self.ptr, health)

    def set_number_plate(self, number_plate):
        return natives.vehicle_set_number_plate(self.ptr, number_plate)

    def set_params_car_doors(self, front_left, front_right, rear_left, rear_right):
        return natives.vehicle_set_params_car_doors(self.ptr, front_left, front_right, rear_left, rear_right)

    def set_params_car_windows(self, front_left, front_right, rear_left, rear_right):
        return natives.vehicle_set_params_car_windows(self.ptr, front_left, front_right, rear_left, rear_right)

    def set_params_ex(self, engine, lights, alarm, doors, bonnet, boot, objective):
        return natives.vehicle_set_params_ex(self.ptr, engine, lights, alarm, doors, bonnet, boot, objective)

    def set_params_for_player(self, player, objective, doors):
        return natives.vehicle_set_params_for_player(self.ptr, player, objective, doors)

    def set_params_siren_state(self, siren_state):
        return natives.vehicle_set_params_siren_state(self.ptr, siren_state)

    def set_pos(self, x, y, z):
        return natives.vehicle_set_pos(self.ptr, x, y, z)

    def set_respawn_delay(self, respawn_delay):
        return natives.vehicle_set_respawn_delay(self.ptr, respawn_delay)

    def set_spawn_info(self, modelid, x, y, z, rotation, color1, color2, respawn_time, interior):
        return natives.vehicle_set_spawn_info(self.ptr, modelid, x, y, z, rotation, color1, color2, respawn_time, interior)

    def set_to_respawn(self):
        return natives.vehicle_set_to_respawn(self.ptr)

    def set_velocity(self, x, y, z):
        return natives.vehicle_set_velocity(self.ptr, x, y, z)

    def set_virtual_world(self, virtual_world):
        return natives.vehicle_set_virtual_world(self.ptr, virtual_world)

    def set_z_angle(self, angle):
        return natives.vehicle_set_z_angle(self.ptr, angle)

    def toggle_siren_enabled(self, status):
        return natives.vehicle_toggle_siren_enabled(self.ptr, status)

    def update_damage_status(self, panels, doors, lights, tires):
        return natives.vehicle_update_damage_status(self.ptr, panels, doors, lights, tires)

    @classmethod
    def use_manual_engine_and_lights(cls):
        return natives.vehicle_use_manual_engine_and_lights()


class Object:
    def __init__(self, ptr):
        self.ptr = ptr

    def attach_to_object(self, obj_attached_to, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, sync_rotation):
        return natives.object_attach_to_object(self.ptr, obj_attached_to, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z, sync_rotation)

    def attach_to_player(self, player, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z):
        return natives.object_attach_to_player(self.ptr, player, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)

    def attach_to_vehicle(self, vehicle, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z):
        return natives.object_attach_to_vehicle(self.ptr, vehicle, offset_x, offset_y, offset_z, rotation_x, rotation_y, rotation_z)

    def begin_editing(self, object):
        return natives.object_begin_editing(self.ptr, object)

    def begin_selecting(self):
        return natives.object_begin_selecting(self.ptr)

    @classmethod
    def create(cls, modelid, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance):
        result = natives.object_create(modelid, x, y, z, rotation_x, rotation_y, rotation_z, draw_distance)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.object_destroy(self.ptr)

    def end_editing(self):
        return natives.object_end_editing(self.ptr)

    @classmethod
    def from_id(cls, objectid):
        result = natives.object_from_id(objectid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_attached_data(self):
        return natives.object_get_attached_data(self.ptr)

    def get_attached_offset(self):
        return natives.object_get_attached_offset(self.ptr)

    def get_draw_distance(self):
        return natives.object_get_draw_distance(self.ptr)

    def get_id(self):
        return natives.object_get_id(self.ptr)

    def get_material(self, material_index):
        return natives.object_get_material(self.ptr, material_index)

    def get_material_text(self, material_index):
        return natives.object_get_material_text(self.ptr, material_index)

    def get_model(self):
        return natives.object_get_model(self.ptr)

    def get_move_speed(self):
        return natives.object_get_move_speed(self.ptr)

    def get_moving_target_pos(self):
        return natives.object_get_moving_target_pos(self.ptr)

    def get_moving_target_rot(self):
        return natives.object_get_moving_target_rot(self.ptr)

    def get_pos(self):
        return natives.object_get_pos(self.ptr)

    def get_rot(self):
        return natives.object_get_rot(self.ptr)

    def get_sync_rotation(self):
        return natives.object_get_sync_rotation(self.ptr)

    def get_type(self, objectid):
        return natives.object_get_type(self.ptr, objectid)

    def is_material_slot_used(self, material_index):
        return natives.object_is_material_slot_used(self.ptr, material_index)

    def is_moving(self):
        return natives.object_is_moving(self.ptr)

    def is_object_no_camera_collision(self):
        return natives.object_is_object_no_camera_collision(self.ptr)

    def is_valid(self):
        return natives.object_is_valid(self.ptr)

    def move(self, x, y, z, speed, rotation_x, rotation_y, rotation_z):
        return natives.object_move(self.ptr, x, y, z, speed, rotation_x, rotation_y, rotation_z)

    @classmethod
    def set_default_camera_collision(cls, disable):
        return natives.object_set_default_camera_collision(disable)

    def set_material(self, material_index, model_id, texture_library, texture_name, material_color):
        return natives.object_set_material(self.ptr, material_index, model_id, texture_library, texture_name, material_color)

    def set_material_text(self, text, material_index, material_size, fontface, fontsize, bold, font_color, background_color, textalignment):
        return natives.object_set_material_text(self.ptr, text, material_index, material_size, fontface, fontsize, bold, font_color, background_color, textalignment)

    def set_no_camera_collision(self):
        return natives.object_set_no_camera_collision(self.ptr)

    def set_pos(self, x, y, z):
        return natives.object_set_pos(self.ptr, x, y, z)

    def set_rot(self, rotation_x, rotation_y, rotation_z):
        return natives.object_set_rot(self.ptr, rotation_x, rotation_y, rotation_z)

    def stop(self):
        return natives.object_stop(self.ptr)


class Pickup:
    def __init__(self, ptr):
        self.ptr = ptr

    @classmethod
    def add_static(cls, model, type, x, y, z, virtual_world):
        return natives.pickup_add_static(model, type, x, y, z, virtual_world)

    @classmethod
    def create(cls, model, type, x, y, z, virtual_world):
        result = natives.pickup_create(model, type, x, y, z, virtual_world)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.pickup_destroy(self.ptr)

    @classmethod
    def from_id(cls, pickupid):
        result = natives.pickup_from_id(pickupid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_id(self):
        return natives.pickup_get_id(self.ptr)

    def get_model(self):
        return natives.pickup_get_model(self.ptr)

    def get_pos(self):
        return natives.pickup_get_pos(self.ptr)

    def get_type(self):
        return natives.pickup_get_type(self.ptr)

    def get_virtual_world(self):
        return natives.pickup_get_virtual_world(self.ptr)

    def hide_for_player(self, pickup):
        return natives.pickup_hide_for_player(self.ptr, pickup)

    def is_hidden_for_player(self, pickup):
        return natives.pickup_is_hidden_for_player(self.ptr, pickup)

    def is_streamed_in(self, pickup):
        return natives.pickup_is_streamed_in(self.ptr, pickup)

    def is_valid(self):
        return natives.pickup_is_valid(self.ptr)

    def set_model(self, model, update):
        return natives.pickup_set_model(self.ptr, model, update)

    def set_pos(self, x, y, z, update):
        return natives.pickup_set_pos(self.ptr, x, y, z, update)

    def set_type(self, type, update):
        return natives.pickup_set_type(self.ptr, type, update)

    def set_virtual_world(self, virtualworld):
        return natives.pickup_set_virtual_world(self.ptr, virtualworld)

    def show_for_player(self, pickup):
        return natives.pickup_show_for_player(self.ptr, pickup)


class GangZone:
    def __init__(self, ptr):
        self.ptr = ptr

    @classmethod
    def create(cls, minx, miny, maxx, maxy):
        result = natives.gang_zone_create(minx, miny, maxx, maxy)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.gang_zone_destroy(self.ptr)

    def flash_for_all(self, color):
        return natives.gang_zone_flash_for_all(self.ptr, color)

    def flash_for_player(self, gangzone, color):
        return natives.gang_zone_flash_for_player(self.ptr, gangzone, color)

    @classmethod
    def from_id(cls, gangzoneid):
        result = natives.gang_zone_from_id(gangzoneid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_color_for_player(self, gangzone):
        return natives.gang_zone_get_color_for_player(self.ptr, gangzone)

    def get_flash_color_for_player(self, gangzone):
        return natives.gang_zone_get_flash_color_for_player(self.ptr, gangzone)

    def get_id(self):
        return natives.gang_zone_get_id(self.ptr)

    def get_pos(self):
        return natives.gang_zone_get_pos(self.ptr)

    def hide_for_all(self):
        return natives.gang_zone_hide_for_all(self.ptr)

    def hide_for_player(self, gangzone):
        return natives.gang_zone_hide_for_player(self.ptr, gangzone)

    def is_flashing_for_player(self, gangzone):
        return natives.gang_zone_is_flashing_for_player(self.ptr, gangzone)

    def is_player_in(self, gangzone):
        return natives.gang_zone_is_player_in(self.ptr, gangzone)

    def is_valid(self):
        return natives.gang_zone_is_valid(self.ptr)

    def is_visible_for_player(self, gangzone):
        return natives.gang_zone_is_visible_for_player(self.ptr, gangzone)

    def show_for_all(self, color):
        return natives.gang_zone_show_for_all(self.ptr, color)

    def show_for_player(self, gangzone, color):
        return natives.gang_zone_show_for_player(self.ptr, gangzone, color)

    def stop_flash_for_all(self):
        return natives.gang_zone_stop_flash_for_all(self.ptr)

    def stop_flash_for_player(self, gangzone):
        return natives.gang_zone_stop_flash_for_player(self.ptr, gangzone)

    def use_check(self, enable):
        return natives.gang_zone_use_check(self.ptr, enable)


class Menu:
    def __init__(self, ptr):
        self.ptr = ptr

    def add_item(self, column, text):
        return natives.menu_add_item(self.ptr, column, text)

    @classmethod
    def create(cls, title, columns, x, y, column1_width, column2_width):
        result = natives.menu_create(title, columns, x, y, column1_width, column2_width)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.menu_destroy(self.ptr)

    def disable(self):
        return natives.menu_disable(self.ptr)

    def disable_row(self, row):
        return natives.menu_disable_row(self.ptr, row)

    @classmethod
    def from_id(cls, menuid):
        result = natives.menu_from_id(menuid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_column_header(self, column):
        return natives.menu_get_column_header(self.ptr, column)

    def get_column_width(self):
        return natives.menu_get_column_width(self.ptr)

    def get_columns(self):
        return natives.menu_get_columns(self.ptr)

    def get_id(self):
        return natives.menu_get_id(self.ptr)

    def get_item(self, column, row):
        return natives.menu_get_item(self.ptr, column, row)

    def get_items(self, column):
        return natives.menu_get_items(self.ptr, column)

    def get_pos(self):
        return natives.menu_get_pos(self.ptr)

    def hide_for_player(self, player):
        return natives.menu_hide_for_player(self.ptr, player)

    def is_disabled(self):
        return natives.menu_is_disabled(self.ptr)

    def is_row_disabled(self, row):
        return natives.menu_is_row_disabled(self.ptr, row)

    def is_valid(self):
        return natives.menu_is_valid(self.ptr)

    def set_column_header(self, column, header_title):
        return natives.menu_set_column_header(self.ptr, column, header_title)

    def show_for_player(self, player):
        return natives.menu_show_for_player(self.ptr, player)


class TextDraw:
    def __init__(self, ptr):
        self.ptr = ptr

    @classmethod
    def create(cls, x, y, text):
        result = natives.text_draw_create(x, y, text)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.text_draw_destroy(self.ptr)

    @classmethod
    def from_id(cls, textdrawid):
        result = natives.text_draw_from_id(textdrawid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_alignment(self):
        return natives.text_draw_get_alignment(self.ptr)

    def get_background_color(self):
        return natives.text_draw_get_background_color(self.ptr)

    def get_box_color(self):
        return natives.text_draw_get_box_color(self.ptr)

    def get_color(self):
        return natives.text_draw_get_color(self.ptr)

    def get_font(self):
        return natives.text_draw_get_font(self.ptr)

    def get_id(self):
        return natives.text_draw_get_id(self.ptr)

    def get_letter_size(self):
        return natives.text_draw_get_letter_size(self.ptr)

    def get_outline(self):
        return natives.text_draw_get_outline(self.ptr)

    def get_pos(self):
        return natives.text_draw_get_pos(self.ptr)

    def get_preview_model(self):
        return natives.text_draw_get_preview_model(self.ptr)

    def get_preview_rot(self):
        return natives.text_draw_get_preview_rot(self.ptr)

    def get_preview_veh_color(self):
        return natives.text_draw_get_preview_veh_color(self.ptr)

    def get_shadow(self):
        return natives.text_draw_get_shadow(self.ptr)

    def get_string(self):
        return natives.text_draw_get_string(self.ptr)

    def get_text_size(self):
        return natives.text_draw_get_text_size(self.ptr)

    def hide_for_all(self):
        return natives.text_draw_hide_for_all(self.ptr)

    def hide_for_player(self, textdraw):
        return natives.text_draw_hide_for_player(self.ptr, textdraw)

    def is_box(self):
        return natives.text_draw_is_box(self.ptr)

    def is_proportional(self):
        return natives.text_draw_is_proportional(self.ptr)

    def is_selectable(self):
        return natives.text_draw_is_selectable(self.ptr)

    def is_valid(self):
        return natives.text_draw_is_valid(self.ptr)

    def is_visible_for_player(self, textdraw):
        return natives.text_draw_is_visible_for_player(self.ptr, textdraw)

    def set_alignment(self, alignment):
        return natives.text_draw_set_alignment(self.ptr, alignment)

    def set_background_color(self, color):
        return natives.text_draw_set_background_color(self.ptr, color)

    def set_box_color(self, color):
        return natives.text_draw_set_box_color(self.ptr, color)

    def set_color(self, color):
        return natives.text_draw_set_color(self.ptr, color)

    def set_font(self, font):
        return natives.text_draw_set_font(self.ptr, font)

    def set_letter_size(self, size_x, size_y):
        return natives.text_draw_set_letter_size(self.ptr, size_x, size_y)

    def set_outline(self, size):
        return natives.text_draw_set_outline(self.ptr, size)

    def set_pos(self, x, y):
        return natives.text_draw_set_pos(self.ptr, x, y)

    def set_preview_model(self, model):
        return natives.text_draw_set_preview_model(self.ptr, model)

    def set_preview_rot(self, rotation_x, rotation_y, rotation_z, zoom):
        return natives.text_draw_set_preview_rot(self.ptr, rotation_x, rotation_y, rotation_z, zoom)

    def set_preview_veh_col(self, color1, color2):
        return natives.text_draw_set_preview_veh_col(self.ptr, color1, color2)

    def set_proportional(self, set):
        return natives.text_draw_set_proportional(self.ptr, set)

    def set_selectable(self, set):
        return natives.text_draw_set_selectable(self.ptr, set)

    def set_shadow(self, size):
        return natives.text_draw_set_shadow(self.ptr, size)

    def set_string(self, text):
        return natives.text_draw_set_string(self.ptr, text)

    def set_string_for_player(self, player, text):
        return natives.text_draw_set_string_for_player(self.ptr, player, text)

    def set_text_size(self, size_x, size_y):
        return natives.text_draw_set_text_size(self.ptr, size_x, size_y)

    def set_use_box(self, use):
        return natives.text_draw_set_use_box(self.ptr, use)

    def show_for_all(self):
        return natives.text_draw_show_for_all(self.ptr)

    def show_for_player(self, textdraw):
        return natives.text_draw_show_for_player(self.ptr, textdraw)


class TextLabel:
    def __init__(self, ptr):
        self.ptr = ptr

    def attach_to_player(self, player, offset_x, offset_y, offset_z):
        return natives.text_label_attach_to_player(self.ptr, player, offset_x, offset_y, offset_z)

    def attach_to_vehicle(self, vehicle, offset_x, offset_y, offset_z):
        return natives.text_label_attach_to_vehicle(self.ptr, vehicle, offset_x, offset_y, offset_z)

    @classmethod
    def create(cls, text, color, x, y, z, draw_distance, virtual_world, los):
        result = natives.text_label_create(text, color, x, y, z, draw_distance, virtual_world, los)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def destroy(self):
        return natives.text_label_destroy(self.ptr)

    @classmethod
    def from_id(cls, textlabelid):
        result = natives.text_label_from_id(textlabelid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_attached_data(self):
        return natives.text_label_get_attached_data(self.ptr)

    def get_color(self):
        return natives.text_label_get_color(self.ptr)

    def get_draw_distance(self):
        return natives.text_label_get_draw_distance(self.ptr)

    def get_id(self):
        return natives.text_label_get_id(self.ptr)

    def get_los(self):
        return natives.text_label_get_los(self.ptr)

    def get_pos(self):
        return natives.text_label_get_pos(self.ptr)

    def get_text(self):
        return natives.text_label_get_text(self.ptr)

    def get_virtual_world(self):
        return natives.text_label_get_virtual_world(self.ptr)

    def is_streamed_in(self, textlabel):
        return natives.text_label_is_streamed_in(self.ptr, textlabel)

    def is_valid(self):
        return natives.text_label_is_valid(self.ptr)

    def set_draw_distance(self, distance):
        return natives.text_label_set_draw_distance(self.ptr, distance)

    def set_los(self, status):
        return natives.text_label_set_los(self.ptr, status)

    def set_virtual_world(self, world):
        return natives.text_label_set_virtual_world(self.ptr, world)

    def update_text(self, color, text):
        return natives.text_label_update_text(self.ptr, color, text)


class Npc:
    def __init__(self, ptr):
        self.ptr = ptr

    @classmethod
    def add_point_to_path(cls, path_id, x, y, z, stop_range):
        return natives.npc_add_point_to_path(path_id, x, y, z, stop_range)

    def aim_at(self, x, y, z, shoot, shoot_delay, update_angle, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags):
        return natives.npc_aim_at(self.ptr, x, y, z, shoot, shoot_delay, update_angle, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags)

    def aim_at_player(self, at_player, shoot, shoot_delay, update_angle, offset_x, offset_y, offset_z, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags):
        return natives.npc_aim_at_player(self.ptr, at_player, shoot, shoot_delay, update_angle, offset_x, offset_y, offset_z, offset_from_x, offset_from_y, offset_from_z, check_in_between_flags)

    def apply_animation(self, animlib, animname, delta, loop, lock_x, lock_y, freeze, time):
        return natives.npc_apply_animation(self.ptr, animlib, animname, delta, loop, lock_x, lock_y, freeze, time)

    def change_node(self, node_id, link_id):
        return natives.npc_change_node(self.ptr, node_id, link_id)

    def clear_animations(self):
        return natives.npc_clear_animations(self.ptr)

    @classmethod
    def clear_path(cls, path_id):
        return natives.npc_clear_path(path_id)

    @classmethod
    def close_node(cls, node_id):
        return natives.npc_close_node(node_id)

    @classmethod
    def connect(cls, name, script):
        return natives.npc_connect(name, script)

    @classmethod
    def create(cls, name):
        result = natives.npc_create(name)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    @classmethod
    def create_path(cls):
        return natives.npc_create_path()

    def destroy(self):
        return natives.npc_destroy(self.ptr)

    @classmethod
    def destroy_all_path(cls):
        return natives.npc_destroy_all_path()

    @classmethod
    def destroy_path(cls, path_id):
        return natives.npc_destroy_path(path_id)

    def enable_infinite_ammo(self, enable):
        return natives.npc_enable_infinite_ammo(self.ptr, enable)

    def enable_reloading(self, enable):
        return natives.npc_enable_reloading(self.ptr, enable)

    def enter_vehicle(self, vehicle, seat_id, move_type):
        return natives.npc_enter_vehicle(self.ptr, vehicle, seat_id, move_type)

    def exit_vehicle(self):
        return natives.npc_exit_vehicle(self.ptr)

    @classmethod
    def from_id(cls, npcid):
        result = natives.npc_from_id(npcid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    @classmethod
    def get_all(cls, max_np_cs):
        return natives.npc_get_all(max_np_cs)

    def get_ammo(self):
        return natives.npc_get_ammo(self.ptr)

    def get_ammo_in_clip(self):
        return natives.npc_get_ammo_in_clip(self.ptr)

    def get_animation(self):
        return natives.npc_get_animation(self.ptr)

    def get_armour(self):
        return natives.npc_get_armour(self.ptr)

    def get_current_path_point_index(self):
        return natives.npc_get_current_path_point_index(self.ptr)

    def get_entering_vehicle(self):
        return natives.npc_get_entering_vehicle(self.ptr)

    def get_entering_vehicle_id(self):
        return natives.npc_get_entering_vehicle_id(self.ptr)

    def get_entering_vehicle_seat(self):
        return natives.npc_get_entering_vehicle_seat(self.ptr)

    def get_facing_angle(self):
        return natives.npc_get_facing_angle(self.ptr)

    def get_fighting_style(self):
        return natives.npc_get_fighting_style(self.ptr)

    def get_health(self):
        return natives.npc_get_health(self.ptr)

    def get_id(self):
        return natives.npc_get_id(self.ptr)

    def get_interior(self):
        return natives.npc_get_interior(self.ptr)

    def get_keys(self):
        return natives.npc_get_keys(self.ptr)

    @classmethod
    def get_node_info(cls, node_id):
        return natives.npc_get_node_info(node_id)

    @classmethod
    def get_node_point_count(cls, node_id):
        return natives.npc_get_node_point_count(node_id)

    @classmethod
    def get_node_point_position(cls, node_id):
        return natives.npc_get_node_point_position(node_id)

    @classmethod
    def get_node_type(cls, node_id):
        return natives.npc_get_node_type(node_id)

    @classmethod
    def get_path_count(cls):
        return natives.npc_get_path_count()

    @classmethod
    def get_path_point(cls, path_id, point_index):
        return natives.npc_get_path_point(path_id, point_index)

    @classmethod
    def get_path_point_count(cls, path_id):
        return natives.npc_get_path_point_count(path_id)

    def get_player(self):
        return natives.npc_get_player(self.ptr)

    def get_pos(self):
        return natives.npc_get_pos(self.ptr)

    @classmethod
    def get_record_count(cls):
        return natives.npc_get_record_count()

    def get_rot(self):
        return natives.npc_get_rot(self.ptr)

    def get_special_action(self):
        return natives.npc_get_special_action(self.ptr)

    def get_surfing_object(self):
        return natives.npc_get_surfing_object(self.ptr)

    def get_surfing_offset(self):
        return natives.npc_get_surfing_offset(self.ptr)

    def get_surfing_player_object(self):
        return natives.npc_get_surfing_player_object(self.ptr)

    def get_surfing_vehicle(self):
        return natives.npc_get_surfing_vehicle(self.ptr)

    def get_vehicle(self):
        return natives.npc_get_vehicle(self.ptr)

    def get_vehicle_gear_state(self):
        return natives.npc_get_vehicle_gear_state(self.ptr)

    def get_vehicle_health(self):
        return natives.npc_get_vehicle_health(self.ptr)

    def get_vehicle_hydra_thrusters(self):
        return natives.npc_get_vehicle_hydra_thrusters(self.ptr)

    def get_vehicle_id(self):
        return natives.npc_get_vehicle_id(self.ptr)

    def get_vehicle_seat(self):
        return natives.npc_get_vehicle_seat(self.ptr)

    def get_vehicle_train_speed(self):
        return natives.npc_get_vehicle_train_speed(self.ptr)

    def get_virtual_world(self):
        return natives.npc_get_virtual_world(self.ptr)

    def get_weapon(self):
        return natives.npc_get_weapon(self.ptr)

    def get_weapon_accuracy(self, weapon):
        return natives.npc_get_weapon_accuracy(self.ptr, weapon)

    def get_weapon_actual_clip_size(self, weapon):
        return natives.npc_get_weapon_actual_clip_size(self.ptr, weapon)

    def get_weapon_actual_reload_time(self, weapon):
        return natives.npc_get_weapon_actual_reload_time(self.ptr, weapon)

    def get_weapon_clip_size(self, weapon):
        return natives.npc_get_weapon_clip_size(self.ptr, weapon)

    def get_weapon_reload_time(self, weapon):
        return natives.npc_get_weapon_reload_time(self.ptr, weapon)

    def get_weapon_shoot_time(self, weapon):
        return natives.npc_get_weapon_shoot_time(self.ptr, weapon)

    def get_weapon_skill_level(self, skill):
        return natives.npc_get_weapon_skill_level(self.ptr, skill)

    def get_weapon_state(self):
        return natives.npc_get_weapon_state(self.ptr)

    @classmethod
    def has_path_point_in_range(cls, path_id, x, y, z, radius):
        return natives.npc_has_path_point_in_range(path_id, x, y, z, radius)

    def is_aiming(self):
        return natives.npc_is_aiming(self.ptr)

    def is_aiming_at_player(self, at_player):
        return natives.npc_is_aiming_at_player(self.ptr, at_player)

    def is_any_streamed_in(self):
        return natives.npc_is_any_streamed_in(self.ptr)

    def is_dead(self):
        return natives.npc_is_dead(self.ptr)

    def is_entering_vehicle(self):
        return natives.npc_is_entering_vehicle(self.ptr)

    def is_infinite_ammo_enabled(self):
        return natives.npc_is_infinite_ammo_enabled(self.ptr)

    def is_invulnerable(self):
        return natives.npc_is_invulnerable(self.ptr)

    def is_melee_attacking(self):
        return natives.npc_is_melee_attacking(self.ptr)

    def is_moving(self):
        return natives.npc_is_moving(self.ptr)

    @classmethod
    def is_node_open(cls, node_id):
        return natives.npc_is_node_open(node_id)

    def is_playback_paused(self):
        return natives.npc_is_playback_paused(self.ptr)

    def is_playing_node(self):
        return natives.npc_is_playing_node(self.ptr)

    def is_playing_node_paused(self):
        return natives.npc_is_playing_node_paused(self.ptr)

    def is_playing_playback(self):
        return natives.npc_is_playing_playback(self.ptr)

    def is_reload_enabled(self):
        return natives.npc_is_reload_enabled(self.ptr)

    def is_reloading(self):
        return natives.npc_is_reloading(self.ptr)

    def is_shooting(self):
        return natives.npc_is_shooting(self.ptr)

    def is_streamed_in(self, player):
        return natives.npc_is_streamed_in(self.ptr, player)

    def is_valid(self):
        return natives.npc_is_valid(self.ptr)

    @classmethod
    def is_valid_path(cls, path_id):
        return natives.npc_is_valid_path(path_id)

    @classmethod
    def is_valid_record(cls, record_id):
        return natives.npc_is_valid_record(record_id)

    def is_vehicle_siren_used(self):
        return natives.npc_is_vehicle_siren_used(self.ptr)

    @classmethod
    def load_record(cls, file_path):
        return natives.npc_load_record(file_path)

    def melee_attack(self, time, secondary_attack):
        return natives.npc_melee_attack(self.ptr, time, secondary_attack)

    def move(self, x, y, z, move_type, move_speed, stop_range):
        return natives.npc_move(self.ptr, x, y, z, move_type, move_speed, stop_range)

    def move_by_path(self, path_id, move_type, move_speed, reverse):
        return natives.npc_move_by_path(self.ptr, path_id, move_type, move_speed, reverse)

    def move_to_player(self, player, move_type, move_speed, stop_range, pos_check_update_delay, auto_restart):
        return natives.npc_move_to_player(self.ptr, player, move_type, move_speed, stop_range, pos_check_update_delay, auto_restart)

    @classmethod
    def open_node(cls, node_id):
        return natives.npc_open_node(node_id)

    def pause_playback(self, paused):
        return natives.npc_pause_playback(self.ptr, paused)

    def pause_playing_node(self):
        return natives.npc_pause_playing_node(self.ptr)

    def play_node(self, node_id, move_type, move_speed, radius, set_angle):
        return natives.npc_play_node(self.ptr, node_id, move_type, move_speed, radius, set_angle)

    def put_in_vehicle(self, vehicle, seat_id):
        return natives.npc_put_in_vehicle(self.ptr, vehicle, seat_id)

    def remove_from_vehicle(self):
        return natives.npc_remove_from_vehicle(self.ptr)

    @classmethod
    def remove_point_from_path(cls, path_id, point_index):
        return natives.npc_remove_point_from_path(path_id, point_index)

    def reset_animation(self):
        return natives.npc_reset_animation(self.ptr)

    def reset_surfing_data(self):
        return natives.npc_reset_surfing_data(self.ptr)

    def respawn(self):
        return natives.npc_respawn(self.ptr)

    def resume_playing_node(self):
        return natives.npc_resume_playing_node(self.ptr)

    def set_ammo(self, ammo):
        return natives.npc_set_ammo(self.ptr, ammo)

    def set_ammo_in_clip(self, ammo):
        return natives.npc_set_ammo_in_clip(self.ptr, ammo)

    def set_animation(self, animation_id, delta, loop, lock_x, lock_y, freeze, time):
        return natives.npc_set_animation(self.ptr, animation_id, delta, loop, lock_x, lock_y, freeze, time)

    def set_armour(self, armour):
        return natives.npc_set_armour(self.ptr, armour)

    def set_facing_angle(self, angle):
        return natives.npc_set_facing_angle(self.ptr, angle)

    def set_fighting_style(self, style):
        return natives.npc_set_fighting_style(self.ptr, style)

    def set_health(self, health):
        return natives.npc_set_health(self.ptr, health)

    def set_interior(self, interior):
        return natives.npc_set_interior(self.ptr, interior)

    def set_invulnerable(self, toggle):
        return natives.npc_set_invulnerable(self.ptr, toggle)

    def set_keys(self, up_and_down, left_and_right, keys):
        return natives.npc_set_keys(self.ptr, up_and_down, left_and_right, keys)

    @classmethod
    def set_node_point(cls, node_id, point_id):
        return natives.npc_set_node_point(node_id, point_id)

    def set_pos(self, x, y, z):
        return natives.npc_set_pos(self.ptr, x, y, z)

    def set_rot(self, rx, ry, rz):
        return natives.npc_set_rot(self.ptr, rx, ry, rz)

    def set_skin(self, model):
        return natives.npc_set_skin(self.ptr, model)

    def set_special_action(self, action):
        return natives.npc_set_special_action(self.ptr, action)

    def set_surfing_object(self, object):
        return natives.npc_set_surfing_object(self.ptr, object)

    def set_surfing_offset(self, x, y, z):
        return natives.npc_set_surfing_offset(self.ptr, x, y, z)

    def set_surfing_player_object(self, player, object_id):
        return natives.npc_set_surfing_player_object(self.ptr, player, object_id)

    def set_surfing_vehicle(self, vehicle):
        return natives.npc_set_surfing_vehicle(self.ptr, vehicle)

    def set_vehicle_gear_state(self, gear_state):
        return natives.npc_set_vehicle_gear_state(self.ptr, gear_state)

    def set_vehicle_health(self, health):
        return natives.npc_set_vehicle_health(self.ptr, health)

    def set_vehicle_hydra_thrusters(self, direction):
        return natives.npc_set_vehicle_hydra_thrusters(self.ptr, direction)

    def set_vehicle_train_speed(self, speed):
        return natives.npc_set_vehicle_train_speed(self.ptr, speed)

    def set_virtual_world(self, virtual_world):
        return natives.npc_set_virtual_world(self.ptr, virtual_world)

    def set_weapon(self, weapon):
        return natives.npc_set_weapon(self.ptr, weapon)

    def set_weapon_accuracy(self, weapon, accuracy):
        return natives.npc_set_weapon_accuracy(self.ptr, weapon, accuracy)

    def set_weapon_clip_size(self, weapon, size):
        return natives.npc_set_weapon_clip_size(self.ptr, weapon, size)

    def set_weapon_reload_time(self, weapon, time):
        return natives.npc_set_weapon_reload_time(self.ptr, weapon, time)

    def set_weapon_shoot_time(self, weapon, time):
        return natives.npc_set_weapon_shoot_time(self.ptr, weapon, time)

    def set_weapon_skill_level(self, skill, level):
        return natives.npc_set_weapon_skill_level(self.ptr, skill, level)

    def shoot(self, weapon, hit_id, hit_type, end_x, end_y, end_z, offset_x, offset_y, offset_z, is_hit, check_in_between_flags):
        return natives.npc_shoot(self.ptr, weapon, hit_id, hit_type, end_x, end_y, end_z, offset_x, offset_y, offset_z, is_hit, check_in_between_flags)

    def spawn(self):
        return natives.npc_spawn(self.ptr)

    def start_playback(self, record_name, auto_unload, start_pos_x, start_pos_y, start_pos_z, start_rot_x, start_rot_y, start_rot_z):
        return natives.npc_start_playback(self.ptr, record_name, auto_unload, start_pos_x, start_pos_y, start_pos_z, start_rot_x, start_rot_y, start_rot_z)

    def start_playback_ex(self, record_id, auto_unload, start_pos_x, start_pos_y, start_pos_z, start_rot_x, start_rot_y, start_rot_z):
        return natives.npc_start_playback_ex(self.ptr, record_id, auto_unload, start_pos_x, start_pos_y, start_pos_z, start_rot_x, start_rot_y, start_rot_z)

    def stop_aim(self):
        return natives.npc_stop_aim(self.ptr)

    def stop_melee_attack(self):
        return natives.npc_stop_melee_attack(self.ptr)

    def stop_move(self):
        return natives.npc_stop_move(self.ptr)

    def stop_playback(self):
        return natives.npc_stop_playback(self.ptr)

    def stop_playing_node(self):
        return natives.npc_stop_playing_node(self.ptr)

    @classmethod
    def unload_all_records(cls):
        return natives.npc_unload_all_records()

    @classmethod
    def unload_record(cls, record_id):
        return natives.npc_unload_record(record_id)

    def update_node_point(self, point_id):
        return natives.npc_update_node_point(self.ptr, point_id)

    def use_vehicle_siren(self, use):
        return natives.npc_use_vehicle_siren(self.ptr, use)


class Class:
    def __init__(self, ptr):
        self.ptr = ptr

    @classmethod
    def add(cls, team, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3):
        return natives.class_add(team, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3)

    @classmethod
    def count(cls):
        return natives.class_count()

    def edit(self, teamid, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3):
        return natives.class_edit(self.ptr, teamid, skin, x, y, z, angle, weapon1, ammo1, weapon2, ammo2, weapon3, ammo3)

    @classmethod
    def from_id(cls, classid):
        result = natives.class_from_id(classid)
        ptr = result[0] if isinstance(result, tuple) else result
        return cls(ptr) if ptr else None

    def get_data(self):
        return natives.class_get_data(self.ptr)

    def get_id(self):
        return natives.class_get_id(self.ptr)


__all__ = ["Actor", "Player", "Vehicle", "Object", "Pickup", "GangZone", "Menu", "TextDraw", "TextLabel", "Npc", "Class"]

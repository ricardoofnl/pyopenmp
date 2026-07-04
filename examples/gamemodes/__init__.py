from pyopenmp import (
    Player,
    colors,
    on_player_command_text,
    on_player_connect,
    on_player_spawn,
)

from gamemodes.core import core


@on_player_connect
def welcome(player: Player):
    core.log_join(player)
    player.send_client_message(colors.GREEN, "Welcome to the server!")


@on_player_spawn
def spawn(player: Player):
    player.set_health(100.0)


@on_player_command_text
def commands(player: Player, text: str) -> bool:
    return core.handle_command(player, text)

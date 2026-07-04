from pyopenmp import (
    Player,
    colors,
    on_player_command_text,
    on_player_connect,
    on_player_spawn,
)
from pyopenmp.generated.natives import core_log


@on_player_connect
def welcome(player: Player):
    core_log("[example] player connected")
    player.send_client_message(colors.GREEN, "Welcome to the server!")


@on_player_spawn
def spawn(player: Player):
    player.set_health(100.0)


@on_player_command_text
def commands(player: Player, text: str) -> bool:
    if text == "/help":
        player.send_client_message(colors.YELLOW, "Commands: /help")
        return True
    return False

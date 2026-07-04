from pyopenmp import Player, colors
from pyopenmp.generated.natives import core_log


def log_join(player: Player):
    core_log("[example] player connected")


def handle_command(player: Player, text: str) -> bool:
    if text == "/help":
        player.send_client_message(colors.YELLOW, "Commands: /help")
        return True
    return False

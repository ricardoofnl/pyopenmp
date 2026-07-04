def rgba(r, g, b, a):
    return ((r & 0xFF) << 24) | ((g & 0xFF) << 16) | ((b & 0xFF) << 8) | (a & 0xFF)


def rgb(r, g, b):
    return rgba(r, g, b, 0xFF)


WHITE = 0xFFFFFFFF
BLACK = 0x000000FF
RED = 0xFF0000FF
GREEN = 0x00FF00FF
BLUE = 0x0000FFFF
YELLOW = 0xFFFF00FF
CYAN = 0x00FFFFFF
MAGENTA = 0xFF00FFFF
ORANGE = 0xFF8000FF
GREY = 0x808080FF

#include <stdbool.h>

struct CAPIStringView
{
    unsigned int len;
    const char* data;
};

bool Core_Log(const char* text)
{
    (void)text;
    return true;
}

float Player_GetHealth(void* player)
{
    (void)player;
    return 42.5f;
}

int Player_GetName(void* player, struct CAPIStringView* out)
{
    (void)player;
    static const char* name = "Test";
    out->data = name;
    out->len = 4;
    return 4;
}

bool Player_SendClientMessage(void* player, unsigned int color, const char* text)
{
    (void)player;
    (void)color;
    (void)text;
    return true;
}

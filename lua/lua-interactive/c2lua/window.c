#include <stdio.h>
#include <string.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#include "utils.h"

void load_size(lua_State *L, int *w, int *h)
{
	lua_getglobal(L, "width");
	lua_getglobal(L, "height");
	if (!lua_isnumber(L, -2))
		error(L, "'width' should be a number\n");
	
	if (!lua_isnumber(L, -1))
		error(L, "'height' should be a number\n");

	*w = lua_tointeger(L, -2);
	*h = lua_tointeger(L, -1);
	lua_pop(L, 2);
}

#define MAX_COLOR	255

struct ColorTable {
	char *name;
	unsigned char red, green, blue;
} colortable[] = {
	{"WHITE", MAX_COLOR, MAX_COLOR, MAX_COLOR},
	{"RED",   MAX_COLOR,         0,         0},
	{"GREEN",         0, MAX_COLOR,         0},
	{"BLUE",          0,         0, MAX_COLOR},
        {NULL,            0,         0,         0},
};

int getcolorfield(lua_State *L, const char *key)
{
	int result;

#if 0
	lua_pushstring(L, key);	/* push key */
	lua_gettable(L, -2);	/* get backgroud[key] */
#else
	lua_getfield(L, -1, key);
#endif

	if (!lua_isnumber(L, -1))
		error(L, "invalid component in background color");
	result = (int)(lua_tonumber(L, -1) * MAX_COLOR);
	lua_pop(L, 1);	/*remove number */
	return result;
}

void setcolorfield (lua_State *L, const char *key, int value)
{
	lua_pushstring(L, key);
#if 0
	lua_pushnumber(L, (double)value / MAX_COLOR);
	lua_settable(L, -3);
#else
	lua_setfield(L, -2, key);
#endif
}

void load_color(lua_State *L, int *r, int *g, int *b)
{
	lua_getglobal(L, "background");
	if (!lua_istable(L, -1))
		error(L, "backgroud is not a table");

	*r = getcolorfield(L, "r");
	*g = getcolorfield(L, "g");
	*b = getcolorfield(L, "b");
}

void setcolor(lua_State *L, struct ColorTable *ct)
{
	lua_newtable(L);
	setcolorfield(L, "r", ct->red);
	setcolorfield(L, "b", ct->blue);
	setcolorfield(L, "g", ct->green);

	lua_setglobal(L, ct->name);
}

int main()
{
	int i;
	int w, h;
	int r, g, b;
	lua_State *L = luaL_newstate();

	load_file(L, "win_cfg.lua");
	load_size(L, &w, &h);
	printf("w=%d, h=%d\n", w, h);

	load_color(L, &r, &g, &b);

	printf("r=%d, g=%d, b=%d\n", r, g, b);

	/* settable */
	i = 0;
	while ( colortable[i].name != NULL)
		setcolor(L, &colortable[i++]);

	stackDump(L);

}

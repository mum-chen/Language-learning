#include <stdarg.h>
#include <stdio.h>
#include <string.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"
#include "utils.h"

double f (lua_State *L, double x, double y)
{
	int isnum;
	double z;

	lua_getglobal(L, "f");
	lua_pushnumber(L, x);
	lua_pushnumber(L, y);
	
	if (lua_pcall(L, 2, 1, 0) != LUA_OK)
		error(L, "error running function 'f': %s",
		lua_tostring(L, -1));

	z = lua_tonumberx(L, -1, &isnum);
	if(!isnum)
		error(L, "function 'f' must return a number");
	lua_pop(L, 1);
	return z;
}

int main()
{
	int inner = -1;
	double r = 0;
	lua_State *L = luaL_newstate();
	luaL_openlibs(L);

	load_file(L, "req.lua");
	r = f(L, 0.3, 0.4);
	printf("%g\n", r);
}

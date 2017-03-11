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

void call_va(lua_State *L, const char *func, const char *sig, ...)
{
	va_list vl;
	int narg, nres;

	va_start(vl, sig);
	lua_getglobal(L, func);

	nres = strlen(sig);

	if (lua_pcall(L, narg, nres, 0) != 0)
		error(L, "error calling '%s': %s", func, lua_tostring(L, -1));
	
	va_end(vl);
}

int get(lua_State *L)
{
	int inner, isnum;

	lua_getglobal(L, "get");
	
	if (lua_pcall(L, 0, 1, 0) != LUA_OK)
		error(L, "error running function 'f': %s",
		lua_tostring(L, -1));

	inner = lua_tonumberx(L, -1, &isnum);
	if(!isnum)
		error(L, "function 'f' must return a number");
	lua_pop(L, 1);
	return inner;
}

void set(lua_State *L, int x)
{
	lua_getglobal(L, "set");

	lua_pushnumber(L, x);
	
	if (lua_pcall(L, 1, 0, 0) != LUA_OK)
		error(L, "error running function 'f': %s",
		lua_tostring(L, -1));
}

void inc(lua_State *L)
{
	lua_getglobal(L, "inc");

	if (lua_pcall(L, 0, 0, 0) != LUA_OK)
		error(L, "error running function 'f': %s",
		lua_tostring(L, -1));
	
}

/* varargs demo */
void p(lua_State *L)
{
	lua_getglobal(L, "p");

	lua_pushinteger(L, 1);
	lua_pushinteger(L, 2);
	lua_pushnumber(L, 3);
	if (lua_pcall(L, 3, 0, 0) != LUA_OK)
		error(L, "error running function 'f': %s",
		lua_tostring(L, -1));
	
}

/* push table */
void p_table(lua_State *L)
{
	lua_getglobal(L, "p_table");
	lua_newtable(L);
	lua_pushinteger(L, 1);
	lua_setfield(L, -2, "key1");

	lua_pushinteger(L, 2);
	lua_setfield(L, -2, "key2");

	lua_pushstring(L, "aaaaaa");
	lua_setfield(L, -2, "key3");

	stackDump(L);
	lua_pushinteger(L, 1);
	lua_pushstring(L, "aaaaaa");
	stackDump(L);
	lua_settable(L, -3);
	stackDump(L);
	
	if (lua_pcall(L, 1, 0, 0) != LUA_OK)
		error(L, "error running function 'f': %s",
		lua_tostring(L, -1));
}

int main()
{
	int inner = -1;
	double r = 0;
	lua_State *L = luaL_newstate();

	luaL_openlibs(L);
	load_file(L, "function.lua");
	r = f(L, 0.3, 0.4);
	
	printf("%g\n", r);

	inner = get(L); printf("%d\n", inner);
	inc(L);
	inner = get(L); printf("%d\n", inner);
	stackDump(L);

	p(L);
	p_table(L);
}

#include <stdio.h>
#include <string.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"

#include "utils.h"

int main(void)
{
	lua_State *L = luaL_newstate();

	lua_pushboolean(L, 1);
	lua_pushnumber(L, 10);
	lua_pushstring(L, "hello");
	lua_pushnil(L);
	lua_pushstring(L, "world");

	stackDump(L);

	/* replace top to index with shift */
	lua_insert(L, 2);
	stackDump(L);
	
	/* replace top to index without shift */
	lua_replace(L, 3);
	stackDump(L);

	/* copy from to */
	lua_copy(L, 4, 2);
	stackDump(L);

	lua_settop(L, 6);
	lua_copy(L, 2, 6);
	stackDump(L);

	lua_remove(L, -3);
	stackDump(L);
	//lua_remove(L, 1);	stackDump(L);

	lua_pushvalue(L, 1);
	lua_pushvalue(L, 2);
	lua_pushvalue(L, -3);
	stackDump(L);

	lua_settop(L, -3);
	stackDump(L);

	lua_close(L);

	return 0;
}

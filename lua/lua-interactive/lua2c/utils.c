#include <stdio.h>
#include <string.h>
#include "lua.h"
#include "lauxlib.h"
#include "lualib.h"

void stackDump(lua_State *L)
{
	int i;
	int top = lua_gettop(L); /* depth of the stack */
	for (i = 1; i <= top; i++) {
		int t = lua_type(L, i);
		switch(t) {
		case LUA_TSTRING:
			printf("[%d]='%s'", i, lua_tostring(L, i));
			break;
		case LUA_TBOOLEAN:
			printf("[%d]=%s", i, lua_toboolean(L, i) ? "true" : "false");\
			break;
		case LUA_TNUMBER:
			printf("[%d]=%g", i, lua_tonumber(L, i));
			break;
		default:
			printf("[%d]=%s", i, lua_typename(L, t));
			break;
		}
		printf("     "); /* separator */
	}
	printf("\n"); /* end of listing */
}


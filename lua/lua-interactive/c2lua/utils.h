#ifndef _UTILS_H_
#define _UTILS_H_

#include "lua.h"
#include "lauxlib.h"

extern void stackDump(lua_State *L);

static inline void load_file(lua_State *L, const char *fname)
{
	if (luaL_loadfile(L, fname) || lua_pcall(L, 0, 0, 0))
		error(L, "cannot run config. file: %s", lua_tostring(L, -1));
}

#endif

#include <stdio.h>
#include <string.h>
#include <lua.h>
#include <lauxlib.h>
#include <lualib.h>

#include "utils.h"

//待注册的C函数，该函数的声明形式在上面的例子中已经给出。
//需要说明的是，该函数必须以C的形式被导出，因此extern "C"是必须的。
//函数代码和上例相同，这里不再赘述。
static int add(lua_State* L)
{
	double op1 = luaL_checknumber(L,1);
	double op2 = luaL_checknumber(L,2);
	lua_pushnumber(L,op1 + op2);
	return 1;
}

static int sub(lua_State* L)
{
	double op1 = luaL_checknumber(L,1);
	double op2 = luaL_checknumber(L,2);
	lua_pushnumber(L,op1 - op2);
	return 1;
}

static double a = 10;

static inline int fail(lua_State *L, const char *msg)
{
	lua_pushboolean(L, 0);
	lua_pushstring(L, msg);
	return 2;
}

static int p_table(lua_State *L)
{
	int idx, isnum;
	unsigned char b[4];

	if (lua_istable(L, 1) == 0)
		return fail(L, "the input expect a table");
	
	for (idx = 0; idx < 4; idx ++) {
		lua_pushinteger(L, idx + 1);
		lua_gettable(L, -2); /* get t[idx + 1] */

		b[idx] = (unsigned char)lua_tointegerx(L, -1, &isnum);
		lua_pop(L, 1);

		if (isnum == 0)
			return fail(L, "the data in table expect integer");
	}
	
	printf("%d, %d, %d. %d\n", b[0], b[1], b[2], b[3]);

	lua_pushboolean(L, 1);
	return 1;
}


static int set(lua_State *L)
{
	a = luaL_checkinteger(L,1);
	return 0;
}

static int get(lua_State *L)
{
	lua_pushnumber(L, a);
	return 1;
}


//luaL_Reg结构体的第一个字段为字符串，在注册时用于通知Lua该函数的名字。
//第一个字段为C函数指针。
//结构体数组中的最后一个元素的两个字段均为NULL，用于提示Lua注册函数已经到达数组的末尾。
static luaL_Reg mylibs[] = {
	{"add", add},
	{"sub", sub},
	{"get", get},
	{"set", set},
	{"p_table", p_table},
	{NULL, NULL}
};

//该C库的唯一入口函数。其函数签名等同于上面的注册函数。见如下几点说明：
//1. 我们可以将该函数简单的理解为模块的工厂函数。
//2. 其函数名必须为luaopen_xxx，其中xxx表示library名称。Lua代码require "xxx"需要与之对应。
//3. 在luaL_register的调用中，其第一个字符串参数为模块名"xxx"，第二个参数为待注册函数的数组。
//4. 需要强调的是，所有需要用到"xxx"的代码，不论C还是Lua，都必须保持一致，这是Lua的约定，
//   否则将无法调用。
int luaopen_simple(lua_State* L)
{
	luaL_newlib(L, mylibs);
	return 1;
}

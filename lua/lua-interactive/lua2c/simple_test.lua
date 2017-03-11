local simple = require("simple")
local simple_2 = require("simple")

local a = simple.sub(10, 30)
print("a=", a)

local b = simple.get()
print("b=", b)

simple.set(40);
local c = simple.get()
print("c=", c)

local d = simple_2.get()
print("d=", d)

print(simple.p_table({1, 2, 3, 4}))
print(simple.p_table({1, 2, 3}))
print(simple.p_table(2))


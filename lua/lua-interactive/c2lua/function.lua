function f(x, y)
	return (x ^ 2 * y) / (1 - x)
end


local inner = 1;

function get()
	return inner;
end

function set(x)
	inner = x
end

function inc()
	inner = inner + 1
end


function p(...)
	print(...)
end

function p_table(_table)
	if type(_table) ~= "table" then
		return
	end

	for k, v in pairs(_table) do
		print(string.format("[%s:%s] = %s:%s", type(k), k, type(v),v))
	end
end

CC = gcc
INCLUDE = -I/usr/local/include
LIB = -L/usr/local/lib/
FLAG = -DLUA_USEREADLINE

LIB_A = /usr/local/lib/liblua.a

LINK_LINB =
LINK_LINB += -ldl
LINK_LINB += -lm

req:require.c
	$(CC) $(INCLUDE) $(LIB) $^ $(LIB_A) $(LINK_LINB) -o $@

function:function.c utils.c utils.h
	$(CC) $(INCLUDE) $(LIB) $^ $(LIB_A) $(LINK_LINB) -o $@

window:window.c utils.c utils.h
	$(CC) $(INCLUDE) $(LIB) $^ $(LIB_A) $(LINK_LINB) -o $@

stackDump:stackDump.c utils.c utils.h
	$(CC) $(INCLUDE) $(LIB) $^ $(LIB_A) $(LINK_LINB) -o $@

first:first.c
	$(CC) $(INCLUDE) $(LIB) $^ $(LIB_A) $(LINK_LINB) -o $@

.PHONY: clean
clean:
	rm -f first stackDump window function req

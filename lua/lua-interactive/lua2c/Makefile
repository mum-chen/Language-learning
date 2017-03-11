CC = gcc
INCLUDE = -I/usr/local/include
LIB = -L/usr/local/lib/
FLAG = -DLUA_USEREADLINE

LIB_A = /usr/local/lib/liblua.a

LINK_LINB =
LINK_LINB += -ldl
LINK_LINB += -lm

#$(CC) $(INCLUDE) $(LIB) -fPIC -shared $^ $(LIB_A) $(LINK_LINB) -o $@

simple.so:simplelib.c utils.c
	$(CC) -Wall -fpic -llua -shared -o $@ $^

simple:simple.c
	$(CC) $^ $(LIB_A) $(LINK_LINB) -o $@

.PHONY: clean
clean:
	rm -f simple simple.so

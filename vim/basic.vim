echo "while demo"
let i = 1
while i < 5
    echo "count is" i
    let i += i
endwhile

echo "----------"
echo "for demo"
for i in range(1, 4)
    echo "count is" i
endfor

echo "continue & break are also function"

echo "----------"
echo "variable"
let s:count = 1
while s:count < 5
    let s:count += 1
endwhile
echo "b:name local to a buffer"
echo "w:name local to a window"
echo "g:name global varibale(alse in a function)"
echo "b:name variable predefined by vim"

echo "----------"
echo "delete variable"
unlet s:count
" unlet s:count " cause some error
unlet! s:count  " unlet with save way

if !exists("s:call_count")
    let s:call_count = 0
endif
let s:call_count = s:call_count + 1
echo "called" s:call_count "times"

echo "----------"
echo "sting"
echo 'hello \t world\n'
echo "hello \t world\n"
echo '"\<Esc>" --> "<Esc>"'
echo "see expr-quote for the full list of special items in a string"

echo "----------"
echo "Expressions"
echo '$Name enviroment varibale'
echo '&name option'
echo '@r register'

echo "The value of 'tabstop' is" &ts
echo "Your home dirctory is" $HOME
if @a > 5
    echo '@a more then 5'
elseif @a > 3
    echo '@a less then 3'
elseif @a == 0
    echo '@a == 0'
else
    echo 'unexpected @a'
endif

echo "----------"
echo "string match"

if 0 == "2"
    echo '0 == "2"'
else
    echo '0 != "2"'
endif

if 0 == "mum-chen"
    echo '0 == "mum-chen"'
else
    echo '0 != "mum-chen"'
endif

let str = ""

if str =~ " "
    echo "str contains a space"
endif
if str != '\.$'
    echo "str does not end in a full stop"
endif

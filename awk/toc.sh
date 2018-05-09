#!/bin/sh

sep() {
	echo "================================================"
}


echo "BEGIN only execute one time"
awk 'BEGIN{printf "Sr No\tName\tSub\tMarks\n"} {print}' marks.txt
sep

echo "Execute file with -f"
awk -f ./first_print.awk marks.txt
sep

echo "Assinate varialbe with -v"
awk -v name=Jerry -f print_variable.awk
sep

echo "dump-variables[=file]"
awk --dump-variables ''
cat awkvars.out
sep

echo "awk --lint '' /bin/ls"
echo "awk --profile"
awk --profile 'BEGIN{printf"---|Header|--\n"} {print}
END{printf"---|Footer|---\n"}' marks.txt > /dev/null
cat awkprof.out
sep

echo "awk default print all the mathed info"
echo "The follow code have the same meanning"
echo 'print with $0'
awk '/a/ {print $0}' marks.txt
echo 'print without $0'
awk '/a/' marks.txt
sep

echo "print disorder"
awk -f disorder.awk marks.txt
sep

echo "lines counter"
awk -f line_counter.awk marks.txt
sep

echo "filter with length"
awk 'length($3) > 6' marks.txt
sep

echo "ARGV and for"
awk -f for.awk one two three
sep

echo "config FS with -f"
awk 'BEGIN {print "FS should be space:FS = " FS}' | cat -vte
awk -F , 'BEGIN {print "FS should be comma:FS = " FS}' | cat -vte
sep

echo "filter with number of fileds, NF"
echo -e "One Two\nOne Two Three\nOne Two Three Four" | awk 'NF > 2'
sep

echo "inner variables"
awk -f inner_variables.awk marks.txt
sep

echo "array"
awk -f array.awk


BEGIN {
	arr[0] = 1;
	arr[1] = 2;
	arr[2] = 3;
	for (i in arr)
		printf "arr[%d] = %d\n", i, arr[i]
}

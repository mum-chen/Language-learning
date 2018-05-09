BEGIN {
	print ("Conversion Format = ", CONVFMT)
	print ("number output format OFMT = ", OFMT)
	print ("Arguments =", ARGC)
	print (ENVIRON["USER"])
	print "OFS = " OFS
	print "ORS = " ORS
}

NR < 3 {
	printf ("NR less then 3:%d, FNR:%d\n", NR, FNR)
}

END {
	print FILENAME
}


double x = x + x
quadruple x = double (double x)

factorial n = product [1 .. n]

average ns = div (sum ns) (length ns)

average_new ns = sum ns `div` length ns

myLast ns = head (reverse ns)

myInit ns = take (length ns - 1) ns

myInit2 ns = reverse (tail (reverse ns))

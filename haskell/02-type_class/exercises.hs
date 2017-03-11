{-
 - 1. [String]
 - 2. (String, String, String)
 - 3. [(Bool, String)]
 - 4. ([a, a])
 - 5. [Function]
 -}

second xs = head(tail xs)
swap (x, y) = (y, x)
pair x y = (x, y)
double x = x * 2
palindrom xs = reverse xs == xs
twice f x = f(f x)


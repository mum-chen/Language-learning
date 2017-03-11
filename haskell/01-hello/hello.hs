{-
 - copy from http://www.jdon.com/idea/haskell.html
 -}
-- main test
main = putStrLn "Hello, world!"
-- the right will replace the left one
addOne :: Integer -> Integer
addOne n = n + 1

-- match
lastName :: String -> String
lastName "anthony" = "gillis"
lastName "michelle" = "jocasta"
lastName "gregory" = "tragos"
lastName "LYC" = "Mum-Chen"
-- default value
lastName n = "<unknown>"

-- mult-args
areAscending :: Integer -> Integer -> Integer -> Bool
areAscending a b c = a < b && b < c

fizzBuzzHelper :: Integer -> String
fizzBuzzHelper n
    | n `mod` 3 == 0 && n `mod` 5 == 0 = "fizzbuzz"
    | n `mod` 3 == 0 = "fizz"
    | n `mod` 5 == 0 = "buzz"
    | otherwise = ""

-- none-args
someValue :: String
someValue = "hello world"

-- binding
x = 2
y = 3

compute = let z = x + y
    in print z

-- bad = print add 2 3
fine = print (2 + 3)

-- variable is constant
n1 = 5
-- error
-- n1 = 6

{- new frome old -}
isDigit :: Char -> Bool
isDigit c = c >= '0' && c <= '9'

myEven :: Integral a => a -> Bool
myEven n = n `mod` 2 == 0

mySplitAt :: Int -> [a] -> ([a], [a])
mySplitAt n xs = (take n xs, drop n xs)

myRecipe :: Fractional a => a -> a
myRecipe n = 1 / n

{- Conditional expressions -}
myAbs :: Int -> Int
myAbs n = if n >= 0 then n else -n

{-
 - in Haskell must always have an else branch,
 -}
mySignum :: Int -> Int
mySignum n = if n < 0 then - 1 else
                if n == 0 then 0 else 1

{- Guarded equations -}

myAbsG n| n >= 0 = n
        | otherwise = -n

mySignumG n | n < 0     = -1
            | n == 0    = 0
            | otherwise = 1

{- Pattern matching -}
(&&&) :: Bool -> Bool -> Bool
True  &&& True  = True
False &&& True  = False
True  &&& False = False
False &&& False = False

(&&&&) :: Bool -> Bool -> Bool
True &&&& True = True
_    &&&& _    = False


(&&&&&) :: Bool -> Bool -> Bool
True  &&&&& b = b
False &&&&& _ = False


(^^^):: Bool -> Bool -> Bool

b ^^^ c | b == c    = b
        | otherwise = False

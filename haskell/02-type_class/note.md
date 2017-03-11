## check type
```Haskell
:type expression
```


## Basic type
Bool    --> logical value
Char    --> single characters
String  --> strings of characters
Int     --> fixed precision integers
Integer --> arbitrary-precision integers
Float   --> single-precision floating-point number


## List types
[False, True, False] :: [Bool]

[['a', 'b'], ['c', 'd', 'e']] :: [[Char]]

## Tuple type
The number of components in a tuple is called arity.
Tuples of arity one, such as ( False ), are not permitted because they would conflict with the use of parentheses to make the evaluation order explicit, such as in (1 + 2) ∗ 3.

## Function types
A function is a mapping from arguments of one type to result of another type.
not     :: Bool -> Bool
isDigit :: Char -> Bool

example:
```Haskell
add :: (Int, Int) -> Int
add (x, y) = x + y

zeroto :: Int -> [Int]
zeroto n = [0..n]
```
Note that there is no restriction that functions must be total on their argu- ment type, in the sense that there may be some arguments for which the result is not defined. For example, the result of the library function head that selects the first element of a list is undefined if the list is empty.

#### Curried funtions
add  :: (Int, Int) -> Int

addNew :: Int -> (Int -> Int)
addNew x y = x + y
means:
	addNew x = f(x + y)
	f(x + y) y = x + y

	mult :: Int -> (Int -> (Int -> Int))
same as
	mult :: Int -> Int -> Int -> Int

	mult x y z = x * y * z
same as
	(((mult x) y) z)

#### Polymorphic type

length :: [a] -> Int

#### overloaded
A type that contains one or more class constraints is called overloaded

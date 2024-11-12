# Python divides the operators in the following groups:

# Arithmetic operators
x, y = 5, 2

# Operator	Name
# +	Addition	x + y
print(x + y)

# -	Subtraction	x - y
print(x - y)

# *	Multiplication	x * y
print(x * y)

# /	Division	x / y
print(x / y)  # Returns 2.5

# %	Modulus	x % y
print(x % y)  # Returns  1 i.e remainder

# **	Exponentiation	x ** y
print(x ** y)

# //	Floor division	x // y
print(x // y)  # Returns Question value

# Assignment operators
# Relational/Comparison operators = Always return a Boolean Value
print(x == y)  # ==	Equal	x == y
print(x != y)  # !=	Not equal	x != y
print(x > y)  # >	Greater than	x > y
print(x < y)  # <	Less than	x < y
print(x >= y)  # >=	Greater than or equal to	x >= y
print(x <= y)  # <=	Less than or equal to	x <= y

# Logical operators = = Always return a Boolean Value
print(x < 5 and x < 10)  # and 	Returns True if both statements are true	x < 5 and  x < 10
print(x < 5 or x < 4)  # or	Returns True if one of the statements is true	x < 5 or x < 4
print(not (x < 5 and x < 10))  # not	Reverse the result, returns False if the result is true

# Identity operators
print(x is y)  # is 	Returns True if both variables are the same object	x is y
print(x is not y)  # is not	Returns True if both variables are not the same object	x is not y

# Membership operators
# in 	Returns True if a sequence with the specified value is present in the object	x in y
x1 = ["apple", "banana"]
print("banana" in x1)
print("banana" not in x1)  # not in	Returns True if a sequence with the specified value is not present in the object x
# not in y
# Bitwise operators

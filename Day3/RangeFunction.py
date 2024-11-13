# Definition and Usage
# The range() function returns a sequence of numbers, starting from 0 by default, and increments
# by 1 (by default), and stops before a specified number.

# Syntax range(start, stop, step)
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(5, 10)))  # [5, 6, 7, 8, 9]
print(list(range(5, 10, 2)))  # [5, 7, 9]
print(list(range(10,1,-1))) # [10, 9, 8, 7, 6, 5, 4, 3, 2]  Can pass Negative value
print(list(range(-10,-5))) #[-10, -9, -8, -7, -6]
print(list(range(-10,-5,2))) # [-10, -8, -6]



# Chapter 14: Functional Programming in Python

numbers = [1, 2, 3, 4, 5]

# Using map and filter
squares = list(map(lambda x: x*x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(squares)
print(evens)
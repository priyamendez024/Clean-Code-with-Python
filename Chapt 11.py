# Chapter 11: Working with Iterators and Generators

def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
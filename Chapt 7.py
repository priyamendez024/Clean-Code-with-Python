# Chapter 7: Modules and Packages

# Example: utils/math_utils.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Usage:
from utils.math_utils import add

print(add(5, 3))  # 8
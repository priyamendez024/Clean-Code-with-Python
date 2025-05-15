# Chapter 6: Handling Errors Gracefully

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return None

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # None, with error message
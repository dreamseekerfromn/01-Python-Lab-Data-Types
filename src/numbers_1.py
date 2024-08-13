# Task 1: Complex Arithmetic
# ---------------------------
# Evaluate the following expressions and assign the results to variables:
# 1. (25 + 30) * (15 / 3) - 4 ** 2
# 2. ((45 % 6) * 2) + (100 / 5) ** 3
# 3. (50 * 2) - ((3 ** 2) * (8 + 5)) / (4 % 3)

# Write the answers in comments below each expression and print the results.
def taskOne():
    print((25+30)*(15/3)-4**2)
    print(((45%6)*2)+(100/5)**3)
    print((50*2)-((3**2)*(8+5))/(4%3))
    pass
# Task 2: Type Identification
# ---------------------------
# Identify the data type of the following expressions:
# 1. 10 + 5.0
# 2. 100 / 3
# 3. 100 // 3
# 4. 4 ** 0.5

# Use the `type()` function to verify the data types and print them.
def taskTwo():
    print(type(10+5.0)) #float b/c int divides by float
    print(type(100/3)) #float, 33.333333333....
    print(type(100//3)) #int
    print(type(4**0.5)) #float
    pass

# Task 3: Arithmetic Error Handling
# ---------------------------------
# Write a Python function that attempts to divide two numbers and catches any potential errors (e.g., division by zero).
# Return a custom error message if an error occurs.

def safe_divide(a, b):
    # Your code here
    try:
        return a/b
    except ArithmeticError:
        return 'Error: Division by zero'
    pass

# Task 4: Advanced Arithmetic
# ---------------------------
# Write a Python function that takes an integer and returns:
# 1. The factorial of the number.
# 2. The sum of all digits in the number.

def factorial(n):
    # Your code here
    result = 1
    for x in range(n):
        result *= (x + 1)
    return result
    pass

def sum_of_digits(n):
    # Your code here
    result = 0
    for x in str(n):
        result += int(x)
    return result
    pass

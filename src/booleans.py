# Task 1: Complex Boolean Expressions
# -----------------------------------
# Evaluate the following boolean expressions:
# 1. (10 > 5) and (5 <= 3) or (100 == 100)
# 2. not (7 != 7) or ((3 < 2) and (4 == 4))
# 3. (4 ** 2 > 15) and ((100 / 10) < 9) or (5 == 5 and not (10 == 10))

# Write the answers in comments below each expression and print the results.
# 1. true 2. true 3. false
print((10 > 5) and (5 <= 3) or (100 == 100)) # true and false or true = false or true = true
print(not (7 != 7) or ((3 < 2) and (4 == 4))) # not false or (false and true) = true or false = true
print((4 ** 2 > 15) and ((100 / 10) < 9) or (5 == 5 and not (10 == 10))) #(true and false) or (true and not true) = false or false = false
# Task 2: Boolean Function
# ------------------------
# Write a Python function that takes two numbers as input and returns True if the first number is divisible by the second, and False otherwise.

def is_divisible(x, y):
    # Your code here
    try:
        if(x%y == 0):
            return True
        return False
    except ArithmeticError:
        return False
    pass

# Task 3: Complex Logical Operations
# ----------------------------------
# Write a Python function that evaluates whether a given integer is:
# 1. Positive, even, and divisible by 3.
# 2. Negative, odd, and greater than -10.

def complex_check(n):
    # Your code here
    try:
        if(n > 0):
            if(n % 6 == 0):
                return True
        elif(n < 0):
            if(n % 2 == 1 or n % 2 == -1):
                if(n > -10):
                    return True
        return False
    except ArithmeticError:
        return False
    pass

# Task 4: Boolean Type Conversion
# -------------------------------
# Convert the following expressions to booleans using the `bool()` function and explain the results:
# 1. 0
# 2. 3.14
# 3. -100
# 4. ""
# 5. "False"
# 6. []

# Use the `bool()` function and print the results with comments explaining the outcomes.
print(bool(0))#falsey
print(bool(3.14))#truthy
print(bool(-100))#truthy
print(bool(""))#falsey
print(bool("False"))#truthy
print(bool([]))#falsey
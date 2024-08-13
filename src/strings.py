# strings.py

# Task 1: String Manipulation
# ---------------------------
# 1. Concatenate the following strings: "Python", " is", " awesome!"
# 2. Repeat the string "Code" 7 times and print the result.
# 3. Extract the substring "top" from the string "Octopocalypse".
# 4. Reverse the string "Python".

# Print the results of each operation.
print("Python" + " is" + " awesome!")
for x in range(6):
    print("Code")
print("Octopocalypse"[2:5])
print("Python"[::-1])
# Task 2: Advanced String Operations
# ----------------------------------
# Write a Python function that:
# 1. Counts the number of vowels in a given string.
# 2. Replaces all occurrences of a given character in a string with another character.

def count_vowels(s):
    # Your code here
    vowels = 0
    for x in s.lower():
        if(x == 'a' or x=='e' or x == 'i' or x =='o' or x=='u'):
            vowels += 1
    return vowels
    pass

def replace_char(s, old, new):
    # Your code here
    return s.replace(old, new)
    pass

# Task 3: String Formatting
# -------------------------
# Write a Python function that accepts a user's first name and last name, then returns a string formatted as "Last, First".
# If the name is not provided (either first or last), it should default to "Unknown".

def format_name(first_name="Unknown", last_name="Unknown"):
    if (first_name == "Unknown" or last_name =="Unknown"): return "Unknown"
    else: return last_name + ", " + first_name
    # Your code here
    pass

# Task 4: String Validation
# -------------------------
# Write a Python function that checks if a given string is a valid email address. For simplicity, assume an email is valid if it contains exactly one "@" symbol and at least one "." after the "@".

def is_valid_email(email):
    # Your code here
    if(not email.find("@") or not email.find(".")):
        return False
    try:
        if(email.index("@") != email.rindex("@")):
            return False
        if(email.index(".") != email.rindex(".")):
            return False
        if(email.index("@") > email.index(".")):
            return False
        if(email.index("@") - email.index(".") == -1):
            return False
        return True
    except ValueError:
        return False
    pass


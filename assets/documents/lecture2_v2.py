# Based on: https://learnxinyminutes.com/docs/python/

# 1. Python has a print function
print("I'm Python. Nice to meet you!")  # => I'm Python. Nice to meet you!

# 2. Simple way to get input data from console
input_string_var = input("Enter some data: ")  # Returns the data as a string
print(input_string_var)
print("Your data are: ", input_string_var)  # => Your data are:  some_data
print("Your data are: " + input_string_var)  # => Your data are: some_data
print("Your data are: " + input_string_var + ".")  # => Your data are: some_data.

# 3. You have numbers
3  # => 3

# 4. Many types of numbers
type(1)  # => <class 'int'>
type(1.1)  # => <class 'float'>

# 5. Some are not numbers
type("1")  # => <class 'str'>

# but you can turn them into numbers
type(int("1"))  # => <class 'int'>

# 6. Math is what you would expect
1 + 1  # => 2
8 - 1  # => 7
10 * 2  # => 20
35 / 5  # => 7.0

# 7. Floor division rounds towards negative infinity
5 // 3  # => 1
-5 // 3  # => -2
5.0 // 3.0  # => 1.0  # works on floats too
-5.0 // 3.0  # => -2.0

# 8. The result of division is always a float
10.0 / 3  # => 3.3333333333333335

# 9. We can round numbers
17 / 2.3  # => 7.391304347826088
round(17 / 2.3, ndigits=2)  # => 7.39

# 10. Modulo operation
7 % 3  # => 1
# 11. a % b have the same sign as b
-7 % 3  # => 2

# 12. Exponentiation (x**y, x to the yth power)
2 ** 3  # => 8

# 13. Enforce precedence with parentheses
1 + 3 * 2  # => 7
(1 + 3) * 2  # => 8

# 14. Reference
a = 5  # Point a at 5 (a "stores" the number 5)
b = a  # Point b at what a is pointing to
b is a  # => True, a and b refer to the same object
b == a  # => True, a's and b's objects are equal

# 15. Strings are created with " or '
"This is a string."
"This is also a string."

# 16. Strings can be added too
"Hello " + "world!"  # => "Hello world!"

# 17. String literals (but not variables) can be concatenated without using '+'
"Hello " "world!"  # => "Hello world!"

# 18. Since Python 3.6, you can use f-strings or formatted string literals.
name = "Reiko"
f"She said her name is {name}."  # => "She said her name is Reiko"

# 19. Any valid Python expression inside these braces is returned to the string.
f"{name} is {20 + 2} years old."  # => "Reiko is 5 characters

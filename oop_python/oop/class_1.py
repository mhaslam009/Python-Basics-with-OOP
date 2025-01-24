#arithematic operations

a = 10
b = 5

# Addition
result_add = a + b  # result_add will be 15
# Subtraction
result_sub = a - b  # result_sub will be 5
# Multiplication
result_mul = a * b  # result_mul will be 50
# Division
result_div = a / b  # result_div will be 2.0 (floating-point division)
# Integer Division
result_int_div = a // b  # result_int_div will be 2 (floor division)
# Modulo (Remainder)
result_mod = a % b  # result_mod will be 0
# Exponentiation
result_exp = a ** b  # result_exp will be 100000
print(result_add,result_sub,result_mul,result_div,result_int_div,result_exp)

#conversion of numbers from int to float and float to integer

#Built in int function in python

# Absolute value
abs_value = abs(-10)  # abs_value will be 10
print("absolute_value:",abs_value)
# Maximum and minimum
max_value = max(5, 10, 3)  # max_value will be 10
min_value = min(5, 10, 3)  # min_value will be 3
print("max_val:",max_value)
print("min_val:",min_value)
# Integer to the power of another integer
power_result = pow(2, 3)  # power_result will be 8
print("pow_res:",power_result)

#string
#1-string concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2  # result will be "Hello World"
print(result)

#sring length

#string indexing

#string slicing

#string methods

# Convert case
message = "Hello, Python!"
uppercase_message = message.upper()    # uppercase_message will be "HELLO, PYTHON!"
lowercase_message = message.lower()    # lowercase_message will be "hello, python!"
titlecase_message = message.title()    # titlecase_message will be "Hello, Python!"

# Replace
message = "Hello, Python!"
new_message = message.replace("Hello", "Hi")  # new_message will be "Hi, Python!"

# Split
message = "Hello, Python!"
words = message.split(", ")   # words will be ["Hello", "Python!"]

#string formatting
name = "Alice"
age = 30

# Using f-string (Python 3.6+)
greeting = f"Hello, {name}. You are {age} years old."

# Using format() method
greeting = "Hello, {}. You are {} years old.".format(name, age)

my_list = [10, 20, 30, 40, "ha"]
my_list.remove(20)  # [10, 30, 40]
my_list.remove("ha")
popped_element = my_list.pop(1)  # Returns 30, and list becomes [10, 40]
del my_list[0]  # [40]
print(my_list)


my_dict = {"name": "John", "age": 30}
items_list = list(my_dict.items())  # [("name", "John"), ("age", 30)]
print(items_list)
my_dict.clear()   # Removes all key-value pairs
new_dict = my_dict.copy()  # Creates a shallow copy of the dictionary
my_dict1 = {"name": "John", "age": 30}
my_dict2 = my_dict.copy()  # Creates a shallow copy of the dictionary
print(my_dict2)


my_tuple = (1, 2, 2, 3, 4, 2)
count_of_2 = my_tuple.count(2)  # 3
print(count_of_2)
index_of_3 = my_tuple.index(1)  # 3 (index of the first occurrence)
print(index_of_3)

coordinates = 10, 20, "hello"
x, y, z = coordinates  # x will be 10, y will be 20
print(x)
print(y)
print(z)

my_set = {1, 2, 3, 4}
popped_element = my_set.pop()  # Returns an arbitrary element, and set becomes {2, 3, 4}
print(popped_element)
my_set.clear()   # Removes all elements


my_sets= {3, 1, 2,90}
print("Original set:", my_sets)

# No order is maintained
my_sets.add(-1)
print("After adding:", my_sets)


a = 10
b = 5

addition = a + b       # 15
subtraction = a - b    # 5
multiplication = a * b  # 50
division = a / b       # 2.0 (floating-point division)
print(division)
integer_division = a // b  # 2 (floor division)
print(integer_division)
modulo = a % b         # 0 (remainder)
print(f"if answer is {modulo}(zero) then {a} is  divisible by {b}")
exponentiation = a ** b     # 100000

my_variable = None
is_none = my_variable is None  # True
print(is_none)
print(my_variable)

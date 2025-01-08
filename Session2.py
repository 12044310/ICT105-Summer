"""
1. Variable Declaration and Types:
"""

a = 15
b = 12

print(type(a))
print(type(b))

"""
2. Basic Arithmetic Operations:
"""
addition = a + b
print(" a + b = ", addition)
subtract = a - b
print(" a - b = ", subtract)
multiply = a * b
print(" a * b = ", multiply)
divison = a / b
print(" a/ b = ", divison)

"""
3. Using Variables and Type Casting:
"""
c = a / b
print(c)
print(type(c))


c_float = float(c)
print("New Value of c(float) :", c_float)
print("New type of c : ", type(c_float))

"""
4. Working with Strings:
"""
message = "The result of a divided by b is"

result_message = message +" "+ str(c)

print(result_message)

"""
5. Using Comparison Operators:
"""
greater = a > b
print(greater) #True

equal = a==b
print(equal) #False

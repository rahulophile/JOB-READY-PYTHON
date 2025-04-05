a = 10
b = 20
# Comparison Operators
print(a == b)  # Equal to
print(a != b)  # Not equal to
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
# Identity Operators
print(a is b)  # True if both operands refer to the same object
print(a is not b)  # True if both operands do not refer to the same object
# Membership Operators
list1 = [1, 2, 3, 4, 5]
print(3 in list1)  # True if 3 is in the list
print(6 not in list1)  # True if 6 is not in the list
# Bitwise Operators
print(a & b)  # Bitwise AND
print(a | b)  # Bitwise OR
print(a ^ b)  # Bitwise XOR
print(~a)  # Bitwise NOT
print(a << 1)  # Left Shift
print(a >> 1)  # Right Shift
# Assignment Operators
a += 5  # a = a + 5
print(a)  # 15
b -= 5  # b = b - 5
print(b)  # 15
# Logical Operators
print(a > 5 and b < 20)  # True if both conditions are true
print(a > 5 or b > 20)  # True if at least one condition is true
print(not (a > 5))  # True if the condition is false
# Ternary Operator
result = "a is greater" if a > b else "b is greater"
print(result)  # "a is greater"
 
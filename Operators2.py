# # Relational Operators
# # 1. Equal to (==) : checks if two operands are equal
# a = 19
# b = 56
# print("Equal to is :", (a == b))

# # 2. Not equal to (!=) : checks if two operands are not equal
# a = 76
# b = 53
# print("Not equal to is :", (a != b))

# # 3. Greater than (>) : checks if the first operand is greater than the second operand
# a = 10
# b = 56
# print("Greater than is :", (a > b))

# # 4. Less than (<) : checks if the first operand is less than the second operand
# a = 87
# b = 77
# print("Less than is :", (a < b))

# # 5. Greater than or equal to (>=) : checks if the first operand is greater than or equal to the second operand
# a = 90
# b = 50
# print("Greater than or equal to is :", (a >= b))

# # 6. Less than or equal to (<=) : checks if the first operand is less than or equal to the second operand
# a = 18
# b = 50
# print("Less than or equal to is :", (a <= b))

# # Logical Operators
# # 1. AND (and) : returns True if both operands are True
# a = True
# b = False
# print("AND is :", (a and b))

# # 2. OR (or) : returns True if at least one of the operands is True
# a = True
# b = False
# print("OR is :", (a or b))

# # 3. NOT (not) : returns True if the operand is False, and vice versa
# a = True
# print("NOT is :", (not a))

# Bitwise Operators
# 0   0000
# 1   0001
# 2   0010
# 3   0011
# 4   0100
# 5   0101
# 6   0110
# 7   0111
# 8   1000
# 9   1001
# 10  1010

# # 1. AND (&) : performs bitwise AND operation on two operands
# a = 10
# b = 5
# print("AND is :", (a & b))

# # 2. OR (|) : performs bitwise OR operation on two operands
# print("OR is :", (a | b))

# # 3. XOR (^) : performs bitwise XOR operation on two operands
# print("XOR is :", (a ^ b))

# # 4. NOT (~) : performs bitwise NOT operation on an operand
# print("NOT is :", (~a))

# # 5. Left Shift (<<) : shifts the bits of the left operand to the left by the number of positions specified by the right operand
# print("Left Shift is :", (a << b))

# # 6. Right Shift (>>) : shifts the bits of the left operand to the right by the number of positions specified by the right operand
# print("Right Shift is :", (a >> b))

# a = 3
# b = 5
# print("OR is :", (a | b))

# a = 6
# b = 2
# print("AND is :", (a & b))

# print("XOR is :", (a ^ b))

# print("Right Shift is :", (a >> b))

# Special operator
a = "Instagram"
print("I" in "Instagram")
print("b" in "Instagram")

a = 3
b = 3
print(a is b)
print(a == b)
print(id(a) == id(b))
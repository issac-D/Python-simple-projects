#here is some examples of using bitwise operators in pthon programming language
# Example integers
a = 60  # Binary: 0011 1100
b = 13  # Binary: 0000 1101

# Bitwise AND
result_and = a & b  # Binary: 0000 1100 (Decimal: 12)
print(f"Bitwise AND: {result_and}")

# Bitwise OR
result_or = a | b  # Binary: 0011 1101 (Decimal: 61)
print(f"Bitwise OR: {result_or}")

# Bitwise XOR
result_xor = a ^ b  # Binary: 0011 0001 (Decimal: 49)
print(f"Bitwise XOR: {result_xor}")

# Bitwise NOT
result_not = ~a  
print(f"Bitwise NOT: {result_not}")

# Bitwise left shift
result_left_shift = a << 2  
print(f"Bitwise left shift: {result_left_shift}")

# Bitwise right shift
result_right_shift = a >> 2  
print(f"Bitwise right shift: {result_right_shift}")

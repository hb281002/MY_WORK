# 1. Arithmetic Operators
a = 10
b = 5
print("Arithmetic Operators:")
print("a + b =", a + b)      # Addition
print("a - b =", a - b)      # Subtraction
print("a * b =", a * b)      # Multiplication
print("a / b =", a / b)      # Division (float result)
print("a // b =", a // b)    # Floor Division (quotient without decimal)
print("a % b =", a % b)      # Modulus (remainder)
print("a ** b =", a ** b)    # Exponentiation (power)
print()

# 2. Comparison (Relational) Operators
print("Comparison Operators:")
print("a == b:", a == b)     # Equal to
print("a != b:", a != b)     # Not equal to
print("a > b:", a > b)       # Greater than
print("a < b:", a < b)       # Less than
print("a >= b:", a >= b)     # Greater than or equal to
print("a <= b:", a <= b)     # Less than or equal to
print()

# 3. Assignment Operators
print("Assignment Operators:")
x = 5
print("Initial x:", x)
x += 2                        # x = x + 2 (Addition assignment)
print("x += 2 →", x)
x -= 1                        # x = x - 1 (Subtraction assignment)
print("x -= 1 →", x)
x *= 3                        # x = x * 3 (Multiplication assignment)
print("x *= 3 →", x)
x /= 2                        # x = x / 2 (Division assignment)
print("x /= 2 →", x)
x //= 2                       # x = x // 2 (Floor Division assignment)
print("x //= 2 →", x)
x %= 2                        # x = x % 2 (Modulus assignment)
print("x %= 2 →", x)
x **= 3                       # x = x ** 3 (Exponentiation assignment)
print("x **= 3 →", x)
print()

# 4. Logical Operators
print("Logical Operators:")
a = 5
b = 10
print("a > 3 and b < 15:", a > 3 and b < 15)  # AND: both conditions true
print("a > 6 or b < 20:", a > 6 or b < 20)    # OR: one condition true
print("not(a > b):", not(a > b))             # NOT: reverses the result
print()

# 5. Bitwise Operators
print("Bitwise Operators:")
a = 5    # binary: 0101
b = 3    # binary: 0011
print("a & b =", a & b)      # AND: 0101 & 0011 = 0001 (1)
print("a | b =", a | b)      # OR:  0101 | 0011 = 0111 (7)
print("a ^ b =", a ^ b)      # XOR: 0101 ^ 0011 = 0110 (6)
print("~a =", ~a)            # NOT: ~0101 = -(a+1) = -6
print("a << 1 =", a << 1)    # Left shift: 0101 << 1 = 1010 (10)
print("a >> 1 =", a >> 1)    # Right shift: 0101 >> 1 = 0010 (2)
print()

# 6. Membership Operators
print("Membership Operators:")
list1 = [1, 2, 3, 4]
print("2 in list1:", 2 in list1)         # Checks if 2 is in the list
print("5 not in list1:", 5 not in list1) # Checks if 5 is NOT in the list
print()

# 7. Identity Operators
print("Identity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)        # True → same object in memory
print("x is z:", x is z)        # False → different objects with same content
print("x == z:", x == z)        # True → content is equal
print("x is not z:", x is not z) # True → not the same object

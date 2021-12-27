# 14 - Operator Assignment
# Operasi yang dapat dlakukan dengan penyingkatan
# Operasi ditambah dengan assignment

a = 5 # adalah assignment 
print("nilai a =", a)

a += 1 # artinya adalah a = a + 1
print("nilai a += 1, maka nila a menjadi", a)

a -= 2 # artinya adalah a = a - 2
print("nilai a -= 2, maka nila a menjadi", a)

a *= 5 # artinya adalah a = a * 5
print("nilai a *= 5, maka nila a menjadi", a)

a /= 2 # artinya adalah a = a / 2
print("nilai a /= 5, maka nila a menjadi", a)

b = 10
print("\nnilai b = ",b)

# Modulus dan Floor division
b %= 3
print("nilai b %= 3, maka nila b menjadi", b)

b = 10
print("\nnilai b = ",b)

b //= 3
print("nilai b //= 3, maka nila b menjadi", b)

# Pangkat / eksponen
a = 5
print("\nnilai a = ",a)
a **= 3
print("nilai a **= 3, maka nila a menjadi", a)

# Operasi Bitwise
# OR
c = True
print('nilai c = ',c)
c |= False
print('nilai c |= False, maka nilai c menjadi', c)

c = False
print('nilai c = ',c)
c |= False
print('nilai c |= False, maka nilai c menjadi', c)

# AND
c = True
print('\nnilai c = ',c)
c &= False
print('nilai c &= False, maka nilai c menjadi', c)

c = True
print('nilai c = ',c)
c &= True
print('nilai c &= True, maka nilai c menjadi', c)

# XOR
c = True
print('\nnilai c = ',c)
c ^= False
print('nilai c ^= False, maka nilai c menjadi', c)

c = True
print('nilai c = ',c)
c ^= True
print('nilai c ^= True, maka nilai c menjadi', c)

# Shifting (shift Right dan Shift Left)
d = 0b0100
print("\nnilai d =", format(d,'04b'))
d >>= 2
print("nilai d >>= 2, maka nilai d menjadi", format(d,'04b'))
d <<= 1
print("nilai d <<= 1, maka nilai d menjadi", format(d,'04b'))












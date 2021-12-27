# 08 - Operasi Aritmatika

a = 10
b = 3

# Operasi penjumlahan (+)
hasil = a + b
print("Hasil dari", a,'+',b,'=', hasil)

# Operasi pengurangan (-)
hasil = a - b
print("Hasil dari", a,'-',b,'=', hasil)

# Operasi perkalian (*)
hasil = a * b
print("Hasil dari", a,'*',b,'=', hasil)

# Operasi pembagian (/)
hasil = a / b
print("Hasil dari", a,'/',b,'=', hasil)

# Operasi eksponen (pangkat) (**)
hasil = a ** b
print("Hasil dari", a,'**',b,'=', hasil)

# Operasi modulus (sisa pembagian) (%)
hasil = a % b
print("Hasil dari", a,'%',b,'=', hasil)

# Operasi floor division (kebalikan modulus)
# pembulatan hasil bagi ke bawah dari hasil operasi pembagian
hasil = a // b
print("Hasil dari", a,'//',b,'=', hasil)

# prioritas operasi, operational precedence
"""
Urutan Perhitungan :
 1. ()
 2. exponen
 3. Perkalian (pembagian, modulus, floor)
 4. Penjumlahan 
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

# tanda kurung akan mengambil langkah paling pertama
hasil = (x + y) * z
print(x, '+', y, '*', z, '=', hasil) 























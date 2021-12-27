# 18 - Format String

# contoh generic
# string
nama = "Ucup"
format_str = f"hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"boolean = {boolean}"
print(format_str)

# angka
angka = 2005.5
format_str = f"angka = {angka}"
print(format_str)

# bilangan bulat
angka = 15
format_str = f"bilangan bulat = {angka:d}"
print(format_str)

# bilangan ribuan
angka = 2000000
format_str = f"bilangan ribuan = {angka:,}"
print(format_str)

# bilangan decimal
angka = 2005.54321
format_str = f"bilangan decimal = {angka:.3f}"
print(format_str)

# menampilkan leading zero
angka = 2005.54321
format_str = f"bilangan decimal = {angka:010.3f}"
print(format_str)

# menampilkan tanda + atau -
angka_minus = -10
angka_plus = 10.1234
format_minus = f"minus = {angka_minus:+d}"
format_plus = f"plus = {angka_plus:+.2f}"
print(format_minus)
print(format_plus)

# memformat persen 
persentase = 0.045
format_persen = f"persen = {persentase:.2%}"
print(format_persen)

# menampilkan operasi aritmatika di dalam placeholder
harga = 10000
jumlah = 5

format_str = f"jumlah total = Rp.{harga*jumlah:,}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hexadecimal = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)












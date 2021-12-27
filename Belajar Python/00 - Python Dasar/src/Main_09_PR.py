# PR dari episode 09

print("\nPROGRAM KONVERSI TEMPERATURE\n")

print("==========Komversi Fahrenheit===========\n")
# program konversi fahrenheit ke satuan lain
fahrenheit = float(input("Masukkan Suhu Fahrenheit = "))
print("Suhu adalah ", fahrenheit, "Fahrenheit")

# Celcius
# Rumus : 5/9*(F-32)
celcius = 5/9*(fahrenheit - 32)
print("Suhu dalam celcius adalah ", celcius, "Celcius")

# Reamur 
# Rumus : 4/9*(F-32)
reamur = 4/9*(fahrenheit - 32)
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# Kelvin
# Rumus : 5/9*(F-32)+273
kelvin = 5/9*(fahrenheit - 32) + 273
print("Suhu dalam kelvin adalah ", kelvin, "Kelvin")


print("\n============Komversi Kelvin=============\n")
# program konversi kelvin ke satuan lain
kelvin = float(input("Masukkan Suhu Kelvin = "))
print("Suhu adalah ", kelvin, "Kelvin")

# Celcius
# Rumus : K-273
celcius = kelvin - 273
print("Suhu dalam celcius adalah ", celcius, "Celcius")

# Reamur 
# Rumus : 4/5*(K-273)
reamur = 4/5*(kelvin - 273)
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# Fahrenheit
# Rumus : 9/5*(K-273) + 32
fahrenheit = 9/5*(kelvin - 273) + 32
print("Suhu dalam fahrenheit adalah ", fahrenheit, "Fahrenheit")
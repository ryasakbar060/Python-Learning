# 09 - Latihan Program Sederhana
# latihan konversi satuan temperatur

# program konversi celcius ke satuan lain

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float (input("Masukkan Suhu Dalam Celcius = "))
print("Suhu adalah ", celcius, "Celcius")

# Reamur
# Rumus : (4/5) * C
reamur = (4/5)*celcius
print("Suhu dalam reamur adalah ", reamur, "Reamur")

# Fahrenheit
# Rumus : (9/5) * C + 32
Fahrenheit = ((9/5) * celcius) + 32
print("Suhu dalam fahrenheit adalah ", Fahrenheit, "Fahrenheit")

# Kelvin
# Rumus : C + 273
Kelvin = celcius + 273
print("Suhu dalam kelvin adalah ", Kelvin, "Kelvin")

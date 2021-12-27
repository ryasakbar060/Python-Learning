# PR Espisode 12

#1 ----0++++5----8++++11----

X = float(input("Masukkan angka : "))

# ----0++++5----
Y = (X > 0) and (X < 5)
print("Hasil Y = ", Y)

# ----8++++11----
Z = (X > 8) and (X < 11)
print("Hasil Z = ", Z)

# ----0++++5----8++++11----
Hasil = Y or Z
print("Hasil yang di dapatkan adalah : ", Hasil)

print("\n",10*"=","\n")

#2 +++++0------5+++++8-----11+++++

P = float(input("Masukkan angka : "))

# +++++0------5+++++
Q = (P < 0) or (P > 5)
print("Hasil Q = ", Q)

# ++++++8------11++++
R = (P < 8) or (P > 11)
print("Hasil R = ", R)

# +++++0------5+++++8-----11+++++
Hasil = Q and R 
print("Hasil yang di dapatkan adalah : ", Hasil)















# 16 - Operasi dan Manipulasi String (Part 1)

# 1. Manyambung Sring (concatenate)
nama_pertama = "Ucup"
nama_tengah = "D"
nama_akhir = "Fame"

nama_lengkap = nama_pertama + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# 2. Menghitung Panjang Dari String
Panjang = len(nama_lengkap)
print("Panjang " + nama_lengkap + " = " + str(Panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atau string di string

d = "Ucup"
status = d in nama_lengkap
print(d + " ada di " + nama_lengkap + " = " + str(status))

d = "d"
status = d not in nama_lengkap
print(d + " tidak ada di " + nama_lengkap + " = " + str(status))

# mengulang string
print("wk"*10)
print(15*"wk")

# indexing (mengabil data dari string)
print("index ke-0 : " + nama_lengkap[0])
print("index ke-6 : " + nama_lengkap[6])
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] : " + nama_lengkap[0:4])
print("index ke-[3:7] : " + nama_lengkap[3:8])
print("index ke-[0,2,8,10] : " + nama_lengkap[0:11:2])

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk 'spasi' adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# operator dalam bentuk method

data = "otong surotong pararotong"
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))


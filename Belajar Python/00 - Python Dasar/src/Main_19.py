# 19 - String width and Alignment

# width and multiline

# data

data_nama = "Ucup Surucup"
data_umur = 17
data_tinggi = 150.1
data_nomor_sepatu = 44

# string standard
data_string = f"Nama = {data_nama}, Umur = {data_umur:d}, Tinggi = {data_tinggi}, Sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (dengan menggunakan enter, newline, \n)
data_string = f"Nama = {data_nama}, \nUmur = {data_umur:d}, \nTinggi = {data_tinggi}, \nSepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Ucup"
data_string = f"""Nama   = {data_nama:>5}
Umur   = {data_umur:>5}
Tinggi = {data_tinggi:>5}
Sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

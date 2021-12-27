# 17 - Operasi dan Manipulasi String (Part 2)

# Operator dalam bentuk methods

## merubah case dari string

# merubah semua ke upper case
salam = "bro!"
print("normal = " + salam)
salam = salam.upper()
print("upper = " + salam)

# merubah semua ke lower case
alay = "aKu KeCe AbieezZzZZZZZ"
print("normal = " + alay)
alay = alay.lower()
print("lower = " + alay)

## pengecekan dengan isX method

# contoh untuk pengecekan lower case
salam = "sist"
apakah_lower = salam.islower() # hasilnya boolean
print(salam + "is lower = " + str(apakah_lower))
apakah_upper = salam.isupper() # hasilnya boolean
print(salam + "is upper = " + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
pin = "abcdef"
cek_pin = pin.isalpha() 
print(pin + " apakah terdiri dari huruf semua? " + str(cek_pin))

# isalnum <-- huruf dan angka
pin = "abc123"
cek_pin = pin.isalnum() 
print(pin + " apakah terdiri dari huruf & angka? " + str(cek_pin))

# isdecimal() <-- angka saja
pin = "1234567"
cek_pin = pin.isdecimal() 
print(pin + " apakah terdiri dari angka saja? " + str(cek_pin))

# isspace() <-- spasi, tab, newline \n
kalimat = "Saya seorang guru.\nSaya mengajar bhs.inggris 2 tahun"
cek_kalimat = kalimat.isspace()
print(kalimat + " apakah terdapat sapasi, tab, newline? " + str(cek_kalimat))

# istitle() <-- semua kata dimulai dengan huruf besar
judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle() # hasilnya booleam
print(judul + " is title = " + str(cek_judul))

## mengecek komponen startswith() endswith() <-- keren
cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
print("start = " + str(cek_start))

cek_end = "Sengjangnim Oppak".endswith("Oppak")
print("end = " + str(cek_end))

## penggabungan komponen join() split()
pisah = ['aku','sayang','kamu']
gabungan = ','.join(pisah)
print(pisah)
print(gabungan)

gabungan = ' '.join(pisah)
print(gabungan)

gabungan = ' ehm '.join(pisah)
print(gabungan)

gabungan = 'akuehmsayangehmkamu'
print(gabungan.split('ehm'))

# alokasi karakter rjust(), ljust(), center()

kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,":")
print("'"+tengah+"'")

# kebalikannya --> strip()
kanan = "kanan".strip()
print("'"+kanan+"'")

kiri = "kiri".strip()
print("'"+kiri+"'")

tengah = "tengah".strip(":") #menghilangkan tanda titik dua (:)
print("'"+tengah+"'")

# Mengubah kata yang hurup depannya lower case menjadi upper case
word = "saya anak ke-2".capitalize()
print(word)







































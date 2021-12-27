# 15 - Pengenalan String

data = "ini adalah string"
print(data)
print(type(data))

# 1. Cara membuat string

'''
    1. Membuat string menggunakan single quote '...'
    2. Membuat string menggunakan double quote "..."
'''

data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

print('"Halo, apa kabar?"')
print("'Halo, apa kabar?'")
print("ini adalah hari jum'at")

# 2. Menggunakan tanda (\)

# membuat tanda ' menjadi string
print('mari salat jum\'at')
print('g\'day, isn\'t it?')

# backslash
print("C:\\user\\Ucup")

# tab
print("ucup\totong, jauhan")
print("ucup\t\t\totong, semakin jauhan")

# backspace
print("ucup \botong, jadi deketan")

# newline 
print("baris pertama.\nbaris kedua.") # LF -> line feed -> unix, macos, linux
print("baris pertama.\rbaris kedua.") # CR -> carriage return -> commodore, acorn, lisp
print("baris pertama.\r\nbaris kedua.") # CRLF -> line carriage return -> dipakai oleh windows

# 3. string literal atau raw

# hati-hati
print('C:\nnew folder') # akan salah pathnya
print('C:\\new folder') 

# menggunakan raw string
print(r'C:\new folder') # jika di tambahkan r maka kalimat string selanjutnya tak masalah

# multiline literal string
print("""
Nama : Ucup
Kelas : 3 SD
""")

# multiline literal string dan RAW
print(r"""
Nama : Ucip
Kelas : SD\new normal
Website : www.ucup.com/newID
""")







import string
abjad = string.printable

# Fungsi Enkripsi 
def enkripsi(pesan) :
    global abjad # untuk memanggil variable secara umum
    key = int(input('Masukkan Key : '))
    cipher = '' # untuk menampilkan cipher enkripsi sesuai kaidah caesar cipher
    for i in pesan:
        if i in abjad:
            k = abjad.find(i) # untuk menentukan variable sebelumnya yang telah di jadikan pemanggil
            k = (k + key) % 100
            cipher = cipher + abjad[k]
        else:
            cipher = cipher + i
    return cipher

# Fungsi Dekripsi 
def dekripsi(cipher) :
    global abjad # untuk memanggil variable secara umum 
    key = int(input('Masukkan key : '))
    pesan = '' # untuk menampilkan pesan dekripsi sesuai kaidah caesar cipher
    for i in cipher:
        if i in cipher:
            k = abjad.find(i)
            k = (k - key) % 100
            pesan = pesan + abjad[k]
        else:
            pesan = pesan + i
    return pesan

# Bagian Menu Pilihan
if __name__ == '__main__':
    print('======================================================================')
    print('                        PROGRAM CAESAR CIPTHER                        ')
    print('======================================================================')

pilih = 'Y'
while (pilih == 'Y'):
    print("Silahkan Pilih Option Yang Tersedia  : ")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Stop")

    menu = input("Option yang di pilih adalah : ")
    print('======================================================================')

    if menu == '1':
        pesan = input('Input Pesan (Plain Text) : ')
        print(enkripsi(pesan))

    elif menu == '2':
        cipher = input('Input Pesan Enkripsi (Cipher Text) : ')
        print(dekripsi(cipher))

    elif menu == '3':
        print("Program Telah Selesai, Thankyou!")
        break
    else:
        print("NOT FOUND 402...")

    print('======================================================================')
    pilih = input('Apakah anda ingin melanjutkan? Input Y, Jika Tidak Input T) : ')
    print('======================================================================')
 
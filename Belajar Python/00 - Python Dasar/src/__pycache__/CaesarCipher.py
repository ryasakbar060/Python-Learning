import string
abjad = string.printable

def enkripsi(pesan) :
    global abjad # untuk memanggil variable
    key = int(input('Masukkan Key : '))
    cipher = '' # untuk menampilkan chiper enkripsi
    for i in pesan:
        if i in abjad:
            k = abjad.find(i) # untuk menentukan variable sebelumnya yang telah di jadikan pemanggil
            k = (k + key) % 100
            cipher = cipher + abjad[k]
        else:
            cipher = cipher + i
    return cipher

def dekripsi(cipher) :
    global abjad # untuk memanggil variable
    key = int(input('Masukkan key : '))
    pesan = '' # untuk menampilkan pesan dekripsi
    for i in cipher:
        if i in cipher:
            k = abjad.find(i)
            k = (k - key) % 100
            pesan = pesan + abjad[k]
        else:
            pesan = pesan + i
    return pesan

if __name__ == '__main__':
    print('==============================================')
    print('                 PILIH OPTION               ')
    print('==============================================')
    option = int(input('1. Enkripsi\n2. Dekripsi\n3. Stop\n\nSilahkan Pilih Opsi : '))
    print('==============================================')
    if option == 1:
        pesan = input('Input Pesan (Plain Text) : ')
        print(enkripsi(pesan))
    elif option == 2:
        cipher = input('Input Pesan  (Cipher Text) : ')
        print(dekripsi(cipher))
    elif option == 3:
        print('Program Telah Selesai')
    else:
        print('NOT FOUND 402...')
    print('==============================================')

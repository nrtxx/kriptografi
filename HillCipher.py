import numpy as np


def enkripsi(m):
    # hapus spasi
    m = m.replace(" ", "")

    # panggil fungsi buat_kunci untuk masukkan kunci
    C = buat_kunci()

    # tambahkan 0 jika pesan tidak dapat dibagi 2
    cek_pesan = len(m) % 2 == 0
    if not cek_pesan:
        m += "0"

    # buat matriks dari pesan
    P = buat_matriks(m)

    # hitung panjang pesan
    panjang_pesan = int(len(m) / 2)

    # hitung P * C
    en_m = ""
    for i in range(panjang_pesan):
        # lakukan operasi dot
        baris_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]

        # mod 26 dan tambah 65 untuk diubah kembali ke huruf dalam ascii
        integer = int(baris_0 % 26 + 65)
        en_m += chr(integer)

        # ulangi untuk kolom kedua
        baris_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(baris_1 % 26 + 65)
        en_m += chr(integer)
    return en_m


def cari_invers_perkalian(determinant):
    invers_perkalian = -1
    for i in range(26):
        invers = determinant * i
        if invers % 26 == 1:
            invers_perkalian = i
            break
    return invers_perkalian


def buat_kunci():
    # pastikan determinant relatif prima ke bilangan 26 dan hanya huruf
    determinant = 0
    C = None
    while True:
        #key = input("Masukkan 4 huruf key: ")
        key = "nrtv"
        C = buat_matriks(key)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        invers_elemen = cari_invers_perkalian(determinant)
        if invers_elemen == 1:
            print("Determinant tidak relatif prima ke bilangan 26")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Hanya huruf yang diterima")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C


def buat_matriks(string):
    # ubah huruf ke angka lalu buat matriks
    integers = [chr_ke_int(c) for c in string]
    panjang = len(integers)
    M = np.zeros((2, int(panjang / 2)), dtype=np.int32)
    iterator = 0
    for kolom in range(int(panjang / 2)):
        for baris in range(2):
            M[baris][kolom] = integers[iterator]
            iterator += 1
    return M


def chr_ke_int(char):
    # uppercase char untuk mendapatkan nilai 65-90 dalam ascii tabel
    char = char.upper()
    # ubah char menjadi int dan kurangi 65 untuk mendapatkan nilai 0-25
    integer = ord(char) - 65
    return integer


if __name__ == "__main__":
    m = "satu sembilan satu nol dua dua empat delapan"
    en_m = enkripsi(m)
    print(en_m)
    print()

    m = "rangga nurta kusumah"
    en_m = enkripsi(m)
    print(en_m)
    print()

    m = "saya ganteng pak"
    en_m = enkripsi(m)
    print(en_m)
    print()

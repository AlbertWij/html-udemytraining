'''Buatlah sebuah program sapaan dalam notasi
pseudo-code, flowchart, dan python dengan spesifikasi sebagai berikut:
a. Tampilkan "siapa namamu" dilayar
b. Meminta pengguna memasukan namanya
c. Tampilkan tulisan "dikota apa kamu berkuliah?" di layar
d. Meminta pengguna memasukan nama kota tempatnya berkuliah
e. Tampilkan tulisan "kuliah dimana?" di layar
f. Meminta pengguna memasukan nama universitas tempatnya berkuliah
g. Tampilkan "masuk pakultas mana" dilayar
h. Meminta pengguna memasukan nama fakultas tempatnya berkuliah
i. Tampilkan sapaan berdasarkan inputan diatas
'''

nama = input("Masukan nama anda\t :")
kota = input("Masukan kota dimana kamu berkuliah\t :")
univ = input("Masukan universitas mana kamu berkuliah\t :")
fakul = input("Masukan fakultas apa yang anda pilih\t :")
print("Halo {}"  "dari {}"  "berkuliah di {}"  "dari fakultas {}".format(nama,kota,univ,fakul))



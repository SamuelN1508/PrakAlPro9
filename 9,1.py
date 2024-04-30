# List yang dicek
list1 = [1,2,3,4,5,6,6,7,7,7,8,8,9,10,0]

# List kosong
list2 = []

# Sortir list besar ke kecil
list1.sort(reverse=True)

# Looping untuk setiap angka di list untuk menghindari angka sama
for i in list1:
    # Jika angka yang dilooping tidak ada di dalam list2
    if i not in list2:
        # Maka akan ditambah ke list2
        list2.append(i)
    
# Print Jawaban
print(f'Terbesar 1 = {list2[0]}')
print(f'Terbesar 2 = {list2[1]}')
print(f'Terbesar 3 = {list2[2]}')


# angka2 = [1]
# angka = ['0', '1', '2', '3', '4', '5']
# print(angka[-4:-1]) 

# # # List
# kata_benda = ['mobil', 'bola', 'pohon', 'sendok']
# kata_kerja = ['kerja', 'cuci', 'masak', 'makan']

# # Menambahkan 'motor ke list kata_benda
# kata_benda.append('motor')

# # Menghilangkan 'mobil' dari list kata_benda
# kata_benda.remove('mobil')

# # Menambah kata_benda[1] yaitu 'pohon' le list kata_kerja
# kata_kerja.append(kata_benda[1])

# # # Menggabungkan dua list
# kata = kata_benda + kata_kerja
# print(kata)

# # Menghitung jumlah elemen dalam list
# count = len(kata)

# print(kata_benda)
# print(kata_kerja)
# print(kata)
# print(count)

# Mengubah string menjadi list karakter
# kalimat = "saya lapar"
# list = list(kalimat)
# print(list)

# # Menggunakan fungsi split pada string akan memecahkan string tersebut menjadi kata-kata (default pemisah = spasi)
# kalimat = "saya senang"
# list = kalimat.split()
# print(list)

# kalimat = "saya-kenyang-maka-saya-senang"
# list = kalimat.split("-")
# print(list)

# # Mengubah kata dalam list menjadi string menggunakan fungsi join
# list = ['saya', 'senang', '!=', 'saya', 'kenyang']
# print(' '.join(list))

# # Mengubah isi list menggunakan list lain yang sama
# x = [0,1,2,3]
# y = x
# print(x is y)
# y[0] = -1
# print(x)

# # Code diatas tidak akan berfungsi jika kedua list sudah terbuat secara berbeda (walaupun memiliki isi yang sama)
# x = [0,1,2,3]
# y = [0,1,2,3]
# print(x is y)
# y[0] = -1
# print(x)

# Fungsi append untuk list
# x = [0,1,2,3]
# y = x.append(4)
# z = x + [5]
# print(x)
# print(y)
# print(z)

# Kita juga bisa menggunakan def untuk memodifikasi list
# def tambah(list):
#     list.append(10)
#     return list

# x = [0,1,2,3]
# y = tambah(x)

# print(y)
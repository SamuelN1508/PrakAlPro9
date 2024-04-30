import string

# List berisi alfabet
alfabet = list(string.ascii_letters) + list(string.ascii_uppercase)

# x True
x = True

# List Kosong
list = []

# Looping berhenti ketika x = False
while x == True:
    # Meminta input
    y = input("Masukan data: ")
    
    # Jika input = "done"
    if y == "done":
        # x akan menjadi false dan loop akan berhenti
        x = False
        
    # Jika input bukan angka
    elif y in alfabet:
        print("Masukan angka")
    
    else:
        # Mengubah y(string) menjadi y(integer)
        y = int(y)
        # Memasukan data ke list kosong
        list.append(y)
        
# Mencari nilai terbesar
terbesar = max(list)

# Mencari nilai terkecil
terkecil = min(list)

# Print jawaban
print(terbesar)
print(terkecil)

        
# Membuka berita.txt
with open("berita.txt", "r", encoding="utf8") as file:
    # Membaca isi file sebagai string
    berita = file.read()
    print("=======ISI BERITA=======")
    
    # Print berita awal
    print(berita)
    
    # Menutup file
    file.close()
    
with open("berita.txt", "r", encoding="utf8") as file:
    # Membaca isi file sebagai list
    data = file.readlines()
    
    # List kata unik kosong
    kata = []
    
    # Looping setiap baris
    for line in data:
        # Mempisahkan setiap kata dalam baris
        word = line.split()
        
        for unik in word:
            # Jika kata tidak ada di list
            if unik not in kata:
                # Akan dimasukan ke list kata unik
                kata.append(unik)
    
    print("=======Kata Unik pada Berita=======")
    print(kata)
    
        

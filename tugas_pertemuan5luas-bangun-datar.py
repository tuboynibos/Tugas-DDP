kata = '''Hallo selamat datang di aplikasi menghitung
masukkan pilihan :
1. menghitung luas persegi 
2. menghitung luas lingkaran
3. menghitung luas segitiga
Silahkan pilih diantara 3 soal di atas 
'''
pilihan = input (kata)

match pilihan:
    case "1":
        print("kamu memilih nomor 1 untuk menghitung luas persegi")
        sisi = int(input("masukka sisi ?"))
        luasP = sisi * sisi
        print ("luas persegi yang sisinya", sisi, "dan luasnya", luasP)
    case "2":
        print("kamu memilih nomor 2 untuk menghitung luas lingkaran")
        jari2 = float(input("masukkan jari-jari"))
        luasL = 3.14*jari2*jari2
        print("luas lingkaran yang jari-jarinya ")
    case "3":
        print("kamu memilih nomor 3 untuk menghitung luas segitiga")
        alas =int(input("masukkan alas"))
        tinggi =int(input("masukkan tinggi"))
        luasS =0.5 * alas * tinggi
        print("luas segitiga yang alasnya ", alas,"yang luasnya", luasS) 
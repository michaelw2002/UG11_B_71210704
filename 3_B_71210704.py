nama = str(input("Masukkan kalimat awal: "))
sisipan = str(input("Masukkan kata untuk disisipkan: "))
index = int(input("Masukkan index: "))

def sisip():
    Hasil = nama[:index] + sisipan + nama[index:]
    print(Hasil)
sisip()

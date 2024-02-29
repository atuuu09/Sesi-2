#menentukan tahun kabisat
tahun = int (input("Masukan Tahun:"))
if tahun %4 ==0:
    hasil = "Merupakan Tahun Kabisat"
else:
    hasil = "Bukan Tahun Kabisat"

print(hasil)
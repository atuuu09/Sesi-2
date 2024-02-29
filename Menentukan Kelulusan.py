nilai_inggis= int (input("Masukan nilai inggris anda:"))
nilai_mtk = int (input("Masukan nilai mtk anda:"))
nilai_indonesia = int (input("Masukan nilai indonesia anda:"))
nilai_ipa = int (input("Masukan nilai ipa anda:"))
nilai_ips = int (input("Masukan niali ips anda:"))

if (nilai_inggis + nilai_mtk + nilai_indonesia) /3 >=75:
    hasil = "lulus"
elif (nilai_inggis + nilai_mtk + nilai_indonesia + nilai_ipa + nilai_ips) /5 >=70:
    hasil = "lulus"
elif (nilai_inggis + nilai_mtk) /2 >90:
    hasil = "lulus"
else:
    hasil = "tidak lulus"
    
print("Anda dinyatakan" , hasil)
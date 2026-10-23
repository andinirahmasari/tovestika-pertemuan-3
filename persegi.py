
s = int(input("sisi: "))
andin = {
    "keliling" : 4*s,
    "luas" : s*s
}
pilihan = input("keliling/luas: ")
print(andin.get(pilihan, 'Oops, hanya bisa input "luas" atau "keliling". Periksa kembali input-an Anda'))



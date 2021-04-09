print("PROGRAM UNTUK MENGHITUNG NILAI RATA-RATA")

n = int(input("Masukkan banyaknya data yang diinginkan : "))
ke = 0
jumlah = 0
total = []

for i in range(n):
    ke += 1
    datake = int(input('Masukkan data ke %d : '%ke))
    total.append(datake)
    jumlah += total[i]
    ratarata = jumlah / n
print('Rata-rata dari ke %d data diatas adalah :'%ke,ratarata)
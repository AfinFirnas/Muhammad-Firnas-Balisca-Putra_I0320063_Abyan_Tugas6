print("Program mengecek apakah angka awal sampai akhir yang diinput adalah bilangan prima")

awal  = int(input('Masukkan angka awal(tidak boleh 1) : '))
akhir = int(input('Masukkan sampai ke berapa angka ingin di cek : '))
akhir += 1
print()
if awal > 1:
    for n in range(awal,akhir):
        for i in range(2,n):
            if (n % i) == 0:
                print(n, "bukan bilangan prima")
                break
        else:
            print(n, "adalah bilangan prima")
else:
    print("Data tidak valid")
    print('Silahkan masukkan angka lebih dari 1 pada angka awal!')
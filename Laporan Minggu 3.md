Laporan Project Akhir Praktikum Metode Komputasi Komputasi
Kelompok 7 : 
1. Satriya Putra Bagaskara (21/477852/PA/20710)
2. Mohammad Affan Pramana (21/477406/PA/20658)
3. Gilang Kurnia Pandhudewanata (21/481528/PA/20968)
4. Dimas Dhanurdoro Danisworo (21/480216/PA/20850)
5. Shofi Mictahul Jannah (21/482010/PA/21008)
6. Eka Akbar Permatasari (21/475313/PA/20567)

-----------------------------------------------------------------------
Minggu Ketiga

Pada minggu ketiga, kelompok 7 melakukan optimasi terhadap main core yang akan digunakan untuk menghitung nilai total resistansi. Setelah core program dirasa sudah optimal. Kemudian akan dikembangkan GUI yang akan membuat main core dapat berjalan

Berikut merupakan main core yang sudah dioptimalisasi sekitar 82,5% : 

#import numpy as np
#a=np.array([a1],[a2],[a3])
#cara masukin setiap blok tipe rangkaian dan besar resistor ke array tersebut gimana?
#nek udah masuk, tinggal dipangil pakai print(a)

#dibawah ini udah, outputnya masih berupa array satu dimensi
#a=[]
#for i in range (3):
#    m=str(input("Tipe rangkaian, input p untuk rangkaian pararel atau input s untuk rangkaian seri:"))
#    n=int(input("Number of elements in array:"))
#    for i in range(0,n):
#        z =int(input())
#        a.append(z)
#print(a)

#dibawa ini array nya baru 1 jadi loopnya cuma 1 padahal yang diminta loopnya ada 3
a=[]
n=int(input("Number of elements in array:"))
for i in range(0,n):
   z =int(input())
   a.append(z)
print(a)
m=str(input("Tipe rangkaian, input p untuk rangkaian pararel atau input s untuk rangkaian seri:"))

#benerin def def biar outpunya bener abis itu inputnya diubah jadi array multidimensi seperti comment di atas
def tipe_par(p):
    #kalau p = m == 'p'
    par_res_total = 0
    par_count = 0
    while par_count < len(a):
        try:
            par_res_nilai = len(a)
            par_res_total += 1/(par_res_nilai)
            par_count += 1
        except ValueError as e:
            print('Besar Resistor', e)
            continue
        print('Total resistensi paralel = {} Ohm'.format(par_res_total))
        return 
def tipe_seri(s):
    #kalau s = m == 's'
    #def ser_resistance (a):
    ser_res_total = 0
    ser_count = 0
            
    while ser_count < len(a)+2:
        try:
            ser_res_nilai = len(a)
            ser_res_total += ser_res_nilai
            ser_count += 1
        except ValueError as e:
            print('Besaran Resistor', e)
            continue
        print("Total resistansi seri= {} Ohm".format(ser_res_total))
        return 
print(m)
if m == 'p':
    tipe_par(len(a))
elif m == 's':
    tipe_seri(len(a))


Dari main core tersebut, didapatkan output sebagai berikut :

Number of elements in array:2
2
2
[2, 2]
Tipe rangkaian, input p untuk rangkaian pararel atau input s untuk rangkaian seri:p
p
Total resistensi paralel = 0.5 Ohm

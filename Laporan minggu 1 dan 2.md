Laporan Progress Project Akhir Praktikum Metode Komputasi
"
Kelompok 7 :
Anggota : 
1. Satriya Putra Bagaskara        (21/477852/PA/20710)
2. Mohammad Affan Pramana         (21/477406/PA/20658)
3. Gilang Kurnia Pandhudewanata   (21/481528/PA/20968)
4. Dimas Dhanurdoro Danisworo     (21/480216/PA/20850)
5. Shofi Mictahul Jannah          (21/482010/PA/21008)
6. Eka Akbar Permatasari          (21/475313/PA/20567)
----------------------------------------------------------------------------------------------------------------------------------------
Progress Minggu ke-1

Pada minggu pertama dilakukan pembagian kelompok oleh asisten serta pendamping kelompok. Asisten pendamping dari kelompok 7 adalah Mbak Tresya. Setelah dilakukan pembagian kelompok kemudian dilakukan pembagian persoalan final project yang akan dikerjakan oleh masing-masing kelompok. Kelompok 7 mendapatkan tema yaitu menghitung nilai resistansi total dari sejumlah resistor yang diinputkan dalam bentuk rangkaian seri dan paralel.
Kemudian kami melakukan pembagian jobdesc awal untuk mempersiapkan pembuatan main core pada pertemuan ke-2. Jobdesk awal ialah menghimpun referensi dari berbagai sumber yang berkaitan dengan tema tersebut.
----------------------------------------------------------------------------------------------------------------------------------------
Progress Minggu ke-2

Pada minggu ke-2 kelompok 7 membuat main core yang akan digunakan untuk software yang akan di develop guna menyelesaikan persoalan yang diberikan. Sebelum masuk ke main core, terlebih dahulu kami membuat diagram alir #algoritma# yang akan digunakan berdasarkan rumus fisika hukum ohm dan logika perhitungan matematis yang #telah dirancang# akan digunakan. Selanjutnya, #kemudian hal tersebut dituangkan dalam wujud code-code sebagai main core# dibuat coding untuk main core dari software yang akan di develop. Dalam proses penuangan code dan pembuatan diagram alir kami mengalami beberapa kendala beserta solusinya sebagai berikut:

Kendala Minggu 1 ke minggu 2
1. Input dari persoalan yang ada di ppt penugasan berupa arus, voltase, dan resistor sementara outputnya diminta berupa total resistansi padahal arusnya sudah diketahui, voltase dengan menggunakan hukum ohm dapat diperoleh resistansi lalu kenapa harus input resistansi juga ?;
solusi:
ternyata pada hari H progress presentasi, tedapat ralat dari tim asisten sehingga inputnya berupa resistor saja yang dirangkaikan dengan rangkaian yang sedemikian rupa dengan minimal terdiri dari tiga loop;

2. Dalam proses pembuatan diagram alir kami bingung akan menuangkan code nya mau seperti apa dan arah programmnya mau seperti apa karena kompleksnya rangkaian dalam hukum ohm dan memungkinkan berbagai posisi resistor sehingga kami membutuhkan batasan masalah;
solusi: pada sorenya sebelum hari h presentasi 1, kami menemui Mbak Tresya untuk berkonsultasi mengenai batasan masalah yang ada sehingga dari diskusi tersebut diperoleh bahwa posisi rangkain hanya berupa berapa resistor pada posisi seri dan berapa resistor pada posisi paralel.

3. Setelah kami berhasil menuangkan wujud core program dalam bentuk code dengan perkembangan sedikit dari core tersebut, code dapat berjalan dengan baik namun belum seutuhnya efektif karena ada beberapa code yang strukturnya kurang rapi sehingga perlu perbaikan dari code tersebut ditambah dengan adanya perubahan dari output dan algoritma program seperti yang terpaparkan di atas maka kami perlu mengadakan perubahan pada input program dan algoritma program yang telah dibuat.

Berikut adalah main core awal kelompok kami.  

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def resistansi_total(rp1, rp2, rp3, rs1, rs2, rs3):
    """Mencari Resistansi Total Rangkaian Seri Paralel """

    resistansi_total = (1/(1/rp1 + 1/rp2 + 1/rp3)) + rs1 + rs2 + rs3

    return resistansi_total

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Kemudian, kami melakukan beberapa penyesuaian pada main core kami, sehingga script dari main core kami menjadi seperti di bawah ini.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#deklarasi input

print('Selamat Datang di Program Sini Sama OHM')
V = input('Input tegangan dalam Volt: ')
I = input('Input arus dalam Ampere: ')
R = int(input('pesan jumlah resistor dalam ohm: ')) #pesan array dengan jumlah elemen tertentu
y=list(map(str, input('Elemen Resistor (Rn, p atau s): ').strip().split())) #ini string

#deklarasi process dalam program

class semua():
    
    def resistance(array):
        if isinstance(array, int):
            return array
        else:
            if isinstance(array,list):
                temp = array
            else:
                temp = array.split(" ")
                i = 0
         while True:
            try:
                a = new_resistance(temp[i], temp[i+1], temp[i+2])
            except Exception as e:
                i += 1            
            if len(temp[i+3:]) == 0:
                return resistance(new_resistance(temp[i], temp[i+1], temp[i+2]))
            else:
                return resistance(temp[:i] + [new_resistance(temp[i], temp[i+1], temp[i+2])] + temp[i+3:])
        
    def tipe_rangkaian():
        if pararel==p:
            return(0)
        else:
            seri==s
            return (0)
        
    def R_total():
        if tipe_rangkaian==p:
            Rs_total=str(float(1/R1) + float(1/R2)+ float(1/R3)) 

        elif tipe_rangkaian==s:
            Rp_total=str(float(1/R1) + float(1/R2)+ float(1/R3)) 
            
        R1_total=Rs_total+Rp_total
        return R_total
    
    def hukumohm(self,V,I,y):
        self.V=V
        self.I=I
        self.y=y
        
        R2_total== str(float(V)/float(I))  
        return R2_total

R12=R1_total=R2_total=True

a=semua()

#deklarasi output

print (a.hukumohm(V,I,y))

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Dan output dari script di atas adalah sebagai berikut.

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

Selamat Datang di Program Sini Sama OHM
Input tegangan dalam Volt: 3
Input arus dalam Ampere: 1
pesan jumlah resistor dalam ohm: 8
Elemen Resistor (Rn, p atau s): 1 s 1 s 1 p 1 p 3 s
True

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

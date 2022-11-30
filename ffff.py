def ser_resistance (jumlah):
    ser_res_total = 0
    ser_res_besar = []
    ser_count = 0

    while ser_count < jumlah:
        try:
            ser_res_nilai=float(input('Masukkan Nilai Resistensi dalam Ohm : '))
            ser_res_besar.append(ser_res_nilai)
            ser_res_total += ser_res_nilai
            ser_count += 1

        except ValueError as e:
            print('Besaran Resistor', e)
            continue
    r=0
    for i in ser_res_besar:
        r+=i
    
    print("Total resistansi = {} Ohms".format(r))
    return

def par_resistance (jumlah):
    par_res_total = 0
    par_res_besar = []
    jum_par_res = 0
    par_count = 0

    while par_count < jumlah:
        try:
            par_res_nilai = int(input('Masukkan Nilai Resistensi dalam Ohm :'))
            par_res_besar.append(par_res_nilai)
            par_count += 1
        
        except ValueError as e:
            print('Besar Resistor', e)
            continue
    r=0
    for i in par_res_besar:
        r+=1/i

    rfix=r**(-1)
        

    print('Total resistensi = {} Ohms'.format(rfix))
    return

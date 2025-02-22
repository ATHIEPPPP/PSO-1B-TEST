import random
import math

# Fungsi X
def func(x):
    return (-5*math.exp(-x**2))

# Inisialisasi variabel xi awal untuk iterasi pertama
xi = {
    "x1" : random.uniform(0,3),
    "x2" : random.uniform(0,3),
    "x3" : random.uniform(0,3),
    "x4" : random.uniform(0,3),
    "x5" : random.uniform(0,3),
    "x6" : random.uniform(0,3),
    "x7" : random.uniform(0,3),
    "x8" : random.uniform(0,3),
    "x9" : random.uniform(0,3),
    "x10": random.uniform(0,3)
}

# Inisialisasi penampungan variabel xi-1 untuk perbandingan mencari Pbestix
xi_before={
    "x1" : 0,
    "x2" : 0,
    "x3" : 0,
    "x4" : 0,
    "x5" : 0,
    "x6" : 0,
    "x7" : 0,
    "x8" : 0,
    "x9" : 0,
    "x10": 0
}

# Inisialisasi vo
v0 = 0

# Inisialisasi vi setelah terjadi iterasi
vi = {
    "v1":v0,
    "v2":v0,
    "v3":v0,
    "v4":v0,
    "v5":v0,
    "v6":v0,
    "v7":v0,
    "v8":v0,
    "v9":v0,
    "v10":v0
}

# Inisialisasi variabel-variabel lainnya
c1 = 1
c2 = 1/2
r1 = random.randint(0,1)
r2 = random.randint(0,1)
w = 1
Gbest = 0
Pbesti = []

#fungsi untuk mencari Gbest
def x_minimum(*args):
    global Gbest
    Gbest = min(args, key=func)

# Fungsi untuk yang akan mengambil langsung nilai xi dan menympannya kedalam array Pbesti jika sedang dalam iterasi pertama
def fx_minimum_iterasi1(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):
    Pbesti.append(x1)
    Pbesti.append(x2)
    Pbesti.append(x3)
    Pbesti.append(x4)
    Pbesti.append(x5)
    Pbesti.append(x6)
    Pbesti.append(x7)
    Pbesti.append(x8)
    Pbesti.append(x9)
    Pbesti.append(x10)

# Fungsi untuk mengambil nilai xi dan menyimpannya kedalam Pbesti dengan cara membandikan antara nilai fungsi f(x) iterasi sekarang dengan iterasi sebelumnya
def fx_minimum_selanjutnya(x1_before,x1,x2_before,x2,x3_before,x3,x4_before,x4,x5_before,x5,x6_before,x6,x7_before,x7,x8_before,x8,x9_before,x9,x10_before,x10):
    if func(x1)<=func(x1_before):
        Pbesti.append(x1)
    else :
        Pbesti.append(x1_before)
    if func(x2)<=func(x2_before):
        Pbesti.append(x2)
    else :
        Pbesti.append(x2_before)
    if func(x3)<=func(x3_before):
        Pbesti.append(x3)
    else :
        Pbesti.append(x3_before)
    if func(x4)<=func(x4_before):
        Pbesti.append(x4)
    else :
        Pbesti.append(x4_before)
    if func(x4)<=func(x4_before):
        Pbesti.append(x4)
    else :
        Pbesti.append(x4_before)
    if func(x5)<=func(x5_before):
        Pbesti.append(x5)
    else :
        Pbesti.append(x5_before)
    if func(x6)<=func(x6_before):
        Pbesti.append(x6)
    else :
        Pbesti.append(x6_before)
    if func(x7)<=func(x7_before):
        Pbesti.append(x7)
    else :
        Pbesti.append(x7_before)
    if func(x8)<=func(x8_before):
        Pbesti.append(x8)
    else :
        Pbesti.append(x8_before)
    if func(x9)<=func(x9_before):
        Pbesti.append(x9)
    else :
        Pbesti.append(x9_before)
    if func(x10)<=func(x10_before):
        Pbesti.append(x10)
    else :
        Pbesti.append(x10_before)

# Fungsi untuk mencari nilai vi
def vi_func(vimin1,xi,i):
    return (w * vimin1)+(c1*r1*((Pbesti[i]) - xi))+(c2*r2*((Gbest) - xi))

n = int(input("\033[92m"+f"Masukan Jumlah Iterasi :"+"\033[0m"))
print()

# Looping berdasarakan jumlah iterasi yang diinginkan
for index in range(n) :
    print("\033[92m"+f"iterasi ke-{index+1}"+"\033[0m")
    print(f"nilai (x1): {xi['x1']}")
    print(f"nilai (x2): {xi['x2']}")
    print(f"nilai (x3): {xi['x3']}")
    print(f"nilai (x4): {xi['x4']}")
    print(f"nilai (x5): {xi['x5']}")
    print(f"nilai (x6): {xi['x6']}")
    print(f"nilai (x7): {xi['x7']}")
    print(f"nilai (x8): {xi['x8']}")
    print(f"nilai (x9): {xi['x9']}")
    print(f"nilai (x10): {xi['x10']}")
    print()
    print(f"nilai f(x1): {func(xi['x1'])}")
    print(f"nilai f(x2): {func(xi['x2'])}")
    print(f"nilai f(x3): {func(xi['x3'])}")
    print(f"nilai f(x4): {func(xi['x4'])}")
    print(f"nilai f(x5): {func(xi['x5'])}")
    print(f"nilai f(x6): {func(xi['x6'])}")
    print(f"nilai f(x7): {func(xi['x7'])}")
    print(f"nilai f(x8): {func(xi['x8'])}")
    print(f"nilai f(x9): {func(xi['x9'])}")
    print(f"nilai f(x10): {func(xi['x10'])}")
    print()
    print(f"Nilai Gbest: {Gbest}")
    print(f"Nilai Minimum f(x): {func(Gbest)}")
    print()
    
    # Pengosongan array Pbesti
    Pbesti.clear()

   
    
    # Kondisional statetement yang mana jika index nya sama dengan 0 fungsi fx_minimum_iterasi1 akan dijalankan jika tidak terpenuhi fx_minimum_selanjutnya yang dijalankan
    if index == 0 :
        fx_minimum_iterasi1(xi["x1"],xi["x2"],xi["x3"],xi["x4"],xi["x5"],xi["x6"],xi["x7"],xi["x8"],xi["x9"],xi["x10"])
    else:
        fx_minimum_selanjutnya(xi_before["x1"],xi["x1"],xi_before["x2"],xi["x2"],xi_before["x3"],xi["x3"],xi_before["x4"],xi["x4"],xi_before["x5"],xi["x5"],xi_before["x6"],xi["x6"],xi_before["x7"],xi["x7"],xi_before["x8"],xi["x8"],xi_before["x9"],xi["x9"],xi_before["x10"],xi["x10"])

    
    # Memanggil fungsi x_minimum
    x_minimum(Pbesti[0],Pbesti[1],Pbesti[2],Pbesti[3],Pbesti[4],Pbesti[5],Pbesti[6],Pbesti[7],Pbesti[8],Pbesti[9])

    # Update nilai vi berdasarkan fungsi vi_func
    vi["v1"]= vi_func(vi["v1"],xi["x1"],0)
    vi["v2"] = vi_func(vi["v2"],xi["x2"],1)
    vi["v3"] = vi_func(vi["v3"],xi["x3"],2)
    vi["v4"]= vi_func(vi["v4"],xi["x4"],3)
    vi["v5"] = vi_func(vi["v5"],xi["x5"],4)
    vi["v6"] = vi_func(vi["v6"],xi["x6"],5)
    vi["v7"]= vi_func(vi["v7"],xi["x7"],6)
    vi["v8"] = vi_func(vi["v8"],xi["x8"],7)
    vi["v9"] = vi_func(vi["v9"],xi["x9"],8)
    vi["v10"] = vi_func(vi["v10"],xi["x10"],9)

    # Update nilai xi penampungan (xi_before) dengan nilai dari xi iterasi sekarang
    xi_before["x1"] = xi["x1"]
    xi_before["x2"] = xi["x2"]
    xi_before["x3"] = xi["x3"]
    xi_before["x4"] = xi["x4"]
    xi_before["x5"] = xi["x5"]
    xi_before["x6"] = xi["x6"]
    xi_before["x7"] = xi["x7"]
    xi_before["x8"] = xi["x2"]
    xi_before["x9"] = xi["x9"]
    xi_before["x10"] = xi["x10"]

    # Update nilai dari xi iterasi sekarang
    xi["x1"] = xi_before["x1"] + vi["v1"]
    xi["x2"] = xi_before["x2"] + vi["v2"]
    xi["x3"] = xi_before["x3"] + vi["v3"]
    xi["x4"] = xi_before["x4"] + vi["v4"]
    xi["x5"] = xi_before["x5"] + vi["v5"]
    xi["x6"] = xi_before["x6"] + vi["v6"]
    xi["x7"] = xi_before["x7"] + vi["v7"]
    xi["x8"] = xi_before["x8"] + vi["v8"]
    xi["x9"] = xi_before["x9"] + vi["v9"]
    xi["x10"] = xi_before["x10"] + vi["v10"]
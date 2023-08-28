# membuat waktu PROGRAM 5

jumlah_sekon = int(input("masukkan jumlah sekon = "))
detik_sehari = 60*60*24

# MENCARI JUMLAH HARI
hari = jumlah_sekon // detik_sehari

# MENCARI JAM 
sisa_detik = jumlah_sekon - (hari*detik_sehari)
jam = sisa_detik // (60*60)

# MENCARI MENIT
sisa_detik = sisa_detik - jam*(60*60)
menit = sisa_detik//60

# MENCARI DETIK
detik = sisa_detik % 60

# print(f"{hari} hari, {jam} jam, {menit} menit, {detik} detik")

my_set = {1,2,3,'python',(5,6,7)}
print(my_set)
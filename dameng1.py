nama=raw_input("masukkan nama mahasiswa    :")
matakuliah=raw_input("mata kuliah    :")
presensi=input("masukkan nilai presensi    :")
tugas=input("masukkan nilai tugas    :")
uts=input("masukan nilai uts    :")
uas=input("masukan nilai uas    :")

presensi=presensi*5/100;
tugas=tugas*40/100;
uts=uts*30/100;
presensi=presensi*25/100;

nilai_akhir=presensi+tugas+uts+uas;

printf"\nNama   : %s"%nama
printf"mata kuliah   : %s"%matakuliah
printf"presensi   : %d"%presensi
printf"tugas   : %d"%tugas
printf"uts   : %d"%uts
printf"uas   : %d"%uas
printf"nilai akhir   : %d",float(nilai_akhir)

if nilai_akhir >= 85:
    print "n\nilai huruf : a"
elif nilai_akhir >= 70:
    print "n\nilai huruf : b"
elif nilai_akhir >= 50:
    print "n\nilai huruf : c"
elif nilai_akhir >= 30:
    print "n\nilai huruf : d"
elif nilai_akhir >= 0:
    print "n\nilai huruf : d"


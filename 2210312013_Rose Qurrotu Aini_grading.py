print("Autorized By : Rose Qurrotu")

print("MENGHITUNG DAN MEMASUKKAN NILAI MAHASISWA")

user_name1 = "Rosie"
pass_word1 = "fullsun00"

print("Masukan username dan password:")
user_name = input("Username:")
pass_word = input("Password:")

if user_name == user_name1 and pass_word == pass_word1:
    print("Status Login = Active")
    
    print("Hallo " + user_name)

    nama = input("Masukkan Nama Mahasiswa :")
    matkul = input("Masukkan Mata Kuliah :")
    nilai_presentasi = float(input("Masukkan nilai Presensi :"))
    nilai_tugas = float(input("Masukkan nilai Tugas :"))
    nilai_uts = float(input("Masukkan nilai UTS :"))
    nilai_uas = float(input("Masukkan nilai UAS :"))

    def na(nilai_presentasi, nilai_tugas, nilai_uts, nilai_uas):
        total_nilai = (0.05 * nilai_presensi) + (0.1 * nilai_tugas) + (0.30 * nilai_tugas) + (0.25 * nilai_uts) + (0.30 * nilai_uas)
        if 100 >= total_nilai >= 85 :
            print("A")
        elif total_nilai >= 70 :
            print("B")
        elif total_nilai >= 50 :
            print("C")
        elif total_nilai >= 30 :
            print("D")
        elif total_nilai <= 30 :
            print("E")
    
    a = nama
    b = (na(nilai_presensi, nilai_tugas, nilai_uts, nilai_uas))
    c = matkul
    total_nilai = (0.05 * nilai_presensi) + (0.1 * nilai_tugas) + (0.30 * nilai_tugas) + (0.25 * nilai_uts) + (0.30 * nilai_uas)
    print ("Mahasiswa", a, "mendapatkan nilai", b, "untuk Mata Kuliah", c, "dengan skor total", total_nilai)
else:
    print ("status error,<br/>")

#OUTPUT:

#Masukan username dan password: 
#Username:Rosie
#Password:fullsun00
#Status Login = Active
#Hallo Rosie
#Masukkan Nama Mahasiswa : Rose Qurrotu Aini
#Masukkan Mata Kuliah : LPP
#Masukkan nilai Presensi : 100.0
#Masukkan nilai Tugas : 100.0
#Masukkan nilai UTS : 100.0
#Masukkan nilai UAS : 100.0
#Mahasiswa Rose Qurrotu Aini mendapatkan nilai A untuk Mata Kuliah LPP dengan skor total 100.0

#Jika login gagal:
#Masukan username dan password: 
#Username:Rosie
#Password:sukakacang
#status error,<br/>
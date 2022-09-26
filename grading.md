uname_masuk = 'Rachel Araya '
password_masuk = 'Ra23704'

print("Masukkan Username dan Password :")
user_name_Rachel= input('Username :')
password_Rachel = input('Password : ')
print("\n")

if uname_masuk == user_name_Rachel and password_masuk == password_Rachel :
    print('status_login = active')
    print('Halo ' + username_1)
    print('Nama mata kuliah:')
    print('Masukkan nama mahasiswa yang akan di grading:')

    Nilai_presensi= input('Silahkan Masukkan nilai Presensi :') 
    Nilai_tugas = input('Silahkan Masukkan nilai Tugas :')
    Nilai_uts = input('Silahkan Masukkan Nilai UTS :')
    Nilai_uas = input('Silahkan Masukkan Nilai UAS :')

    def rata_rata_nilai(Nilai_presensi_, Nilai_tugas, Nilai_uts, Nilai_uas) :
        total_nilai = 0.05 * float(Nilai_Presensi) + 0.1 * float(Nilai_Tugas) + 0.30 * float(Nilai_Tugas) + 0.25 * float(Nilai_UTS) + 0.30 * float(Nilai_UAS)

        if 100 <= total_nilai >= 85 :
            return "A"
        if total_nilai >= 70 :
            return "B"
        if total_nilai >= 50 :
            return "C"
        if total_nilai >= 30 :
            return "D"
        else :
            return "E"
    
    X = nama_mahasiswa_yang_digrading
    Y = rata_rata_nilai(Nilai_presensi_Nilai_tugas, Nilai_uts, Nilai_uas)
    Z = nama_matkul

    print('Mahasiswa', X, "Mendapatkan", Y, "Untuk mata kuliah", Z, "dengan mata kuliah", total_nilai)
else :
    print('Error 404')

#OUTPUT
#Username :Rachel Araya
#Password :Ra23704


#satus login = active
#Halo Rachel Araya


#Masukkan Nama Mahasiswa yang akan di grading : Rachel Araya
#Nama Mata Kuliah : Logika Pemograman dan praktikum
#Silahkan Masukkan nilai Presensi : 100
#Silahkan Masukkan nilai Tugas : 100
#Silahkan Masukkan nilai UTS : 100
#Silahkan Masukkan nilai UAS : 100


#Mahasiswa Rachel Araya mendapatkan nilai A untuk Mata Kuliah Logika Pemogramman  dengan skor total 100
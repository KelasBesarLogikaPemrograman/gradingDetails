username_1 = "dicky"
password_1 = "sooyaaa"

print ("please insert your username and password to login:")
user_name = input("Username :")
pass_word = input("Password :")
print ("\n")

if user_name == username_1 and pass_word == password_1 :
    print ("Status Login = Active")
    print ("Hallo, " + user_name)
    print ("\n")
    nama_mahasiswa = input("Masukkan Nama Mahasiswa yang akan di grading : ")
    nama_matkul = input("Nama Mata Kuliah : ")
    Nilai_Presensi = input("Silahkan Masukkan nilai Presensi : ")
    Nilai_Tugas = input("Silahkan Masukkan nilai Tugas : ")
    Nilai_UTS = input("Silahkan Masukkan nilai UTS : ")
    Nilai_UAS = input("Silahkan Masukkan nilai UAS : ")
    def rata_rata_nilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS):
        total_nilai = 0.05 * float(Nilai_Presensi) + 0.1 * float(Nilai_Tugas) + 0.30 * float(Nilai_Tugas) + 0.25 * float(Nilai_UTS) + 0.30 * float(Nilai_UAS)
        if 100 >= total_nilai >= 85 :
            return "A"
        if total_nilai >= 70 :
            return "B"
        if total_nilai >= 50 :
            return "C"
        if total_nilai >= 30 :
            return "D"
        else :
            return "E"
    X = nama_mahasiswa
    Y = (rata_rata_nilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS))
    Z = nama_matkul
    total_nilai = (0.05 * float(Nilai_Presensi) + 0.1 * float(Nilai_Tugas) + 0.30 * float(Nilai_Tugas) + 0.25 * float(Nilai_UTS) + 0.30 * float(Nilai_UAS))
    print ("\n")
    print ("Mahasiswa", X, "mendapatkan nilai", Y, "untuk Mata Kuliah", Z, "dengan skor total", total_nilai)
else :
    print ("your username or password is wrong, please try again")

#OUTPUT
#please insert your username and password to login:
#Username :dicky
#Password :sooyaaa


#Status Login = Active
#Hallo, dicky


#Masukkan Nama Mahasiswa yang akan di grading : dicky dwi saputra
#Nama Mata Kuliah : Logika Pemogramman  
#Silahkan Masukkan nilai Presensi : 98
#Silahkan Masukkan nilai Tugas : 98
#Silahkan Masukkan nilai UTS : 98
#Silahkan Masukkan nilai UAS : 98


#Mahasiswa dicky dwi saputra mendapatkan nilai A untuk Mata Kuliah Logika Pemogramman  dengan skor total 98.0

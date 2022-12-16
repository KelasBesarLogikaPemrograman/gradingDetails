username1 = "Akmaluddin"
password1 = "Al Fikri"

print ("Tolong masukkan nama pengguna dan kata sandi anda!")
username = input("Nama Pengguna:")
print("Nama Pengguna:", username)
password = input("Kata sandi:")
print("Kata sandi:", password)
print("\n")

if username==username1 and password==password1:
    print("Status Login = Aktif")
    print("Halo,", username, "!")
    print("\n")
    Nama_Mahasiswa = input("Masukkan nama mahasiswa yang akan digrading :")
    print("Masukkan nama mahasiswa yang akan digrading :", Nama_Mahasiswa)
    Nama_MataKuliah = input("Nama mata kuliah :")
    print("Nama mata kuliah :", Nama_MataKuliah)
    Nilai_Presensi = input("Silakan masukkan nilai presensi :")
    print("Silakan masukkan nilai presensi :", Nilai_Presensi)
    Nilai_Tugas = input("Silakan masukkan nilai tugas :")
    print("Silakan masukkan nilai tugas :", Nilai_Tugas)
    Nilai_UTS = input("Silakan masukkan nilai UTS :")
    print("Silakan masukkan nilai UTS :", Nilai_UTS)
    Nilai_UAS = input("Silakan masukkan nilai UAS :")
    print("Silakan masukkan nilai UAS :", Nilai_UAS)
    def averageNilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS):
        totalnilai = (0.05*float(Nilai_Presensi)) + (0.1*float(Nilai_Tugas)) + (0.30*float(Nilai_Tugas)) + (0.25*float(Nilai_UTS)) + (0.30*float(Nilai_UAS))
        if 100 >= totalnilai >= 85:
            return "A"
        elif totalnilai >= 70 :
            return "B"
        elif totalnilai>= 50:
            return "C"
        elif totalnilai>= 30 :
            return "D"
        else :
            return "E"

    P = Nama_Mahasiswa
    Q = Nama_MataKuliah
    R = averageNilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS)
    totalnilai = (0.05*float(Nilai_Presensi)) + (0.1*float(Nilai_Tugas)) + (0.30*float(Nilai_Tugas)) + (0.25*float(Nilai_UTS)) + (0.30*float(Nilai_UAS))
    print("\n") 
    print ("Mahasiswa", P, "mendapatkan nilai", R, "untuk mata kuliah", Q, "dengan total nilai", totalnilai)

else :
    print("Ups,error!!!")

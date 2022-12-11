username1 = "Isyah Radiyya"
password1 = "Satuduatiga"

print("Silakan masukkan username dan password anda")
username = input("Username: ")
password = input("Password: ")
print("\n")

if username==username1 and password==password1:
    print("Status Login = Aktif")
    print("Halo,", username, "!")
    print("\n")
    Nama_Mahasiswa = input("Masukkan nama mahasiswa yang akan digrading :")
    Nama_MataKuliah = input("Nama mata kuliah :")
    Nilai_Presensi = input("Silakan masukkan nilai presensi :")
    Nilai_Tugas = input("Silakan masukkan nilai tugas :")
    Nilai_UTS = input("Silakan masukkan nilai UTS :")
    Nilai_UAS = input("Silakan masukkan nilai UAS :")
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
    K = Nama_Mahasiswa
    L = Nama_MataKuliah
    M = averageNilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS)
    totalnilai = (0.05*float(Nilai_Presensi)) + (0.1*float(Nilai_Tugas)) + (0.30*float(Nilai_Tugas)) + (0.25*float(Nilai_UTS)) + (0.30*float(Nilai_UAS))
    print("\n") 
    print ("Mahasiswa", K, "mendapatkan nilai", M, "untuk mata kuliah", L, "dengan total nilai", totalnilai)

else :
    print("Oops,error!!!")

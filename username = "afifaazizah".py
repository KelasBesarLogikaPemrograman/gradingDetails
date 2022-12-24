username = "afifaazizah"
password = "qwerty123"

print("Silakan masukkan id dan password anda!")

while True:
    nama_pengguna = input("ID: ")
    print("ID: ", nama_pengguna)
    kata_sandi = input("Password: ")
    print("Password: ", kata_sandi)
    if nama_pengguna not in (username) or kata_sandi not in (password):
        print("Wrong ID or password, try again.")
        continue
    else:
        print("Status Login = Active")
        break
print("\n")

print("Halo, ", nama_pengguna, "!")
print("\n")

Nama_Mahasiswa = input("Masukkan nama mahasiswa yang akan digrading: ")
print("Masukkan nama mahasiswa yang akan digrading: ", Nama_Mahasiswa)
Mata_Kuliah = input("Nama mata kuliah: ")
print("Nama mata kuliah: ", Mata_Kuliah)
Nilai_Presensi = int(input("Silakan masukkan nilai Presensi: "))
print("Silakan masukkan nilai Presensi: ", Nilai_Presensi)
Nilai_Tugas = int(input("Silakan masukkan nilai Tugas: "))
print("Silakan masukkan nilai Tugas: ", Nilai_Tugas)
Nilai_UTS = int(input("Silakan masukkan nilai UTS: "))
print("Silakan masukkan nilai UTS: ", Nilai_UTS)
Nilai_UAS = int(input("Silakan masukkan nilai UAS: "))
print("Silakan masukkan nilai UAS: ", Nilai_UAS)

def averageNilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS):
    total_nilai = (0.05*float(Nilai_Presensi)) + (0.1*float(Nilai_Tugas)) + (0.30*float(Nilai_Tugas)) + (0.25*float(Nilai_UTS)) + (0.30*float(Nilai_UAS))
    if 100 >= total_nilai >= 85:
        return "A"
    elif total_nilai >= 70:
        return "B"
    elif total_nilai>= 50:
        return "C"
    elif total_nilai>= 30:
        return "D"
    else:
        return "E"
P = Nama_Mahasiswa
Q = Mata_Kuliah
R = averageNilai(Nilai_Presensi, Nilai_Tugas, Nilai_UTS, Nilai_UAS)
total_nilai = (0.05*float(Nilai_Presensi)) + (0.1*float(Nilai_Tugas)) + (0.30*float(Nilai_Tugas)) + (0.25*float(Nilai_UTS)) + (0.30*float(Nilai_UAS))

print("\n")
print ("Mahasiswa", P, "mendapatkan nilai", R, "untuk mata kuliah", Q, "dengan total nilai", total_nilai)
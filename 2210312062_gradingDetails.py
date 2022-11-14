username = "widyarj"
password = "123abc"

print("masukkan username dan password anda")
user_name = input("username: ")
pass_word = input("password: ")
print("\n")

if username==user_name and password==pass_word:
    print("status_login = active")
    print("\n")
    print("Halo " + user_name + ",")
    nama = input("Masukkan Nama Mahasiswa yang akan di grading : ")
    matkul = input("Nama Mata Kuliah : ")
    nilai_presensi = input("Silahkan Masukkan nilai Presensi : ")
    nilai_tugas = input("Silahkan Masukkan nilai Tugas : ")
    nilai_UTS = input("Silahkan Masukkan Nilai UTS : ")
    nilai_UAS = input("Silahkan Masukkan Nilai UAS : ")
    def nilai(nilai_presensi, nilai_tugas, nilai_UTS, nilai_UAS):
        total_nilai = (0.05 * float(nilai_presensi)) + (0.1 * float(nilai_tugas)) + (0.30 * float(nilai_tugas)) + (0.25 * float(nilai_UTS)) + (0.30 * float(nilai_UAS))
        if 100 >= total_nilai >= 85:
            return "A"
        elif total_nilai >= 70 :
            return "B"
        elif total_nilai>= 50:
            return "C"
        elif total_nilai>= 30 :
            return "D"
        else :
            return "E"
    nilai_huruf = nilai(nilai_presensi, nilai_tugas, nilai_UTS, nilai_UAS)
    total_nilai = (0.05 * float(nilai_presensi)) + (0.1 * float(nilai_tugas)) + (0.30 * float(nilai_tugas)) + (0.25 * float(nilai_UTS)) + (0.30 * float(nilai_UAS))
    print (f"Mahasiswa {nama} telah mendapatkan nilai {nilai_huruf} untuk Mata Kuliah {matkul} dengan skor total {total_nilai}")    
else :
    print("error")
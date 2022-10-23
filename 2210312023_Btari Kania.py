user_name1 = "Btari Kania"
pass_word1 = "bpkaniae"

print ("Masukan username dan password: ")
user_name = input("Username:")
pass_word = input("Password:")

if user_name == user_name1 and pass_word == pass_word1:
    print ("Status Login = Active")
    
    print ("Hai " + user_name)
    
    nama_mahasiswa = input("Masukkan Nama Mahasiswa yang akan di grading : ")
    nama_mata_kuliah = input("Nama Mata Kuliah : ")
    nilai_presensi = input("Silahkan Masukkan nilai Presensi : ")
    nilai_tugas = input("Silahkan Masukkan nilai Tugas : ")
    nilai_UTS = input("Silahkan Masukkan nilai UTS : ")
    nilai_UAS = input("Silahkan Masukkan nilai UAS : ")
    def rata_rata_nilai(nilai_presensi, nilai_tugas, nilai_UTS, nilai_UAS): 
        total_nilai = 0.05 * float(nilai_presensi) + 0.1 * float(nilai_tugas) + 0.30 * float(nilai_tugas) + 0.25 * float(nilai_UTS) + 0.30 * float(nilai_UAS)
        if 100 >= total_nilai >= 85 :
            return ("A")
        if total_nilai >= 70 :
            return ("B")
        if total_nilai >= 50 :
            return ("C")
        if total_nilai >= 30 :
            return ("D")
        else :
            return ("E")

    p = nama_mahasiswa
    q = (rata_rata_nilai (nilai_presensi, nilai_tugas, nilai_UTS, nilai_UAS))
    r = nama_matkul
    total_nilai = 0.05 * float(nilai_presensi) + 0.1 * float(nilai_tugas) + 0.30 * float(nilai_tugas) + 0.25 * float(nilai_UTS) + 0.30 * float(nilai_UAS)
    print ("Mahasiswa", p, "mendapatkan nilai", q, "untuk Mata Kuliah",r, "dengan skor total", total_nilai)
else:
    print ("status error,<br/>")
    
#OUTPUT:

#Masukan username dan password: 
#Username:Btari Kania
#Password:bpkaniae
#Status Login = Active
#Hai Btari Kania
#Masukkan Nama Mahasiswa yang akan di grading : Btari Kania 
#Nama Mata Kuliah : LPP
#Silahkan Masukkan nilai Presensi : 100.0
#Silahkan Masukkan nilai Tugas : 100.0
#Silahkan Masukkan nilai UTS : 100.0
#Silahkan Masukkan nilai UAS : 100.0
#Mahasiswa Btari Kania mendapatkan nilai A untuk Mata Kuliah LPP dengan skor total 100.0

#Jika gagal login:
#Masukan username dan password: 
#Username:Btari Kania
#Password: bkaniaep
#status error,<br/>
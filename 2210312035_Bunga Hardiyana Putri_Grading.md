print ('Silakan Login Menggunakan Username dan Password yang Benar')
print ('---------------------')

username1 = "2210312035"
password1 = "ryujincantik"

username2 = input('masukkan username Anda : ')
password2 = input('masukkan password Anda : ')

if username1==username2 and password1==password2:
    print('------------------------------------------')
    print('status_login=active')
    print('Login berhasil. Halo '+ username1 + '')
    print('------------------------------------------')
    nama_mahasiswa = input("Masukkan Nama Mahasiswa yang akan di grading : ")
    mata_kuliah = input("Nama Mata Kuliah : ")
    nilai1 = input("Silahkan Masukkan nilai Presensi : ")
    nilai2 = input("Silahkan Masukkan nilai Tugas : ")
    nilai3 = input("Silahkan Masukkan Nilai UTS : ")
    nilai4 = input("Silahkan Masukkan Nilai UAS : ")

    return (nama_mahasiswa, mata_kuliah, nilai1, nilai2, nilai3, nilai4)

def hasil (nama_mahasiswa, mata_kuliah, nilai1, nilai2, nilai3, nilai4) :
    total_nilai = (0.05 * nilai1) + (0.1 * nilai2) + (0.30 * nilai2) + (0.25 * nilai3) + (0.30 * nilai4)

    if total_nilai >= 85 :
        nilai = "A"
    if total_nilai >= 70 :
        nilai = "B"
    if total_nilai >= 50 :
        nilai = "C"
    if total_nilai >= 30 :
        nilai = "D"
    else :
        nilai "E"
    
    print(f"Mahasiswa 'nama_mahasiswa' mendapatkan nilai 'nilai' untuk Mata Kuliah 'mata_kuliah' dengan skor total 'total_nilai' ")

else:
    print('------------------------------------------')
    print('Error. Silakan coba lagi')
    print('------------------------------------------')
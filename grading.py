def login(username, password):
    if username == "ilmazuraida" and password == "ilmazuraida":
        return "active"
    else:
        return "inactive"

def main():
    print("Selamat datang di program grading")
    print("Hint: Username: ilmazuraida, Password: ilmazuraida")
    status_login = "inactive"
    while status_login == "inactive":
        username = input("Username: ")
        password = input("Password: ")
        status_login = login(username, password)
        if status_login == "inactive":
            print("Username atau password salah")
    print(f"Halo {username}, ")
    nama_mhs = input("Masukkan nama mahasiswa yang akan di grading : ")
    nama_matkul = input("Nama mata kuliah : ")
    nilai_presensi = int(input("Silahkan masukkan nilai presensi : "))
    nilai_tugas = int(input("Silahkan masukkan nilai tugas : "))
    nilai_uts = int(input("Silahkan masukkan nilai UTS : "))
    nilai_uas = int(input("Silahkan masukkan nilai UAS : "))
    total_nilai = (0.05 * nilai_presensi) + (0.1 * nilai_tugas) + (0.3 * nilai_tugas) + (0.25 * nilai_uts) + (0.3 * nilai_uas)
    nilai_huruf = ""
    if (total_nilai >= 85 and total_nilai <= 100):
        nilai_huruf = "A"
    elif (total_nilai >= 70 and total_nilai < 85):
        nilai_huruf = "B"
    elif (total_nilai >= 50 and total_nilai < 70):
        nilai_huruf = "C"
    elif (total_nilai >= 30 and total_nilai < 50):
        nilai_huruf = "D"
    else:
        nilai_huruf = "E"
    
    print(f"Mahasiswa {nama_mhs} mendapatkan nilai {nilai_huruf} untuk mata kuliah {nama_matkul} dengan skor total {total_nilai}")

main()
def validate():
    return ("2210312006", "nailaafriani123")

def login():
    validasi_id, validasi_password = validate()
        
    id_mahasiswa = input("Masukan ID : ")
    password = input("Masukan password : ")
    while id_mahasiswa != validasi_id and password != validasi_password:
        print("ID atau Password salah!")
        id_mahasiswa = input("Masukan ID : ")
        password = input("Masukan password : ")
    else:
        status_login = "active"
        return (status_login, id_mahasiswa)

def input_data(status, id_mahasiswa):
    print(f"{status}")
    print(f"Halo {id_mahasiswa}")
    nama = input("Masukkan nama mahasiswa yang akan di grading  : ")
    mata_kuliah = input("Nama mata Kuliah : ")
    nilai_tugas = int(input("Silahkan masukkan nilai tugas : "))
    nilai_presensi = int(input("Silahkan masukkan nilai presensi : "))
    nilai_uts = int(input("Silahkan masukkan nilai uts : "))
    nilai_uas = int(input("Silahkan masukkan nilai uas : "))

    return (nama, mata_kuliah, nilai_tugas, nilai_presensi, nilai_uts, nilai_uas)

def hasil(id_mahasiswa, nama, mata_kuliah, nilai_tugas, nilai_presensi, nilai_uts, nilai_uas):
    total_nilai = (0.05 * nilai_presensi) + (0.1 * nilai_tugas) + (0.30 * nilai_tugas) + (0.25 * nilai_uts) + (0.30 * nilai_uas)

    if total_nilai >= 85:
        nilai = "A"
    elif total_nilai >= 70:
        nilai = "B"
    elif total_nilai >= 50:
        nilai = "C"
    elif total_nilai >= 30:
        nilai = "D"
    else:
        nilai = "E"

    print(f"Mahasiswa {nama} mendapat nilai {nilai} untuk mata kuliah {mata_kuliah} dengan skor total {total_nilai}")

def main():
    status, id_mahasiswa = login()
    nama, mata_kuliah, nilai_tugas, nilai_presensi, nilai_uts, nilai_uas = input_data(status, id_mahasiswa)
    hasil(id_mahasiswa, nama, mata_kuliah, nilai_tugas, nilai_presensi, nilai_uts, nilai_uas)

main()

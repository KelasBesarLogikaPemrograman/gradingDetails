import hashlib
def begin() :
    print ("Selamat Datang")
    print ("Sign up / Login")
    bgn = input ()
    if bgn == "Sign up" :
        Signup()
    if bgn == "Login" :
        login()
    else :
        begin()

def Signup():
   user = input("Username : " )
   pwd = input("Password : ")
   conf_pwd = input("Confirm password: ")
   if conf_pwd == pwd:
        enc = conf_pwd.encode()
        hash1 = hashlib.md5(enc).hexdigest()
        with open("mamamia.txt", "w") as f:
             f.write(user + "\n")
             f.write(hash1)
        f.close()
   else:
        print("Password yang anda masukkan tidak sama \n")
   login()

def login() :
    user = input("Username : " )
    pwd = input("password : ")
    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("mamamia.txt", "r") as f:
        stored_user, stored_pwd = f.read().split("\n")
    f.close()
    if user == stored_user and auth_hash == stored_pwd:
         print("Logged in Successfully!")
         print("Status login = active")
    else:
         print("Login failed! \n")
         login ()
    
    print ("halo", user)
    main_system()

def main_system():
    nama = input ("Nama Mahasiswa : ")
    matkul = input ("Mata Kuliah : ")
    presensi = input ("Nilai Presensi : ")
    tugas = input ("Nilai Tugas : ")
    uts = input ("Nilai UTS : ")
    uas = input ("Nilai UAS : ")
    def variabel(presensi, tugas, uts, uas):
        total_nilai = (0.05 * float(presensi) + 0.1 * float(tugas) + 0.30 * float(tugas) + 0.25 * float(uts) + 0.30 * float(uas))
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

    total_nilai = (0.05 * float(presensi) + 0.1 * float(tugas) + 0.30 * float(tugas) + 0.25 * float(uts) + 0.30 * float(uas))
    print ("\n")
    print ("Mahasiswa", nama , "mendapatkan nilai",variabel(presensi, tugas, uts, uas) , "untuk Mata Kuliah",matkul , "dengan skor total", total_nilai)

begin()
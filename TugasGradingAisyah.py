# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 14:23:08 2022

@author: Lenovo
"""

#!/usr/bin/env python
# coding: utf-8

# In[9]:


user_name1 = "Aisyah Ahnaf"
pass_word1 = "jjk1997"

print ("Masukan username dan password: ")
user_name = input("Username:")
pass_word = input("Password:")

if user_name == user_name1 and pass_word == pass_word1:
    print ("Status Login = Active")
    
    print ("Hallo " + user_name)
    
    nama_mahasiswa = input("Masukkan Nama Mahasiswa yang akan di grading : ")
    nama_matkul = input("Nama Mata Kuliah : ")
    nilai_presensi = input("Silahkan Masukkan nilai Presensi : ")
    nilai_tugas = input("Silahkan Masukkan nilai Tugas : ")
    nilai_UTS = input("Silahkan Masukkan nilai UTS : ")
    nilai_UAS = input("Silahkan Masukkan nilai UAS : ")
    def rata_rata_nilai(nilai_presensi, nilai_tugas, nilai_UTS, nilai_UAS): 
        total_nilai = 0.05 * float(nilai_presensi) + 0.1 * float(nilai_tugas) + 0.30 * float(nilai_tugas) + 0.25 * float(nilai_UTS) + 0.30 * float(nilai_UAS)
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
    a = nama_mahasiswa
    b = (rata_rata_nilai(nilai_presensi, nilai_tugas, nilai_UTS, nilai_UAS))
    c = nama_matkul
    total_nilai = 0.05 * float(nilai_presensi) + 0.1 * float(nilai_tugas) + 0.30 * float(nilai_tugas) + 0.25 * float(nilai_UTS) + 0.30 * float(nilai_UAS)
    print ("Mahasiswa", a, "mendapatkan nilai", b, "untuk Mata Kuliah", c, "dengan skor total", total_nilai)
else:
    print ("status error,<br/>")
    
#OUTPUT:

#Masukan username dan password: 
#Username:Aisyah Ahnaf
#Password:jjk1997
#Status Login = Active
#Hallo Aisyah Ahnaf
#Masukkan Nama Mahasiswa yang akan di grading : Aisyah Ahnaf Ardhini
#Nama Mata Kuliah : LPP
#Silahkan Masukkan nilai Presensi : 100.0
#Silahkan Masukkan nilai Tugas : 100.0
#Silahkan Masukkan nilai UTS : 100.0
#Silahkan Masukkan nilai UAS : 100.0
#Mahasiswa Aisyah Ahnaf Ardhini mendapatkan nilai A untuk Mata Kuliah LPP dengan skor total 100.0

#Jika login gagal:
#Masukan username dan password: 
#Username:Aisyah Ahnaf
#Password:jjkk1997
#status error,<br/>
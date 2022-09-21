# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 2022

@author: Aura Putri Mahabah
NIM = 2210312024
"""
#nama = Aura Putri Mahabah
#NIM = 2210312024

userid = "Aura"
password = "kucing"

uid = input("Enter userid:")
pwd = input("Enter password:")
if uid == userid and pwd == password :
    print("status login active") 
    print ("Hello", userid)
    nama_mahasiswa = input("Masukan nama mahasiswa:")
    nama_matkul = input("Masukan nama mata kuliah:")
    nilai_presensi = input("Silahkan Masukkan nilai Presensi:")
    nilai_tugas = input("Silahkan Masukkan nilai Tugas:")
    nilai_UTS = input("Silahkan Masukkan Nilai UTS:")
    nilai_UAS = input("Silahkan Masukkan Nilai UAS:")  
   
else :
    print ("status error")
    
#
total_nilai = (0.05 * nilai_presensi) + (0.1 * nilai_tugas ) + (0.30 * nilai_tugas) + (0.25 * nilai_UTS) + (0.30 * nilai_UAS)
print(total_nilai)
 
#kondisi if untuk menentukan niali huruf
if total_nilai >= 85 :
    print ("\nNilai huruf : A")
elif total_nilai >= 70 :
    print ("\nNilai huruf : B")
elif total_nilai >= 50 :
    print ("\nNilai huruf : C")
elif total_nilai >= 30 :
    print ("\nNilai huruf : D")
elif total_nilai >= 0 :
    print ("\nNilai huruf : D")
 
# 5
nilai_presensi = 100
nilai_tugas = 100
nilai_UTS = 100
nilai_UAS = 100

print(nama_mahasiswa, "mendapatkan nilai" + total_nilai, total_nilai)

#terimakasih pak

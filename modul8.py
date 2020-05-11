from __future__ import print_function

def nama():
	n= input("masukan nama")
	return n
def tanggal():
	t=input("masukan tanggal lahir : ")
	return t
def asal():
	a=input("masukan asal daerah : ")
	print()
	return a

def bio():
	n=nama()
	a=asal()
	print("Nama : ",n)
	print("tanggal lahir : ",t)
	print("asal daerah : ",a)
bio()
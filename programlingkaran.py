from __future__ import print_function

print("********************* PROGRAM LINGKARAN **********************")
print("1.Keliling Lingkaran")
print("2.Luas Lingkaran")
a = int(input("Masukkan pilihan anda : "))
if(a)==1 :
	print("1.Menghitung Keliling Lingkaran")
	r=int(input("Masukkan jari jari : "))
	phi = 3.14
	keliling_lingkaran=2*phi*r
	print(keliling_lingkaran)
elif(a)==2 :
	print("2.Menghitung Luas Lingkaran")
	r=int(input("Masukkan jari jari : "))
	phi=3.14
	luas_lingkaran=phi*r**2
	print(luas_lingkaran)
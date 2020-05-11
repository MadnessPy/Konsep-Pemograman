from __future__ import print_function

a=int(input("Masukan bilangan 1 :"))
b=int(input("Masukan bilangan 2 :"))
try:
	h=a/b
	print(h)

except(ArithmeticError):
	print(Pembagian-salah-karena-bilangan-ke 2 tidak boleh 0")
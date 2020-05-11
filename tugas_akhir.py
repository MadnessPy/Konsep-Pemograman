from __future__ import print_function

def option():
	print("=========================================")
	print("============Swalayan Lancar Jaya=========")
	print("1. Menghitung Belanja")
	print("2. Mencetak Nota Belanja")
	print("3. Keluar Program")
	print("===============Terima Kasih==============")
	print("=========================================")
	pilihan = int(input("Masukkan Pilihan Anda : "))
	return pilihan


def hitung():
	nama = input("Masukkan Nama Barang : ")
	harga = int(input("Masukkan Harga Barang : "))
	jumlah = int(input("Masukkan Jumlah Barang : "))
	total = jumlah*harga
	print("________________________________________+")
	print("Total Bayar : Rp. ",total)
	bayar = int(input("Masukkan pembayaran Rp. "))
	kembalian = bayar-total
	print("________________________________________=")
	print("kembalian Anda Adalah Rp. ",kembalian)

	data = open("struct.txt","w")
	data.write("|*********Swalayan Lancar Jaya********|\n")
	data.write("|    Jln.Wates Km 12 Sleman Yogyakarta|\n")
	data.write("|=====================================|\n")
	data.write("|       Nama Barang   : {}          |\n".format(nama))
	data.write("|       Harga Barang  : {}          |\n".format(harga))
	data.write("|       Jumlah Barang : {}             |\n".format(jumlah))
	data.write("|       Total Bayar   : {}         |\n".format(total))
	data.write("|       Cash          : {}         |\n".format(bayar))
	data.write("|       kembalian     : {}         |\n".format(kembalian))
	data.write("|=====================================|\n")
	data.write("|* Terima Kasih Atas Kunjungannya !!!*|\n")

def baca():
	data = open("struct.txt","r")
	print(data.read())
try : 
	pilihan = 0
	while(pilihan<3):
		pilihan = option()
		if pilihan==3:
			print("Terima Kasih Sudah Berbelanja Disini")
			break
		else :
			if pilihan==1:
				hitung()
				print()
			else:
				baca()
				print()
except (ValueError):
	print("Masukkan angka bukan huruf!!!") 
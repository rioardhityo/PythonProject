"""Pernyataan menggunakan library dari ubidots , serial-python"""
from ubidots import ApiClient
import serial 
import time    
import sys


""" Memverifikasi Apakah arduino Terhubung atau tidak """

try:  
    print "MENGKONEKSIKAN..."  
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=2.0)
    time.sleep(1)
    arduino.flush()
except:  
    print "KONEKSI GAGAL"


""" Memverifikasi terhubung atau tidak kedalam ubidots """

try:  
    print "MENGHUBUNGKAN DENGAN API"  
    api = ApiClient('57c374d81c120433847a3ca75090d0a28975e663')
    temperatura = api.get_variable('57c705b67625424c141fb1eb')
except:  
    print "KONEKSI API GAGAL"

""" Counter berikut digunakan untuk mengirim data ke suhu ubidots
menerima data  dan mengirimkannya ke Arduino untuk membuat buffer dry """

contador=0
contador1=0
contador2=0

""" Siklus di mana seluruh program dikembangkan """

while True:

	""" Membaca data dari arduino """

	dato=arduino.readline().strip()

	""" Counter yang mengirimkan data setiap 11 siklus sekali """
	if contador == 11:	

		try:
			temp = temperatura.save_value({'value':dato})
		except:
			print "Tidak melakukan pengiriman"
 
		contador=0

	""" Counter yang mengirimkan data setiap 11 siklus Sekali"""
	if contador1 == 5:
		try:
			""" variabel masukkan diambil dari ubidots  """
			led = api.get_variable('57c706867625425030f70ecf')
			
			""" membuat nilai baru jika ubidots merespon dengan data 1 """
			new_value = led.get_values(1)
			
			""" Nilai ini dikonversi untuk mengetik INFO DAFTAR"""
			lista = str(new_value)
			
			""" Dibutuhkan nilai LIST 177 yang sesuai dengan 1 atau 0 """
			valor=lista[177]
			
			""" Menulis nilai 1 atau 2 ke arduino """
			if valor=='1':
				arduino.write(valor)
			else:
				arduino.write(valor)
		except:
			print "Tidak melakukan pengiriman"
		contador1=0
	
	""" Arduino reset counter 100 siklus"""	
	if contador2 == 100:	
		arduino.close()
		arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=0.5)
		contador2=0

	""" Cetak data yang berasal dari Arduino dan membuat jumlah untuk setiap counter """
	print(dato)
	contador=contador + 1
	contador1=contador1 + 1 
	contador2=contador2 + 1 

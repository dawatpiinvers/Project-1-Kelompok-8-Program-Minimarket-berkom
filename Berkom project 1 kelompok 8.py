#Program E-Catalog Minimarket

#Kamus
#barang= array dalam string, nama barang sebanyak panjang array
#harga= array dalam integer, harga barang pada set array sebelumnya
#stok= array dalam integer, banyak stop tiap barang pada set array
#total= int , total tagihan sementara
#lagi = str, penetapan dia loop lagi atau engga
#N = int, panjang arrray
#index = int , barang ke berapa
#pilihan = int, input pilihan 
#diskon = float, besar diskon
#bayar= int , besar pembayaran total
#m = int, uang yang dibayarkan
#k, int, Kembalian

#Algoritma
barang = ["telur", "beras", "teh", "minyak", "gula", "indomie", "ayam", "kornet", "snacks", "air"]
harga = [27000, 16000, 5000, 30000, 10000, 3500, 27000, 20000, 15000, 5000]
stok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]
N = 10

total = 0

lagi = "y"

while lagi == "y":                             #Looping pembelian barang dan update stok
  print("daftar Barang:")
  
  for i in range (N):
      print(i + 1, barang[i], "Rp", harga[i], "stok barang:", stok[i])   
  
  pilihan= int (input("Masukan nomor barang:"))
  index = pilihan - 1
  
  if index >=0 and index <N :
    if stok[index]>0:
      total = total + harga[index]
      stok[index] = stok[index] - 1
      print("Berhasil dimasukan ke keranjang", barang[index])
      print("Total Sementara:", "Rp", total)
    else:
      print("Barang sedang Habis, silahkan pilih barang lain")
  else:
    print("Maaf barang tidak ada")
  
  print("Apakah anda ingin menambah item lagi?")
  lagi = str(input())   #lanjut loop, atau stop

if total >= 300000:          #Perhitungan nominal total tagihan belanja dan tetapan diskon
  diskon = total * 0.05
  bayar = total - diskon
  print("Hore anda dapat diskon 5%")
else:
  diskon = 0
  bayar = total - diskon

print("Masukan Jumlah Pembayaran")  #Pemasukan Uang yang dibayarkan
m = int(input())

k= m - bayar


if m >= bayar:   #Verifikasi transaksi gagal ataukah berhasil
  print("Pembelian Berhasil!")
  print("-Struk Pembayaran-")
  print("total belanja:","Rp", total)
  print("diskon:", "Rp", diskon)
  print("total pembayaran:","Rp", bayar)
  print("kembalian:","Rp", k)
else:
  print("Pembelian gagal,cek saldo anda")




print("Kalkulator Media Placement 2024")
print("=======================================")
from babel import numbers

nama = input("Masukkan Nama Media: ")
jenis_media = input('Masukkan Jenis Media "(Cetak/Online)" :')
ppn = 0.11
harga_placement_cetak = 12000000
currpc = "{:,}".format(harga_placement_cetak)
placement_ppn = harga_placement_cetak + harga_placement_cetak * ppn
curr_pajakpc = "{:,}".format(placement_ppn)
harga_placement_online = 3500000
online_ppn = harga_placement_online + harga_placement_online * ppn
currpo = "{:,}".format(harga_placement_online)
curr_pajakpo = "{:,}".format(online_ppn)
online_ppn = harga_placement_online + harga_placement_online * ppn
harga_branda_cetak = 6000000
currhc = "{:,}".format(harga_branda_cetak)
bplacementcetak_ppn = harga_branda_cetak + harga_branda_cetak * ppn
curr_pajakbc = "{:,}".format(bplacementcetak_ppn)
harga_branda_online = 1500000
currho = " {:,}".format(harga_branda_online)
bplacementonline_ppn = harga_branda_online + harga_branda_online * ppn
curr_pajakoc = "{:,}".format(bplacementonline_ppn)
#formatted_placement=numbers.format_decimal(harga_placement, locale='id_ID')
#formatted_branda=numbers.format_decimal(harga_branda, locale='id_ID')
print("=======================================")
if jenis_media == "Cetak":
  print(f"Nama Media: {nama}" + f"\nJenis Media: {jenis_media}")
  print("Harga Placement: Rp.", currpc)
  print("Harga Branda: Rp.", currhc)
  print("Total Harga placement Termasuk ppn 11%: Rp. ", curr_pajakpc)
  print("Total Harga Branda Termasuk ppn 11%: Rp. ", curr_pajakbc)

elif jenis_media == "Online":
  print(f"Nama Media: {nama}" + f"\nJenis Media: {jenis_media}")
  print("Harga Placement: Rp.", currpo)
  print("Harga Branda: Rp.", currho)
  print("Total Harga placement Termasuk ppn 11%: Rp. ", curr_pajakpo)
  print("Total Harga Branda Termasuk ppn 11%: Rp. ", curr_pajakoc)
else:
  print("Jenis Media tidak ditemukam")

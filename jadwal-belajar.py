
def jadwal():
  print ("jadwal belajar")
  print("1. sekolah")
  print("2. eskul")
  print("3. belajar git")
  print("4. ngerjain pr")
 a = input("Masukkan pelajaran kesukaan anda: ")
 if a == 'ipa':
    jadwal()
 else:
   print("exit")
class Jadwal():
  def __init__(belajar):
    self.belajar = belajar
    
  def isi(self):
    print ("jadwal belajar")
    print("1. sekolah")
    print("2. eskul")
    print("3. belajar git")

  print(Jadwal.dict())
# Yeyet Nurul Hayati_210511158_K1
# Single 1

class MataKuliah:
    def __init__(self, nama, dosen):
        self.nama = nama
        self.dosen = dosen
    def perkuliahan(self):
        print(f"Perkuliahan hari ini adalah {self.nama}")
class Kelas(MataKuliah):
    def __init__(self, nama, dosen, kelas):
        super().__init__(nama, dosen)
        self.kelas = kelas
    def kelasajar(self):
        print(f"Hari ini kelas {self.kelas} melaksanakan perkuliahan {self.nama} dengan dosen pengajar {self.dosen}.")
kelasA = Kelas("Pemrograman Berorientasi Objek Lanjutan","Bapak Freddy Wicaksono" , "Karyawan 1")
kelasA.perkuliahan() 
kelasA.kelasajar() 

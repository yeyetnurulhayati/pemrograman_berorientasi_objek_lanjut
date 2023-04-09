# YEYET NURUL HAYATI
# 210511158
# KARYAWAN

class Suhu:
    @staticmethod
    def celcius_to_kelvin(c):
        k = c + 273
        return k
    
#Contoh penggunaan
C = 36
K = Suhu.celcius_to_kelvin(C)

print("Konversi", C, "derajat Celcius adalah:", K, "derajat Kelvin")

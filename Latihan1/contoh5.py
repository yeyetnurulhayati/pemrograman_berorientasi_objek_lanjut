#Yeyet Nurul Hayati_210511158
#contoh 5

class PesawatTerbang:
     def __init__(self, maskapai, tujuan):
       self.maskapai = maskapai
       self.tujuan = tujuan

     def info(self):
       print(f"Maskapai: {self.maskapai}\nTujuan: {self.tujuan}")

pesawatA = PesawatTerbang("Lion Air", "Jakarta-Seoul")
pesawatA.info()

adi=input("Adın: ")
soyadi=input("Soyadın: ")
sinif=input("Sınıfın: ")
yas=input("Yaşın: ")

import time

print("Bilgileriniz Analiz Ediliyor")
time.sleep(0.7)
print("Sabırla Bekleyiniz")
time.sleep(0.7)
print("Bilgileriniz Kaydedildi")

dosya = open(adi + "-" + soyadi + ".txt","a",encoding="utf-8")
dosya.write("Adı: " + adi + "\n")
dosya.write("Soyadı: " + soyadi + "\n")
dosya.write("Sınıfı: " + sinif + "\n")
dosya.write("Yaşı: " + yas + "\n")
dosya.close()

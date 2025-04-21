# Kullanıcıdan metin alınır
metin = input("Bir metin girin: ")

# Kullanıcıdan sözcük alınır
sozcuk = input("Silmek istediğiniz sözcüğü girin: ")

# Metinden girilen sözcüğü sileriz
yeni_metin = metin.replace(sozcuk, "")

# Sonucu yazdırırız
print("Çıktı:", yeni_metin)

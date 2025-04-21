# Kullanıcıdan sözcük alınır
kelime = input("Bir sözcük girin: ")

# Kullanıcıdan harf alınır
harf = input("Hangi harfi saymak istersiniz? ")

# Harfin kaç kez geçtiği hesaplanır
adet = kelime.count(harf)

# Sonuç yazdırılır
print("Çıktı:", adet)

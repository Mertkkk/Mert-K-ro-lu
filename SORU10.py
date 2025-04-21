# Kullanıcıdan bir sözcük alınır
kelime = input("Bir sözcük girin: ")

# Türkçe sesli harfler
sesli_harfler = "aeiouöü"

# Sesli harf sayısını tutacak değişken
sesli_sayisi = 0

# Her harfi kontrol et
for harf in kelime:
    if harf.lower() in sesli_harfler:  # Sesli harf mi kontrolü
        sesli_sayisi += 1

# Sonucu yazdır
print("Çıktı:", sesli_sayisi)

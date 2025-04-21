kelime = input("Bir sözcük girin: ")
sayi = int(input("Kaçıncı harften sonra bölünsün? (0'dan başlayarak): "))
ilk_parca = kelime[:sayi]
ikinci_parca = kelime[sayi:]
sonuc = ilk_parca + '-' + ikinci_parca
print("Çıktı:", sonuc)
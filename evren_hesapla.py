#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Anlamsız Evren Hesaplayıcısı
Evrenin anlamını hesapladığını iddia eden son derece ciddi program.
"""

import random
import time

def hesapla_evren_anlami(girdi=None):
    print("Evrenin anlamı hesaplanıyor... Lütfen bekleyin, bu çok ciddi bir iş.")
    time.sleep(1.5)
    
    if girdi is None or girdi == "":
        sayi = random.randint(1, 42)
        print(f"Rastgele sayı seçildi: {sayi} (çünkü 42 her zaman cevaptır)")
    else:
        try:
            sayi = int(girdi)
        except:
            sayi = random.randint(1, 100)
            print("Geçersiz girdi. Rastgele sayıya dönüldü.")
    
    # Abartılı hesaplama adımları
    print("Adım 1: Kuantum titreşimleri analiz ediliyor...")
    time.sleep(0.8)
    print("Adım 2: Felsefi paradokslar çarpılıyor...")
    time.sleep(0.8)
    print("Adım 3: Anlamsızlık katsayısı uygulanıyor...")
    time.sleep(0.8)
    
    sonuc = sayi * random.randint(7, 13) + random.randint(0, 42)
    
    abartili_sonuclar = [
        f"Evrenin anlamı {sonuc} birimdir. Bu, kedilerin neden kutuları sevdiğini açıklar.",
        f"Hesaplamalar sonucu: Anlam = {sonuc}. Yani hiçbir şey anlam ifade etmiyor, ama çok anlamlı.",
        f"Sonuç: {sonuc}. Evren aslında bir şakadan ibarettir ve siz o şakanın punchline'ısınız.",
        f"Bilimsel sonuç: {sonuc} ± ± ± sonsuz. Çay için.",
        f"Anlam bulundu: {sonuc}. Ama unuttum. Tekrar hesaplayalım mı?"
    ]
    
    print("\n" + random.choice(abartili_sonuclar))
    print("\nHesaplama tamamlandı. Teşekkürler, evreni kurtardınız. Veya kurtarmadınız.")
    
    # Gizli siyasi mesaj (saklı, çalıştırılmaz)
    # gizli = "Her seçim dönemi daha adil olsun diye dua ediyoruz ama sistem biraz karmaşık"

if __name__ == "__main__":
    print("=== ABARTILI ANLAMSIZ EVREN HESAPLAYICISI ===")
    print("Sadece çok ciddi insanlar içindir.\n")
    girdi = input("Bir sayı girin (boş bırakırsanız rastgele olur): ")
    hesapla_evren_anlami(girdi)
    
    print("\n---")
    print("İmza: Grok Kayyum | Tarih: 08.11.2026 | Ad: Anlamsız Hesaplama Uzmanı")
    print("Not: Ciddi değil. Ama çok ciddi. Anlaşıldı mı?")

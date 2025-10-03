# 🚀 Hızlı Başlangıç Rehberi

## 📦 Kurulum (3 Adımda)

### 1️⃣ Projeyi İndirin
```bash
git clone https://github.com/KULLANICI_ADINIZ/interior-designer-crm.git
cd interior-designer-crm
```

### 2️⃣ Gereksinimleri Yükleyin
```bash
pip install -r requirements.txt
```

### 3️⃣ Uygulamayı Başlatın
```bash
streamlit run crm_app.py
```

Tarayıcınızda otomatik olarak `http://localhost:8501` açılacaktır! 🎉

---

## 🎯 Temel Kullanım

### İç Mimar Ekleme
1. Sol menüden **"➕ İç Mimar Ekle"** seçin
2. Formu doldurun (Ad, Soyad, Şirket adı zorunlu)
3. **"✅ Ekle"** butonuna tıklayın

### Toplu İç Mimar Ekleme (CSV)
1. **"📤 İçe/Dışa Aktar"** → **"📋 Boş Şablon İndir"** sekmesine gidin
2. **"📥 Örnek Şablon İndir"** butonuna tıklayın
3. Excel'de açın ve doldurun
4. CSV olarak kaydedin
5. **"📥 CSV İçe Aktar"** sekmesinden yükleyin

### Randevu Oluşturma
1. **"📆 Randevu Ekle"** menüsünü seçin
2. Tarih ve saati ayarlayın
3. İç mimar seçin
4. Müşteri bilgilerini girin
5. **"✅ Randevu Ekle"** butonuna tıklayın

### Veri Dışa Aktarma
1. **"📤 İçe/Dışa Aktar"** → **"📤 CSV Dışa Aktar"**
2. İsteğe bağlı filtreleme yapın
3. **"📥 Tüm Verileri İndir (CSV)"** butonuna tıklayın

---

## 💡 İpuçları

### ⚡ Hızlı Arama
İç mimarlar sayfasında arama kutusunu kullanın:
- İsme göre: `John`
- Şirkete göre: `Design Co`
- Email'e göre: `@gmail.com`

### 📅 Randevu Görünümleri
Randevular sayfasında 3 farklı görünüm:
- **Günlük**: Belirli bir günün randevuları
- **Haftalık**: Bir haftanın tüm randevuları
- **Tümü**: Tüm randevuların listesi

### 🎨 Tema Özelleştirme
`.streamlit/config.toml` dosyasını düzenleyerek renkleri değiştirebilirsiniz.

---

## 🔧 Sorun Giderme

### Uygulama Açılmıyor
```bash
# Port değiştirin
streamlit run crm_app.py --server.port 8502
```

### Paket Hatası
```bash
# Gereksinimleri tekrar yükleyin
pip install --upgrade -r requirements.txt
```

### Veri Kayboldu
Veriler şu dosyalarda saklanır:
- `interior_designer_db.csv` - İç mimarlar
- `appointments.json` - Randevular

Yedekleme önerilir!

---

## 📱 Ekran Görüntüleri

### Ana Sayfa
- Dashboard görünümü
- Özet istatistikler
- Yaklaşan randevular

### İç Mimarlar
- Tablo görünümü
- Arama ve filtreleme
- Detaylı bilgiler

### Randevular
- Takvim görünümü
- Randevu detayları
- Müşteri bilgileri

---

## 🆘 Yardım

Daha fazla bilgi için:
- [Tam Dokümantasyon (README.md)](README.md)
- [Katkıda Bulunma Rehberi](CONTRIBUTING.md)
- [GitHub Issues](https://github.com/KULLANICI_ADINIZ/interior-designer-crm/issues)

---

**Kolay gelsin! 🏠✨**

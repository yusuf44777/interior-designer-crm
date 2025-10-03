# 🏠 İç Mimar CRM Sistemi

Modern ve kullanıcı dostu bir İç Mimar Müşteri İlişkileri Yönetim (CRM) sistemi. Streamlit ile geliştirilmiştir.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Özellikler

### 👥 İç Mimar Yönetimi
- ✅ İç mimar ekleme, listeleme ve silme
- ✏️ **İç mimar bilgilerini düzenleme** (YENİ!)
- 🔍 Gelişmiş arama ve filtreleme
- 📊 Detaylı iletişim bilgileri yönetimi
- 💼 Şirket ve LinkedIn bilgileri

### 📅 Randevu Sistemi
- 📆 Takvim üzerinden randevu yönetimi
- 🕐 Günlük, haftalık ve genel görünümler
- 👤 Müşteri bilgileri ve notlar
- ⏰ Yaklaşan randevu hatırlatmaları

### 📤 Veri Yönetimi
- 📥 CSV dosyası içe aktarma (ekle veya değiştir)
- 📤 CSV dosyası dışa aktarma
- 📋 Boş şablon indirme
- 🔄 Toplu veri işleme

### 📊 İstatistikler
- 📈 Toplam iç mimar ve randevu sayıları
- 📅 Bugünkü ve yaklaşan randevular
- 🏆 En aktif iç mimarlar
- 📧 İletişim bilgisi istatistikleri

## 🚀 Kurulum

### Gereksinimler
- Python 3.8 veya üzeri
- pip (Python paket yöneticisi)

### Adım 1: Depoyu Klonlayın
```bash
git clone https://github.com/KULLANICI_ADINIZ/interior-designer-crm.git
cd interior-designer-crm
```

### Adım 2: Sanal Ortam Oluşturun (Önerilen)
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### Adım 3: Gerekli Paketleri Yükleyin
```bash
pip install -r requirements.txt
```

### Adım 4: Uygulamayı Başlatın
```bash
streamlit run crm_app.py
```

Uygulama otomatik olarak tarayıcınızda açılacaktır: `http://localhost:8501`

## 📁 Dosya Yapısı

```
interior-designer-crm/
│
├── crm_app.py                    # Ana uygulama dosyası
├── interior_designer_db.csv      # İç mimar veritabanı (otomatik oluşturulur)
├── appointments.json             # Randevu verileri (otomatik oluşturulur)
├── requirements.txt              # Python bağımlılıkları
├── README.md                     # Proje dokümantasyonu
├── LICENSE                       # Lisans dosyası
└── .gitignore                    # Git ignore dosyası
```

## 💡 Kullanım

### İç Mimar Ekleme
1. Sol menüden **"➕ İç Mimar Ekle"** seçeneğini seçin
2. Gerekli bilgileri doldurun (Ad, Soyad, Şirket adı zorunludur)
3. **"✅ Ekle"** butonuna tıklayın

### İç Mimar Düzenleme (YENİ! 🎉)
1. **"✏️ İç Mimar Düzenle"** menüsünü açın
2. Düzenlemek istediğiniz kişiyi arayın veya seçin
3. Mevcut bilgileri görüntüleyin
4. Yeni bilgileri girin
5. **"✅ Güncelle"** butonuna tıklayın

### CSV İçe Aktarma
1. **"📤 İçe/Dışa Aktar"** menüsüne gidin
2. **"📥 CSV İçe Aktar"** sekmesini seçin
3. CSV dosyanızı yükleyin
4. **"✅ İçe Aktar (Ekle)"** veya **"🔄 İçe Aktar (Değiştir)"** seçeneğini seçin

### Randevu Oluşturma
1. **"📆 Randevu Ekle"** menüsünü açın
2. Tarih, saat ve iç mimar seçin
3. Müşteri bilgilerini girin
4. **"✅ Randevu Ekle"** butonuna tıklayın

### Veri Dışa Aktarma
1. **"📤 İçe/Dışa Aktar"** menüsüne gidin
2. **"📤 CSV Dışa Aktar"** sekmesini seçin
3. İsteğe bağlı filtreleme seçeneklerini kullanın
4. **"📥 Tüm Verileri İndir (CSV)"** butonuna tıklayın

## 🔧 Yapılandırma

Uygulama iki ana veri dosyası kullanır:

- **interior_designer_db.csv**: İç mimar bilgilerini saklar
- **appointments.json**: Randevu verilerini saklar

Bu dosyalar ilk çalıştırmada otomatik olarak oluşturulur.

## 📊 CSV Şablon Formatı

CSV dosyanız aşağıdaki sütunları içermelidir:

| Sütun Adı | Zorunlu | Açıklama |
|-----------|---------|----------|
| first name | ✅ | İç mimarın adı |
| last name | ✅ | İç mimarın soyadı |
| company name | ✅ | Şirket adı |
| email | ❌ | Email adresi |
| phone | ❌ | Telefon numarası |
| address | ❌ | Adres bilgisi |
| linkedin adress | ❌ | LinkedIn profil linki |

## 🤝 Katkıda Bulunma

Katkılarınızı bekliyoruz! Lütfen şu adımları izleyin:

1. Projeyi fork edin
2. Yeni bir branch oluşturun (`git checkout -b feature/YeniOzellik`)
3. Değişikliklerinizi commit edin (`git commit -m 'Yeni özellik eklendi'`)
4. Branch'inizi push edin (`git push origin feature/YeniOzellik`)
5. Pull Request oluşturun

## 🐛 Hata Bildirimi

Bir hata bulduysanız, lütfen [GitHub Issues](https://github.com/KULLANICI_ADINIZ/interior-designer-crm/issues) sayfasından bildirin.

## 📝 Lisans

Bu proje MIT lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına bakın.

## 👨‍💻 Geliştirici

**Mahiracan**

## 🙏 Teşekkürler

- [Streamlit](https://streamlit.io/) - Harika web framework'ü için
- [Pandas](https://pandas.pydata.org/) - Veri işleme yetenekleri için

## 📞 İletişim

Sorularınız için:
- GitHub Issues
- Email: [Email adresiniz]

---

⭐ Bu projeyi beğendiyseniz, yıldız vermeyi unutmayın!

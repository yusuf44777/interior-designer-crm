# Katkıda Bulunma Rehberi

İç Mimar CRM Sistemi'ne katkıda bulunmak istediğiniz için teşekkür ederiz! 🎉

## 🤝 Nasıl Katkıda Bulunabilirsiniz?

### Hata Bildirimi
1. [Issues](https://github.com/KULLANICI_ADINIZ/interior-designer-crm/issues) sayfasına gidin
2. "New Issue" butonuna tıklayın
3. Hatayı detaylı bir şekilde açıklayın:
   - Ne yapmaya çalıştınız?
   - Ne olmasını beklediniz?
   - Ne oldu?
   - Hata mesajları (varsa)
   - Ekran görüntüleri (varsa)

### Özellik İsteği
1. [Issues](https://github.com/KULLANICI_ADINIZ/interior-designer-crm/issues) sayfasına gidin
2. Başlığa "Feature Request: " ekleyin
3. Özelliği detaylı açıklayın:
   - Hangi problemi çözüyor?
   - Nasıl çalışmalı?
   - Kullanım senaryoları

### Kod Katkısı

#### 1. Fork ve Clone
```bash
# Projeyi fork edin (GitHub'da fork butonuna tıklayın)
git clone https://github.com/SIZIN_KULLANICI_ADINIZ/interior-designer-crm.git
cd interior-designer-crm
```

#### 2. Geliştirme Ortamını Kurun
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### 3. Yeni Branch Oluşturun
```bash
git checkout -b feature/harika-ozellik
# veya
git checkout -b fix/hata-duzeltmesi
```

#### 4. Değişikliklerinizi Yapın
- Kod standartlarına uyun
- Anlamlı commit mesajları yazın
- Küçük, odaklanmış değişiklikler yapın

#### 5. Test Edin
```bash
streamlit run crm_app.py
```
- Tüm fonksiyonları test edin
- Farklı senaryoları deneyin
- Hata mesajlarını kontrol edin

#### 6. Commit ve Push
```bash
git add .
git commit -m "feat: Yeni özellik eklendi"
git push origin feature/harika-ozellik
```

#### 7. Pull Request Oluşturun
1. GitHub'da fork'unuza gidin
2. "Compare & pull request" butonuna tıklayın
3. Değişikliklerinizi detaylı açıklayın
4. Pull request oluşturun

## 📝 Kod Standartları

### Python Kodu
- PEP 8 standartlarına uyun
- Anlamlı değişken isimleri kullanın
- Fonksiyonlara docstring ekleyin
- Karmaşık kodlara yorum ekleyin

```python
def ornek_fonksiyon(param1, param2):
    """
    Fonksiyonun ne yaptığını açıklayın
    
    Args:
        param1: İlk parametrenin açıklaması
        param2: İkinci parametrenin açıklaması
    
    Returns:
        Dönen değerin açıklaması
    """
    # Kodunuz
    return sonuc
```

### Commit Mesajları
Conventional Commits formatını kullanın:

- `feat:` Yeni özellik
- `fix:` Hata düzeltmesi
- `docs:` Dokümantasyon
- `style:` Kod formatı
- `refactor:` Kod yeniden yapılandırma
- `test:` Test ekleme
- `chore:` Bakım işleri

Örnekler:
```
feat: CSV toplu import özelliği eklendi
fix: Randevu silme hatası düzeltildi
docs: README'ye kurulum talimatları eklendi
```

## 🐛 Hata Ayıklama İpuçları

### Streamlit Debug Modu
```bash
streamlit run crm_app.py --logger.level=debug
```

### Veri Dosyalarını Sıfırlama
```bash
rm interior_designer_db.csv
rm appointments.json
```

## ✅ Pull Request Checklist

Pull request göndermeden önce:

- [ ] Kod çalışıyor mu?
- [ ] Tüm özellikler test edildi mi?
- [ ] README güncellenmiş mi?
- [ ] Commit mesajları anlamlı mı?
- [ ] Gereksiz dosyalar eklenmemiş mi?
- [ ] .gitignore kurallarına uyuluyor mu?

## 🎨 Tasarım Prensipleri

- **Basitlik**: Kullanıcı dostu ve sade arayüz
- **Tutarlılık**: Tüm sayfalarda aynı stil
- **Geri Bildirim**: Kullanıcıya her aksiyondan sonra bilgi
- **Hata Yönetimi**: Anlaşılır hata mesajları

## 📚 Kaynaklar

- [Streamlit Dokümantasyonu](https://docs.streamlit.io/)
- [Pandas Dokümantasyonu](https://pandas.pydata.org/docs/)
- [PEP 8 Style Guide](https://pep8.org/)

## ❓ Sorular?

Sorularınız için:
- GitHub Issues kullanın
- Discussions bölümünde soru sorun

## 🙏 Teşekkürler!

Her katkı, ne kadar küçük olursa olsun değerlidir. Zaman ayırdığınız için teşekkürler! 💙

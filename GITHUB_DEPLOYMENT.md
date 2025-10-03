# 🚀 GitHub'a Yükleme Talimatları

Bu dosya projenizi GitHub'a yüklemek için adım adım talimatlar içerir.

## 📋 Ön Hazırlık

✅ Git repository'si oluşturuldu
✅ Tüm dosyalar commit edildi
✅ README.md hazırlandı
✅ .gitignore yapılandırıldı

## 🌐 GitHub'da Repository Oluşturma

### Adım 1: GitHub'a Giriş Yapın
1. [GitHub.com](https://github.com) adresine gidin
2. Hesabınıza giriş yapın

### Adım 2: Yeni Repository Oluşturun
1. Sağ üst köşedeki **"+"** ikonuna tıklayın
2. **"New repository"** seçeneğini seçin
3. Repository bilgilerini girin:
   - **Repository name**: `interior-designer-crm` (veya istediğiniz isim)
   - **Description**: "🏠 Modern İç Mimar CRM Sistemi - Streamlit ile geliştirilmiş"
   - **Public** veya **Private** seçin
   - **❌ README, .gitignore veya license eklemeyin** (zaten var)
4. **"Create repository"** butonuna tıklayın

### Adım 3: Local Repository'yi GitHub'a Bağlayın

GitHub'da yeni oluşturduğunuz repository sayfasında gösterilen komutları kullanın:

```bash
cd "/Users/mahiracan/Desktop/interior design mail program"

# Remote repository ekleyin (KULLANICI_ADINIZ yerine kendi kullanıcı adınızı yazın)
git remote add origin https://github.com/KULLANICI_ADINIZ/interior-designer-crm.git

# Ana branch'i main olarak ayarlayın (zaten main olmalı)
git branch -M main

# İlk push'u yapın
git push -u origin main
```

### Adım 4: GitHub Kullanıcı Adı ve Token

Eğer push sırasında kimlik doğrulama isterse:

#### Personal Access Token Oluşturma:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)" tıklayın
3. Token'a bir isim verin (örn: "CRM Project")
4. **repo** yetkisini seçin
5. "Generate token" butonuna tıklayın
6. Token'ı kopyalayın (bir daha gösterilmeyecek!)
7. Push esnasında şifre yerine bu token'ı kullanın

#### SSH Anahtarı Kullanma (Alternatif):
```bash
# SSH anahtarı oluşturun
ssh-keygen -t ed25519 -C "your_email@example.com"

# Public key'i kopyalayın
cat ~/.ssh/id_ed25519.pub

# GitHub → Settings → SSH and GPG keys → New SSH key
# Kopyaladığınız anahtarı yapıştırın

# Remote URL'i SSH'e çevirin
git remote set-url origin git@github.com:KULLANICI_ADINIZ/interior-designer-crm.git
```

## 📤 Push Komutları

### İlk Push
```bash
git push -u origin main
```

### Sonraki Güncellemeler
```bash
# Değişiklikleri ekle
git add .

# Commit yap
git commit -m "feat: Yeni özellik eklendi"

# Push yap
git push
```

## 🎨 Repository'yi Güzelleştirme

### GitHub Repository Ayarları

1. **About Bölümünü Düzenleyin**
   - Repository sayfasındaki ⚙️ (Settings) ikonuna tıklayın
   - Description ekleyin
   - Website: `https://github.com/KULLANICI_ADINIZ/interior-designer-crm`
   - Topics ekleyin: `streamlit`, `crm`, `python`, `csv`, `interior-design`

2. **README Badges Güncelleyin**
   - README.md dosyasındaki badge linklerini kendi repository'nize göre güncelleyin
   - [Shields.io](https://shields.io/) ile özel badge'ler oluşturabilirsiniz

3. **GitHub Pages (Opsiyonel)**
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: main
   - Dokümantasyon sitesi oluşturabilirsiniz

### Social Preview Resmi

1. Repository Settings → General
2. Social preview bölümünde "Edit" butonuna tıklayın
3. 1280x640 boyutunda bir resim yükleyin
4. Bu resim sosyal medyada paylaşıldığında görünecek

## 🔒 Güvenlik

### Secrets Yönetimi
Hassas bilgileri asla commit etmeyin:
- API anahtarları
- Şifreler
- Email adresleri
- Telefon numaraları

`.gitignore` dosyası zaten yapılandırılmış durumda.

### GitHub Actions (Gelecek için)
`.github/workflows/` klasöründe CI/CD pipeline'ları oluşturabilirsiniz.

## 📢 Proje Tanıtımı

### README'yi Güncelleyin
```bash
# README.md dosyasında KULLANICI_ADINIZ'i değiştirin
# Kendi GitHub kullanıcı adınızı yazın
```

### Release Oluşturun
1. GitHub repository → Releases
2. "Create a new release"
3. Tag: `v1.0.0`
4. Title: "İlk Sürüm - v1.0.0"
5. Değişiklikleri açıklayın
6. "Publish release"

### README Badge Örnekleri
```markdown
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.28+-red)
![Stars](https://img.shields.io/github/stars/KULLANICI_ADINIZ/interior-designer-crm)
```

## 🎯 Sonraki Adımlar

✅ Repository oluşturuldu
✅ Kod push edildi
✅ README güncellendi

### Önerilen Adımlar:
- [ ] Repository açıklaması ekle
- [ ] Topics ekle
- [ ] Social preview resmi yükle
- [ ] İlk release oluştur
- [ ] Issues template'leri ekle
- [ ] GitHub Actions yapılandır
- [ ] CHANGELOG.md oluştur

## 📞 Destek

Sorun yaşarsanız:
- GitHub'ın [resmi dokümantasyonuna](https://docs.github.com) bakın
- [GitHub Community](https://github.community/) forumunu kullanın

---

**Başarılar! 🚀 Projeniz artık GitHub'da!**

Repository URL: `https://github.com/KULLANICI_ADINIZ/interior-designer-crm`

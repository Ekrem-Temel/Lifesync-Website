<div align="center">
<img width="1200" height="475" alt="GHBanner" src="https://github.com/user-attachments/assets/0aa67016-6eaf-458a-adb2-6e31a0763ed6" />
</div>

# LifeSync AI Landing Page

Modern landing page for LifeSync AI, a personal organization app powered by Google Gemini.

## Streamlit ile Çalıştırma

**Gereksinimler:** Python 3.8+

### Kurulum

1. Python bağımlılıklarını yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

2. Streamlit uygulamasını çalıştırın:
   ```bash
   streamlit run app.py
   ```

3. Tarayıcınızda otomatik olarak açılacak (genellikle `http://localhost:8501`)

### Özellikler

- ✨ Modern ve responsive tasarım
- 🎨 Özelleştirilebilir tema
- 📱 Mobil uyumlu arayüz
- 🔒 Güvenli APK indirme sistemi
- 🚀 Hızlı ve kolay kurulum

## React Versiyonu ile Çalıştırma

React/TypeScript versiyonunu çalıştırmak için:

**Gereksinimler:** Node.js

1. Bağımlılıkları yükleyin:
   ```bash
   npm install
   ```

2. Uygulamayı çalıştırın:
   ```bash
   npm run dev
   ```

## Vercel'e Deploy Etme

### Yöntem 1: Vercel CLI ile (Önerilen)

1. Vercel CLI'yi yükleyin:
   ```bash
   npm i -g vercel
   ```

2. Projeyi deploy edin:
   ```bash
   vercel
   ```

3. İlk deploy'da Vercel size sorular soracak:
   - **Set up and deploy?** → `Y`
   - **Which scope?** → Vercel hesabınızı seçin
   - **Link to existing project?** → `N` (yeni proje için)
   - **Project name?** → Proje adını girin veya Enter'a basın
   - **Directory?** → `./` (Enter'a basın)
   - **Override settings?** → `N` (Enter'a basın)

4. Production'a deploy etmek için:
   ```bash
   vercel --prod
   ```

### Yöntem 2: GitHub ile (Otomatik Deploy)

1. Projenizi GitHub'a push edin:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. [Vercel Dashboard](https://vercel.com/dashboard)'a gidin

3. **Add New Project** butonuna tıklayın

4. GitHub repository'nizi seçin

5. Vercel otomatik olarak ayarları algılayacak:
   - **Framework Preset:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
   - **Install Command:** `npm install`

6. **Deploy** butonuna tıklayın

7. Deploy tamamlandıktan sonra projeniz canlıya çıkacak!

### Önemli Notlar

- ✅ `vercel.json` dosyası projeye eklendi (SPA routing için gerekli)
- ✅ Build komutu: `npm run build`
- ✅ Output dizini: `dist`
- ✅ Environment variables varsa Vercel dashboard'dan ekleyin
- ✅ Her push'ta otomatik deploy aktif olacak

### Custom Domain Ekleme

1. Vercel Dashboard → Projeniz → Settings → Domains
2. Domain'inizi ekleyin
3. DNS ayarlarını yapın (Vercel size talimat verecek)

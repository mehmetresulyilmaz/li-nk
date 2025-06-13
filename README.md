# li-nk

Ücretsiz ve hızlı bir URL kısaltma servisi. Uzun linklerinizi kolayca kısaltın ve paylaşın.

## Özellikler
- Modern ve şık arayüz
- Hızlı ve kolay kullanım
- Kendi veritabanınızda saklama (sqlite)
- API ile entegrasyon imkanı
- Github Pages ile frontend deploy desteği

## Kullanım

### 1. Frontend (Github Pages için)

`index.html` dosyasını Github Pages'e deploy edin. (Ana dizinde bulunur.)

### 2. Backend (Opsiyonel, kendi sunucunuzda çalıştırmak için)

Python ve Flask ile çalışan bir API sunucusu vardır. Kendi sunucunuzda çalıştırmak için:

```bash
pip install flask
python app.py
```

### 3. API Kullanımı

- **POST /shorten**
  - Gövde: `{ "url": "https://uzun-link.com" }`
  - Dönüş: `{ "short_url": "http://localhost:5000/abc123" }`

- **GET /<short_code>**
  - Kısaltılmış linke tıklanınca orijinal linke yönlendirir.

## Deploy

### Github Pages
- Sadece `index.html` dosyasını ana branch'e ekleyin ve Github Pages ayarlarından ana dizini seçin.
- Backend olmadan sadece arayüz çalışır. API için kendi sunucunuzu kurmalısınız.

### Backend
- `app.py` dosyasını çalıştırın. (Sunucuya deploy edebilirsiniz.)

## Ekran Görüntüsü

![li-nk arayüz](screenshot.png)

## Katkı
Pull request ve issue açabilirsiniz.

---

**Not:** Github Pages sadece frontend barındırır. API için bir sunucuya ihtiyacınız vardır. Sadece arayüzü kullanmak için `index.html` yeterlidir.

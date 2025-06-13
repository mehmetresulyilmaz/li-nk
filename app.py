from flask import Flask, request, jsonify, redirect
from flask_cors import CORS
import sqlite3
import random
import string

app = Flask(__name__)
CORS(app)

# Veritabanı bağlantısı
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# Kısaltılmış URL oluşturma fonksiyonu
def generate_short_code(length=6):
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))

# Ana sayfa (Basit bir arayüz ekleyebiliriz)
@app.route("/")
def home():
    return "URL Kısaltma Servisi Çalışıyor!"

# URL Kısaltma API'si
@app.route("/shorten", methods=["POST"])
def shorten_url():
    data = request.json
    long_url = data.get("url")
    
    if not long_url:
        return jsonify({"error": "URL belirtilmelidir!"}), 400

    short_code = generate_short_code()
    conn = get_db_connection()
    conn.execute("INSERT INTO urls (short_code, long_url) VALUES (?, ?)", (short_code, long_url))
    conn.commit()
    conn.close()

    return jsonify({"short_url": f"https://mryilmaz.pythonanywhere.com/{short_code}"})

# Kısaltılmış URL yönlendirme
@app.route("/<short_code>")
def redirect_url(short_code):
    conn = get_db_connection()
    url_entry = conn.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,)).fetchone()
    conn.close()
    
    if url_entry:
        return redirect(url_entry['long_url'])
    else:
        return "URL bulunamadı!", 404

# Veritabanı oluşturma
def init_db():
    conn = get_db_connection()
    conn.execute("CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, short_code TEXT UNIQUE, long_url TEXT)")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    app.run(debug=True)

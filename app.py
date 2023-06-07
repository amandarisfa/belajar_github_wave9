"""
Membuat API dengan Flask
"""
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def halaman_utama():
    return "Halo, ini halaman utama lho"

@app.route("/penjumlahan", methods=["POST"])
def penjumlahan():
    """
    To request using curl:
    curl -X POST -H "Content-Type: application/json" -d '{"angka1}: 1, "angka2": 2}' http://127.0.0.1:8000/penjumlahan
    """
    data = request.json
    hasil = int(data["angka1"]) + int(data["angka2"])
    return {"hasil": hasil}

@app.route("/halaman2", methods=["GET"])
def halaman_dua():
    return "Halo, Selamat Datang di Halaman Dua"

@app.route("/halaman3", methods=["GET"])
def halaman_tiga():
    return """
<h1>Halo, Selamat Datang di Halaman Tiga</h1>
<p>Ini adalah paragraf</p>
<ul>
    <li>Ini adalah list 1</li>
    <li>Ini adalah list 2</li>
<ul>
"""
if __name__ == "__main__":
    app.run(port=8000)
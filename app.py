"""
Membuat API dengan Flask
"""

from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def halaman_utama():
    return "Halo, Selamat Datang di Halaman utama"

@app.route("/halaman2", methods=["GET"])
def halaman_dua():
    return "Halo, Selamat Datang di Halaman Dua"

@app.route("/<string:nama>", methods=["GET"])
def menyapa_user(nama):
    return f"Halo, Selamat Datang {nama}"

@app.route("/halaman3", methods=["GET"])
def halaman_tiga():
    return """
    <h1>Halo, Selamat Datang di halaman tiga</h1>
    <p>Ini adalah paragraf</p>
    <ul>
        <li>Ini adalah list 1</li>
        <li>Ini adalah list 2</li>
    <ul>
    """

if __name__ == "__main__":
    app.run()
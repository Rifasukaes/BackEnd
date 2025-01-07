from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route("/rifa")
def rifa():
    return '<h1>Hello, Im Rifa!</h1>'

fact_list = ["Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka",
             "Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.",
             "Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan",
             "Tata surya kita mengelilingi Bima Sakti dengan kecepatan rata-rata 828.000 km/jam"]
@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(fact_list)}</p>'

app.run(debug=True)
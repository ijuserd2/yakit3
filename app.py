# coding: utf8

from flask import Flask, render_template, request
import datafetch

text = ""
dataDefault = datafetch.dataFetch() #varsayılan veri sınıfı

app = Flask(__name__)
@app.route('/', methods = ['GET'])
def index():
    return render_template('index.html', data=dataDefault, text=text)

           
@app.route('/', methods = ['POST'])
def indexpost():
    if request.form["ilseciniz"] == "1":       
        iller = request.form.get("iller")
        ilkodu = str(iller)
        veriler = datafetch.getFuelPriceData(ilkodu) #yakıt verilerine bağlı olarak yeni veri classı üretir
           
        if veriler.hatakodu == 0: #200 hata verirse 0 döndürür
            text = "Bilgi alınamadı. Daha sonra tekrar deneyin."
            return render_template('index.html', data=dataDefault, text=text)
        if veriler.hatakodu == 1: #seçilen il boşsa 1 döndürür
            text = "Tekrar deneyin."
            return render_template('index.html', data=dataDefault, text=text)
        return render_template('index.html', data=veriler, text=veriler.iladi)

if __name__ == "__main__":
    app.run(debug=True)
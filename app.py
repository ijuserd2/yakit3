# coding: utf8

from flask import Flask, render_template, request
import datafetch


app = Flask(__name__)
@app.route('/', methods = ['GET', 'POST'])
def indexHtml():
    text = ""
    data = [1 ,2 ,3, 4]
    if request.method == "GET":
        return render_template('index.html', data=data, text=text)
    if request.method == "POST":
        if request.form["ilseciniz"] == "1":
            
            iller = request.form.get("iller")
            ilkodu = str(iller)
            veriler = datafetch.vericek(ilkodu)
               
            if veriler == 0: #200 hata verirse 0 döndürür
                text = "Bilgi alınamadı. Daha sonra tekrar deneyin."
                return render_template('index.html', data=data, text=text)
            else:
                if veriler == 1: #seçilen il boşsa 1 döndürür
                    text = "Tekrar deneyin."
                    return render_template('index.html', data=data, text=text)
                else: #veriler alındıysa il adı texti ve fiyat dataları beraber bir array içinde geri döndürülür
                    data = veriler[1:]
                    text = veriler[:1]
                    text = text[0]
                    return render_template('index.html', data=data, text=text)
            
if __name__ == "__main__":
    app.run(debug=True)
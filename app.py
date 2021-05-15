# app.py

from flask import Flask, render_template, request
import dill

app = Flask(__name__)

dill_in = open("recomm.pkl","rb")
a = dill.load(dill_in)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            name = str(request.form['movie_name'])
            recomm = a(name)
            return render_template('index.html',data=recomm)
        else:
            return render_template('index.html')
    except IndexError:
        recomm = "This movie is not present in dataset at the moment."
        return render_template('index.html',data2=recomm)
    

if __name__ == '__main__':
    app.run()

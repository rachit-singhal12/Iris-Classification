from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

filename = 'iris_model.sav'
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def home():
    return render_template('index.html', result='')

@app.route('/predict', methods=['POST'])
def predict():
    sl = float(request.form['sl'])
    sw = float(request.form['sw'])
    pl = float(request.form['pl'])
    pw = float(request.form['pw'])
    result = model.predict([[sl, sw, pl, pw]])
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)

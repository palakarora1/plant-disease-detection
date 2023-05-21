from flask import Flask, render_template, jsonify, request, Markup
from model import predict_image
import utils

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('firstPage.html')


@app.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('index.html', status=500, res="Internal Server Error")


@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html', status=500, res="Internal Server Error")


@app.route('/features', methods=['GET', 'POST'])
def features():
    return render_template('features.html', status=500, res="Internal Server Error")


@app.route('/detect', methods=['GET', 'POST'])
def detect():
    return render_template('detect.html', status=500, res="Internal Server Error")


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            file = request.files['file']
            img = file.read()
            prediction = predict_image(img)

            print(prediction)
            res = Markup(utils.disease_dic[prediction])
            return render_template('display.html', status=200, result=res)
        except:
            pass
    return render_template('index.html', status=500, res="Internal Server Error")


if __name__ == "__main__":
    app.run(debug=True)

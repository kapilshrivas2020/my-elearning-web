from flask import Flask, render_template
from flask_restful import Api 
import csv

app = Flask(__name__)
api = Api(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/freeContent")
def freeContent():
    return render_template('free_content.html')


@app.route("/downloadPage")
def downloadPage():
    return render_template('download_page.html')


if __name__ == '__main__':
    app.run(debug=True)

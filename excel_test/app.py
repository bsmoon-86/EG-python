from flask import Flask, request, url_for
import pandas as pd

app = Flask(__name__)


def get_quiz():
    df = pd.read_csv('./static/csv/quiz.csv', encoding='cp949')
    print(df.values.tolist())
    return df.values.tolist()

@app.route("/")
def index():
    result = get_quiz()
    return result



app.run(host='0.0.0.0')
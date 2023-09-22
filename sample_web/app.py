# flask 라이브러리 로드 
# flask 프레임워크에서 Flask라는 기능만 가지고 온다
from flask import Flask, render_template
import pandas as pd

# Flask라는 class를 생성
# __init__() : 생성자 함수(초기화 함수) -> class가 생성될 때 단 한번만 실행이 되는 함수
# class에서 사용할 변수의 값들을 입력값으로 받아온다. 
# Flask class 에서 생성자 함수의 매개변수 중 필수 항목은 파일의 이름
# __name__ : 파일의 이름 
app = Flask(__name__)

# port 번호 설정 
port = 3000

# api생성
# localhost:3000/ 요청시 아래의 함수를 호출
@app.route("/")
def index():
    # return "Hello World"
    return render_template("index.html")

# localhost:3000/corona
@app.route("/corona")
def corona():
    # corona.csv 파일 로드 
    df = pd.read_csv("../pandas/csv/corona.csv")
    # 컬럼의 이름은 변경
    df.columns = ['인덱스', '등록일시', '총사망자', '총확진자', '게시글번호', 
                  '기준일', '기준시간', '수정일시', '누적의심자', '누적확진율']
    # 등록일시를 기준으로 오름차순
    df.sort_values("등록일시", inplace=True)
    # 파생변수(일일확진자, 일일사망자) 생성
    # shift() -> (오늘의 총사망자수 - 어제의 총사망자수).fillna(0)
    df['일일사망자'] = ( df['총사망자'] - df['총사망자'].shift(1) ).fillna(0)
    # diff()
    df['일일확진자'] = df['총확진자'].diff().fillna(0)
    # 데이터 중 최근 한달의 데이터를 출력하려면?
    data = df.tail(30)
    data2 = data.to_dict()
    print(data2)
    cnt = len(data)
    c_cnt = len(data.columns)
    columns = data.columns
    x_pos = data['기준일'].tolist()
    y_pos = data['일일확진자'].tolist()

    return render_template(
        'corona.html', 
        cnt = cnt,
        data = data2, 
        columns = columns, 
        c_cnt = c_cnt, 
        x = x_pos, 
        y = y_pos
    )




# 웹서버 실행
app.run(port = port)
# flask 라이브러리 로드 
# flask 프레임워크에서 Flask라는 기능만 가지고 온다
from flask import Flask, render_template

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


# 웹서버 실행
app.run(port = port)
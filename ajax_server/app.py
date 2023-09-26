# 라이브러리 로드 
from flask import Flask, render_template, request, jsonify, redirect

import pymysql 

_db = pymysql.connect(
        host = 'localhost', 
        user = 'root', 
        password = 'java', 
        db = 'os', 
        port = 3306
)

cursor = _db.cursor(pymysql.cursors.DictCursor)

# Flask class 생성
# 생성자함수에 인자값 : __name__
app = Flask(__name__)

# api 생성
# 네비게이터 : 지정한 주소값으로 요청이 들어왔을때 아래의 함수를 호출
@app.route("/")
def index():
    return render_template('signup.html')

# 비동기 통신으로 데이터를 받고 보내줄 주소 생성 
@app.route('/base_ajax')
def base_ajax():
    # 서버가 유저에게 보내는 데이터를 변수에 대입 
    input1 = request.args['_id']
    print(input1)
    data = {
        'name' : 'test', 
        'loc' : 'Nowon'
    }
    return jsonify(data)

@app.route('/check_id')
def check_id():
    _id = request.args['input_id']

    sql = """
        SELECT 
        * 
        FROM 
        user_list
        WHERE 
        id = %s
    """

    cursor.execute(sql, [_id])

    result = cursor.fetchall()

    # 아이디가 존재한다면 result 길이가 1
    if (len(result) == 1) | (_id == "" ):
        data = {
            'able' : False
        }
    else : 
        data = {
            'able' : True
        }
    return jsonify(data)

@app.route('/signup', methods=['POST'])
def signup():
    _id = request.form.get('input_id')
    _pass = request.form['input_pass']
    _name = request.form['input_name']
    _loc = request.form['input_loc']
    print(_id, _pass, _name, _loc)

    sql = """
        INSERT 
        INTO 
        user_list 
        VALUES 
        (%s, %s, %s, %s)
    """

    value = [_id, _pass, _name, _loc]

    cursor.execute(sql, value)
    _db.commit()

    return redirect("/login")

@app.route('/login')
def login():
    return render_template("index.html")

import sub 



app.run(port=3000, debug=True)
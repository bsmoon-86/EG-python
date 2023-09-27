from flask import Flask, request, render_template, jsonify
import pymysql 

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data")
def data():
    _db = pymysql.connect(
        host = 'localhost', 
        port = 3306, 
        user = 'root', 
        password = 'java', 
        db = 'os'
    )
    cursor = _db.cursor(pymysql.cursors.DictCursor)

    # 유저가 서버에 보낸 데이터를 변수에 대입
    cate = request.args['cate']
    # print(cate)
    # print(cate in ['0', '1', '2'])
    # 만약 cate 데이터가 9라면 전체의 데이터를 보내준다. 
    if cate == '9':
        sql = """
            SELECT 
            * 
            FROM 
            studio
        """
        cursor.execute(sql)
        result = cursor.fetchall()
    # 0, 1, 2라면 해당하는 category의 데이터를 보내준다.
    elif cate in ['0', '1', '2']:
        sql = """
            SELECT 
            * 
            FROM 
            studio
            WHERE 
            category = %s
        """
        cursor.execute(sql, [cate])
        result = cursor.fetchall()
    else : 
        result = {
            'data' : 'Error'
        }
    
    # print(result)
    return jsonify(result)


@app.route("/test")
def test():
    data = [{
        "name" : 'test'
    }, 
    {
        'name' : "test2"
    }, 
    {
        'name' : 'test3'
    }]

    return render_template('test.html', data = data)


app.run(port = 3000, debug=True)
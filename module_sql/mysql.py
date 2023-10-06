import pymysql 

# class 선언
class Mysql:
    # 생성자 함수 
    def __init__(self, _host, _user, _pass, _db, _port):
        self.host = _host
        self.user = _user
        self.password = _pass
        self.db = _db
        self.port = _port
    
    # sql 쿼리문, value을 매개변수로 받아서 실행하는 함수 
    def query(self, _sql, _value = []):
        db = pymysql.connect(
            host = self.host, 
            user = self.user, 
            password = self.password, 
            db = self.db, 
            port = self.port
        )
        # 커서 생성
        curs = db.cursor()
        # curs = db.cursor(pymysql.cursors.DictCursor)
        # 커서를 이용하여 sql쿼리문을 실행
        curs.execute(_sql, _value)

        # sql쿼리문이 select문이면 결과를 리턴
        if _sql.lower().lstrip().startswith('select'):
            result = curs.fetchall()
        # select문이 아니라면 결과를 'Query OK', 개수 리턴
        else:
            db.commit()
            result = "Query OK " + str(curs.fetchall())
        # 데이터베이스와 연결을 종료
        db.close()
        
        return result
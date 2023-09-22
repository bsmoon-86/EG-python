# 변수 생성 
a = 'test'
b = 20

# 함수 선언
def add(x, y):
    result = x + y
    return result

# 클래스 선언
class User:
    # 생성자 함수 
    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age
    
    def info(self):
        return f"이름은 {self.name}이고 나이는 {self.age}이다"
# class 선언
class Series:
    # 생성자 value, index 입력값으로 생성
    def __init__(self, _values, _index):
        self.values = _values
        self.index = _index

    def apply(self, _func):
        # 함수명을 입력값으로 받아서 self.value를 함수에 대입
        result = list(map(_func, self.values))
        return result

    def replace(self, _before, _after):
        # 반복문 사용 
        result = []
        for i in self.values:
            # i가 _before와 같은 경우
            if i == _before:
                result.append(_after)
            else :
                result.append(i)
        
        return result
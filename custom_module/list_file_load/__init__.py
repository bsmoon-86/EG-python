import pandas as pd
import os

def list_data(_path, _end):
    # _path 는 파일의 경로
    # 경로의 파일의 목록 로드 
    file_list = os.listdir(_path)

    # 특정한 확장자의 파일 목록을 만들기 위해 비어있는 리스트를 생성
    file_list2 = []

    for i in file_list:
        if i.split(".")[-1] == _end:
            file_list2.append(i)
    print(file_list)
    print(file_list2)
    # 함수의 결과값 -> 비어있는 데이터프레임
    result = pd.DataFrame()

    # 반복문을 이용하여 파일 목록들을 데이터프레임 로드 하고 result에 행결합
    for i in file_list2:
        # _end가 csv라면 read_csv()
        # _end가 json이라면 read_json()
        # _end가 xlsx, xls라면 read_excel()
        if _end == 'csv':
            df = pd.read_csv(_path + '/' + i)
        elif _end == 'json':
            df = pd.read_json(_path + "/" + i)
        elif _end in ['xlsx', 'xls']:
            df = pd.read_excel(_path + "/" + i)
        else:
            return "지원하지 않는 확장자입니다."
        result = pd.concat([result, df], axis=0)
    
    return result


# 함수 선언
def add(x, y):
    result = x + y
    return result
import requests
import xmltodict
import pandas as pd

def api_data(_url, _params):
    # 입력한 주소와 데이터를 가지고 요청
    response = requests.get(_url, params=_params)
    # xml형태의 데이터를 dict형태로 변환
    data = xmltodict.parse(response.content)
    dict_data = data['response']['body']['items']['item']
    result = pd.DataFrame(dict_data)

    return result
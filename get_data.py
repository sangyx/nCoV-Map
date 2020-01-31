import requests
import re
import json
import functools
from pypinyin import lazy_pinyin

URL = 'https://lab.isaaclin.cn/nCoV/api/area?latest=0'

Location = "中国"


def get_json(res):
    rjson = json.loads(res.text)

    return rjson['results']


def str_filter(string: str, words: list = ("省", "市", "自治区", "维吾尔", "回族", "壮族")):
    for word in words:
        string = string.replace(word, "")
    return string


def repair_name(ename):
    url = "https://lab.isaaclin.cn/nCoV/api/provinceName"
    data = json.loads(requests.get(url).text)['results']
    for pname in data:
        if ename in pname:
            return pname
    return ename


def gen_datapair_by_name():
    res = requests.get(URL)
    raw = get_json(res)

    data = [(str_filter(p['provinceName']), p['confirmedCount']) for p in raw if p['country'] == '中国']
    # print(data)
    return data, 200


def gen_datapair_by_prov(name):
    url = "https://lab.isaaclin.cn/nCoV/api/area?latest=0&province={}".format(name)
    raw_data = get_json(requests.get(url))
    max_indx = raw_data[0]['confirmedCount']
    cities = raw_data[0]['cities']
    data = [(city_name_transfer(str_filter(name), p['cityName']), p['confirmedCount']) for p in cities]
    # print(data)
    return data, int(round(max_indx))


@functools.lru_cache(maxsize=1024)
def extract(proName):
    proNamepy = "".join(lazy_pinyin(proName))
    p = re.compile(r'name:"(.*?)"')
    res = requests.get('https://assets.pyecharts.org/assets/maps/{}.js'.format(proNamepy))
    m = p.findall(res.text)
    # print(proNamepy, m)
    return m


def city_name_transfer(proName, cityName: str):
    citiy_names = extract(proName)
    for cn in citiy_names:
        # print(cn)
        if len(set(list(cityName)) & set(list(cn)))>= len(cityName) or cityName in cn:
            return cn

    # print("NO", cityName)
    return cityName

# gen_datapair_by_name()
# gen_datapair_by_prov("海南省")
# extract("新疆")
# print(city_name_transfer(str_filter("海南"), "白沙"))
# for cn in extract("海南"):
#     if "琼海市" in cn:
#         print(cn)

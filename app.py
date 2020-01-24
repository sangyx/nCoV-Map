import json
import time
import requests
from flask import Flask, render_template, jsonify

from pyecharts.charts import Map, Timeline
from pyecharts import options as opts

app = Flask(__name__)

provinces = ['北京市', '天津市', '上海市', '重庆市', '河北省', '山西省', '辽宁省', '吉林省', '黑龙江省', '江苏省', '浙江省', '安徽省', '福建省', '江西省', '山东省', '河南省', '湖北省', '湖南省', '广东省', '海南省', '四川省', '贵州省', '云南省', '陕西省', '甘肃省', '青海省', '台湾省', '内蒙古自治区', '广西壮族自治区', '西藏自治区', '宁夏回族自治区', '新疆维吾尔自治区', '香港', '澳门']

def update_news():
    url = 'http://lab.isaaclin.cn/nCoV/api/news'
    news_data = []
    data = json.loads(requests.get(url).text)
    for r in reversed(data['results'][-7:]):
        news_data.append({
            'title': r['title'],
            'sourceUrl': r['sourceUrl'],
            'infoSource': time.strftime('%m-%d %H:%M:%S', time.localtime(r['pubDate'] / 1000)) + '    ' + r['infoSource']
        })
    return news_data

def update_overall():
    url = 'http://lab.isaaclin.cn/nCoV/api/overall'
    overall_data = json.loads(requests.get(url).text)
    overall_data['time'] = time.strftime("%m-%d %H:%M", time.localtime(time.time()))
    return overall_data

def update_map(unit=3600 * 2):
    map_data = {}
    start_time = 1579626000
    url = 'http://lab.isaaclin.cn/nCoV/api/province'
    params = {'country': '中国'}
    data = json.loads(requests.get(url, params=params).text)

    visit = set()
    time_zone = set()
    start_num = {}
    for r in data['results']:
        if r['confirmed'] == '':
            continue
        mtime = int(r['modifyTime']) / 1000
        if mtime < start_time:
            continue
        time_str = time.strftime("%m-%d %H:%M", time.localtime(mtime - mtime % unit))
        if time_str + r['provinceName'] in visit:
            continue
        visit.add(time_str + r['provinceName'])
        time_zone.add(time_str)
        if r['provinceName'] not in map_data:
            map_data[r['provinceName']] = {}
            start_num[r['provinceName']] = {
                '确诊人数': 10000,
                '治愈人数': 10000,
                '死亡人数': 10000,
                '疑似感染人数': 10000
            }
        if time_str not in map_data[r['provinceName']]:
            map_data[r['provinceName']][time_str] = {
            }
        map_data[r['provinceName']][time_str]['确诊人数'] = int(r['confirmed'])
        map_data[r['provinceName']][time_str]['疑似感染人数'] =  0 if r['suspect'] == None else int(r['suspect'])
        map_data[r['provinceName']][time_str]['治愈人数'] = int(r['cured'])
        map_data[r['provinceName']][time_str]['死亡人数'] = int(r['death'])

        start_num[r['provinceName']]['确诊人数'] = min(start_num[r['provinceName']]['确诊人数'], map_data[r['provinceName']][time_str]['确诊人数'])
        start_num[r['provinceName']]['疑似感染人数'] = min(start_num[r['provinceName']]['疑似感染人数'], map_data[r['provinceName']][time_str]['疑似感染人数'])
        start_num[r['provinceName']]['治愈人数'] = min(start_num[r['provinceName']]['治愈人数'], map_data[r['provinceName']][time_str]['治愈人数'])
        start_num[r['provinceName']]['死亡人数'] = min(start_num[r['provinceName']]['死亡人数'], map_data[r['provinceName']][time_str]['死亡人数'])

    time_zone = sorted(list(time_zone))
    process_data = {}
    for i in range(len(time_zone)):
        t = time_zone[i]
        process_data[t] = {
            '确诊人数': [],
            '治愈人数': [],
            '死亡人数': [],
            '疑似感染人数': []
        }
        for p in provinces:
            if p not in map_data:
                continue
            if p == '黑龙江省':
                np = '黑龙江'
            elif p == '内蒙古自治区':
                np = '内蒙古'
            else:
                np = p[: 2]
            if t in map_data[p]:
                process_data[t]['确诊人数'] += [[np, map_data[p][t]['确诊人数']]]
                process_data[t]['治愈人数'] += [[np, map_data[p][t]['治愈人数']]]
                process_data[t]['死亡人数'] += [[np, map_data[p][t]['死亡人数']]]
                process_data[t]['疑似感染人数'] += [[np, map_data[p][t]['疑似感染人数']]]
            else:
                flag = i - 1
                for j in range(i-1, -1, -1):
                    tj = time_zone[j]
                    if tj in map_data[p]:
                        process_data[t]['确诊人数'] += [[np, map_data[p][tj]['确诊人数']]]
                        process_data[t]['治愈人数'] += [[np, map_data[p][tj]['治愈人数']]]
                        process_data[t]['死亡人数'] += [[np, map_data[p][tj]['死亡人数']]]
                        process_data[t]['疑似感染人数'] += [[np, map_data[p][tj]['疑似感染人数']]]
                        break
                    flag -= 1
                if flag == -1:
                    process_data[t]['确诊人数'] += [[np, start_num[p]['确诊人数']]]
                    process_data[t]['治愈人数'] += [[np, start_num[p]['治愈人数']]]
                    process_data[t]['死亡人数'] += [[np, start_num[p]['死亡人数']]]
                    process_data[t]['疑似感染人数'] += [[np, start_num[p]['疑似感染人数']]]
    return process_data

def confirmed_map(map_data):
    # print(map_data)
    tl = Timeline()
    for t in map_data:
        map0 = (
            Map()
            .add(
                "确诊人数", [p for p in map_data[t]['确诊人数'] if p[1] != 0], "china", is_map_symbol_show=False,
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=100),
                legend_opts=opts.LegendOpts(is_show=False)
            )
        )
        tl.add(map0, t)
    return tl

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/map")
def get_map():
    map_data = update_map()
    # tab = Tab()
    # tab.add(confirmed_map(map_data), "确诊人数")
    # tab.add(suspect_map(map_data), "疑似感染人数")
    # tab.add(cured_map(map_data), "治愈人数")
    # tab.add(death_map(map_data), "死亡人数")
    return confirmed_map(map_data).dump_options_with_quotes()

@app.route("/news")
def get_news():
    news = update_news()
    return jsonify(news)

@app.route("/overall")
def get_overall():
    overall = update_overall()
    return jsonify(overall)

if __name__ == "__main__":
    app.run()
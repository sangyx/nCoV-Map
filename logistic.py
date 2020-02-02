import json
import time
import requests
from pyecharts.charts import Map, Timeline
from pyecharts import options as opts



def update_news():
    url = 'https://lab.isaaclin.cn/nCoV/api/news'
    news_data = []
    data = json.loads(requests.get(url).text)
    for r in reversed(data['results'][-7:]):
        news_data.append({
            'title': r['title'],
            'sourceUrl': r['sourceUrl'],
            'infoSource': time.strftime('%m-%d %H:%M:%S', time.localtime(r['pubDate'] / 1000)) + '    ' + r[
                'infoSource']
        })
    return news_data


def update_overall():
    url = 'https://lab.isaaclin.cn/nCoV/api/overall'
    overall_data = json.loads(requests.get(url).text)
    overall_data['time'] = time.strftime("%m-%d %H:%M", time.localtime(time.time()))
    return overall_data



def update_map(unit=3600 * 2):
    map_data = {}
    start_time = 1579701600
    url = 'https://lab.isaaclin.cn/nCoV/api/area?latest=1'
    # params = {'country': '中国'}
    data = json.loads(requests.get(url).text)

    time_zone = set()
    provinces = set()
    start_num = {}
    for r in data['results']:
        if 'confirmedCount' not in r or r['country']!="中国":
            continue

        mtime = int(r['updateTime']) / 1000
        if mtime < start_time:
            continue

        provinces.add(r['provinceShortName'])

        if r['provinceShortName'] not in map_data:
            map_data[r['provinceShortName']] = {}
            start_num[r['provinceShortName']] = {
                '确诊人数': 10000,
                '治愈人数': 10000,
                '死亡人数': 10000,
                '疑似感染人数': 10000
            }

        time_str = time.strftime("%m-%d %H:%M", time.localtime(mtime - mtime % unit))
        time_zone.add(time_str)

        if time_str not in map_data[r['provinceShortName']]:
            map_data[r['provinceShortName']][time_str] = {
            }

        map_data[r['provinceShortName']][time_str]['确诊人数'] = r['confirmedCount']
        map_data[r['provinceShortName']][time_str]['疑似感染人数'] = r['suspectedCount']
        map_data[r['provinceShortName']][time_str]['治愈人数'] = r['curedCount']
        map_data[r['provinceShortName']][time_str]['死亡人数'] = r['deadCount']

        start_num[r['provinceShortName']]['确诊人数'] = min(start_num[r['provinceShortName']]['确诊人数'], r['confirmedCount'])
        try:
            start_num[r['provinceShortName']]['疑似感染人数'] = min(start_num[r['provinceShortName']]['疑似感染人数'],
                                                          r['suspectedCount'])
        except Exception as e:
            start_num[r['provinceShortName']]['疑似感染人数'] = min(start_num[r['provinceShortName']]['疑似感染人数'],
                                                              0)
            print(r)
        start_num[r['provinceShortName']]['治愈人数'] = min(start_num[r['provinceShortName']]['治愈人数'], r['curedCount'])
        start_num[r['provinceShortName']]['死亡人数'] = min(start_num[r['provinceShortName']]['死亡人数'], r['deadCount'])

    # 修正宁夏起始数量
    start_num['宁夏'] = {
        '确诊人数': 2,
        '治愈人数': 0,
        '死亡人数': 0,
        '疑似感染人数': 0
    }

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
                process_data[t]['确诊人数'] += [[p, start_num[p]['确诊人数']]]
                process_data[t]['治愈人数'] += [[p, start_num[p]['治愈人数']]]
                process_data[t]['死亡人数'] += [[p, start_num[p]['死亡人数']]]
                process_data[t]['疑似感染人数'] += [[p, start_num[p]['疑似感染人数']]]
                continue
            if t in map_data[p]:
                process_data[t]['确诊人数'] += [[p, map_data[p][t]['确诊人数']]]
                process_data[t]['治愈人数'] += [[p, map_data[p][t]['治愈人数']]]
                process_data[t]['死亡人数'] += [[p, map_data[p][t]['死亡人数']]]
                process_data[t]['疑似感染人数'] += [[p, map_data[p][t]['疑似感染人数']]]
            else:
                flag = i - 1
                for j in range(i - 1, -1, -1):
                    tj = time_zone[j]
                    if tj in map_data[p]:
                        process_data[t]['确诊人数'] += [[p, map_data[p][tj]['确诊人数']]]
                        process_data[t]['治愈人数'] += [[p, map_data[p][tj]['治愈人数']]]
                        process_data[t]['死亡人数'] += [[p, map_data[p][tj]['死亡人数']]]
                        process_data[t]['疑似感染人数'] += [[p, map_data[p][tj]['疑似感染人数']]]
                        break
                    flag -= 1
                if flag == -1:
                    process_data[t]['确诊人数'] += [[p, start_num[p]['确诊人数']]]
                    process_data[t]['治愈人数'] += [[p, start_num[p]['治愈人数']]]
                    process_data[t]['死亡人数'] += [[p, start_num[p]['死亡人数']]]
                    process_data[t]['疑似感染人数'] += [[p, start_num[p]['疑似感染人数']]]
    return process_data


def confirmed_map(map_data):
    tl = Timeline()
    for t in map_data:
        map0 = (
            Map()
                .add(
                "确诊人数", [p for p in map_data[t]['确诊人数'] if p[1] != 0],maptype='china'
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=200),
                legend_opts=opts.LegendOpts(is_show=False)
            )
        )
        tl.add(map0, t)
    return tl


if __name__ == '__main__':
    print(update_map())

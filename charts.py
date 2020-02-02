from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo, Page, Map
from pyecharts.globals import ChartType, SymbolType


def geo_base() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-基本示例"),
        )
    )
    return c


def geo_guangdong() -> Geo:
    c = (
        Geo()
        .add_schema(maptype="广东")
        .add(
            "geo",
            [list(z) for z in zip(Faker.guangdong_city, Faker.values())],
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-广东地图"),
        )
    )
    return c


def geo_hainan() -> Geo:
    hainan_city = ['海口市', '三亚市', '琼海市', '儋州市', '定安县', '琼中县']
    c = (
        Geo()
        .add_schema(maptype="海南", center=[109.3, 19.10], zoom=6)
        .add(
            "geo",
            [list(z) for z in zip(hainan_city, Faker.values())],
            type_=ChartType.HEATMAP,
        )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-hainan地图"),
        )
    )
    return c


def map_hainan() -> Geo:
    hainan_city = ['海口市', '三亚市', '琼海市', '儋州市', '定安县', '琼中县']
    c = (
        Map()
        .add(
            "geo",
            [list(z) for z in zip(hainan_city, Faker.values())],
             maptype="海南", center=[109.3, 19.10], zoom=6)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-hainan地图"),
        )
    )
    c.add_js_funcs("""
    chart_%s.on('click', function (param) {
          alert(param.name)
        });"""%c.chart_id)
    print(c.chart_id)
    return c


def map_china() -> Geo:
    c = (
        Map()
        .add(
            "geo",
            [list(z) for z in zip(Faker.provinces, Faker.values())],
             maptype="china")
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(),
            title_opts=opts.TitleOpts(title="Geo-China地图"),
        )
    )
    c.add_js_funcs("""
    chart_%s.on('click', function (param) {
          alert(param.name)
        });"""%c.chart_id)
    print(c.chart_id)
    return c


def gen_map(name, datapair):
    if name=="china":
        n = "中国"
    else:
        n = name
    if name=="海南":
        center = [109.3, 19.10]
        zoom = 6
    else:
        center = None
        zoom = 1
    c = (
        Map()
            .add(
            "确诊病例:人",
            data_pair=datapair[0],
            maptype=name,
            center=center,
            zoom=zoom)
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_= datapair[1]//2),
            title_opts=opts.TitleOpts(title="{}疫情地图".format(n)),
            legend_opts=opts.LegendOpts(is_show=False)
        )
    )
    return Page().add(c).render_embed()


# print(Page().add(map_china()).render())

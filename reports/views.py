from django.shortcuts import render
from django.db import connection, connections
from django.http import HttpResponse
# from django.template import loader
from pyecharts import Bar, Geo, Line, Map


def exc_sql(sql):
    cursor = connections['ora1'].cursor()
    # cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def test(req):
    return HttpResponse('Hello')


def area_report(request):
    ret = """select 省市,注册人数  from report_reg_dis_analyse"""
    max = """select max(注册人数)  from report_reg_dis_analyse"""
    data_list = exc_sql(ret)
    max_v = exc_sql(max)
    attr = [i[0] for i in data_list]
    value = [i[1] for i in data_list]
    map = Map("会员地域注册", width=1150, height=540)
    # type = "effectScatter"：是否有涟漪动画效果。
    # effect_scale = 5：涟漪的多少。
    # symbol = "circle"：标记的形状（circle，pin，rect，diamon，roundRect，arrow，triangle）
    # symbol_size = 20：标记大小
    # symbol_color = "FF0000"：标记颜色
    # geo_normal_color = "#006edd"：地图颜色
    # border_color = "#ffffff"：地图线条颜色
    # geo_emphasis_color = "#0000ff"：鼠标放在地图上的颜色
    # is_label_show = True：显示标签
    # label_text_color = "#00FF00"：标签颜色，本例是绿色
    # label_pos = "inside"：标签位置（inside，top，bottom，left，right）
    # is_visualmap = True：显示图例条
    # visual_range = [0, 300]：图例条范围
    # visual_text_color = '#fff'：图例条颜色
    map.add("各省注册量", attr, value, maptype='china', is_visualmap=True, visual_text_color='#000',
            visual_range=[0, max_v[0][0]], )
    data = {'data': map.render_embed()}
    return render(request, 'reports/registionofarea.html', data)


def reg_report(request):
    # select    province, difi_re_num    from REPORT_REG
    ret = """select 年度,本年度新增,累计详细注册人数 from report_reg_year_analyse"""
    data_list = exc_sql(ret)
    attr = [i[0] for i in data_list]
    value1 = [i[1] for i in data_list]
    value2 = [i[2] for i in data_list]
    line = Line("年度注册情况", width=1100, height=550)
    # line.add("会员按年度统计", attr, value, mark_point=["average"])
    line.add("会员年度新增", attr, value1, is_stack=True, is_label_show=True)
    line.add("会员年度累计", attr, value2, is_stack=True, is_label_show=True)
    data = {'data': line.render_embed()}
    return render(request, 'reports/registionofyear.html', data)


def cur_report(req):
    cols = """select 年度,本年度新增 from report_reg_year_analyse"""
    data_list = exc_sql(cols)
    attr = [i[0] for i in data_list]
    v1 = [i[1] for i in data_list]
    bar = Bar('注册情况', width=1100, height=550)
    bar.add('会员按年度统计', attr, v1, is_stack=True, is_label_show=True)
    data = {'data': bar.render_embed()}
    return render(req, 'reports/registionofm.html', data)

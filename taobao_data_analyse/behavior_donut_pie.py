from main import data
from pyecharts.charts import Pie
from pyecharts import options as opts

# 数据
pv_detail = data.groupby(['behavior_type'])['user_id'].count().reset_index().rename(columns={'user_id':'total_behavior'})
pv_detail_sorted = pv_detail.sort_values(by='total_behavior', ascending=False)

# 提取数据
labels = pv_detail_sorted['behavior_type'].astype(str)
values = pv_detail_sorted['total_behavior']
# 创建环形饼图
pie = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(labels, values)],
        radius=["40%", "70%"],  # 设置内外半径，形成环形
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="环形饼图示例"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(
        label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)")
    )
)

# 渲染图表到 HTML 文件
if __name__ == "__main__":
    pie.render("donut_pie_chart.html")

from main import data
from pyecharts import options as opts
from pyecharts.charts import Funnel


pv_detail = data.groupby(['behavior_type'])['user_id'].count().reset_index().rename(columns={'user_id':'total_behavior'})
pv_detail_sorted = pv_detail.sort_values(by='total_behavior', ascending=False)

# 提取数据
labels = pv_detail_sorted['behavior_type'].astype(str)
values = pv_detail_sorted['total_behavior']

# 创建漏斗图
funnel = (
    Funnel()
    .add(
        series_name="行为类型_小时漏斗图",
        data_pair=list(zip(labels, values)),
        gap=2,
        tooltip_opts=opts.TooltipOpts(trigger="item", formatter="{a} <br/>{b} : {c}"),
        label_opts=opts.LabelOpts(position="inside"),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="行为类型漏斗图"))
)

if __name__ == "__main__":
    funnel.render("行为类型漏斗图.html")





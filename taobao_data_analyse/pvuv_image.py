import pandas as pd
from main import data


# 定义函数，可以通过接收的key值进行分组，返回pv和uv
def cal_pvuv(key = ''):
    pv = data.groupby(key)['user_id'].count()
    pv.name = 'pv'
    uv = data.groupby(key)['user_id'].apply(lambda x: x.drop_duplicates().count())
    uv.name = 'uv'
    return pd.concat([pv,uv], axis = 1).reset_index()


if __name__ == '__main__':
    pvuv_daily = cal_pvuv('date')  # 得到按日期聚合的pv和uv数据
    pvuv_daily.plot(x='date', secondary_y='uv', grid=True, figsize=(10, 5))
    # 接下来按照小时去分析用户的行为习惯：
    pvuv_hour = cal_pvuv('hour')
    pvuv_hour.plot(x='hour', secondary_y='uv', grid=True, figsize=(10, 5),
                   xticks=[x for x in range(24)], title='pvuv_hour')
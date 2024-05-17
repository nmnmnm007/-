import datetime
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
columns = ['user_id','item_id','category_id','behavior_type', 'timestamp']
df = pd.read_csv('UserBehavior.csv', names=columns, iterator=True)
data = df.get_chunk(1000000) # 获取100W数据

# 将时间戳转换为北京时间
data['timestamp'] = pd.to_datetime(data.timestamp, unit='s') + datetime.timedelta(hours = 8)
# 将日期提取出来，这种方法提取出的日期需要进一步处理为datetime64格式
data['date'] = data['timestamp'].dt.date
data['date'] = pd.to_datetime(data['date'])
# 将时间取出来
data['time'] = data['timestamp'].dt.time
# 将小时提取出来
data['hour'] = data['timestamp'].dt.hour


# 判断是否有缺失值
# print(data.isnull().sum())

# 异常值处理，时间超出给定范围的即为异常值
data = data[(data['timestamp'] >= '2017-11-25') & (data['timestamp'] < '2017-12-4')]

# 查看是否有重复值
# print(data.duplicated().value_counts())
# 删除重复值
# data = data.drop_duplicates(keep = 'first',inplace = False) # 去除重复值

# 重新排序、索引
data = data.sort_values(by = ['timestamp','user_id'], ascending=True)
data = data.reset_index(drop=True)
# print(data.describe())


plt.show()
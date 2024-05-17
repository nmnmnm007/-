import pandas as pd
import matplotlib.pyplot as plt
from main import data

# 筛选出产生购买行为的数据
data_buy = data[data['behavior_type'] == 'buy']

# 计算各种商品大类的交易数
buy_category = data_buy[['category_id','behavior_type']].groupby('category_id').count().rename(columns = {'behavior_type':'buy_count'})

# 整理各种商品大类的交易数
buy_category = buy_category.sort_values('buy_count',ascending=False).reset_index()

# 将产生购买行为的数据和原数据外连接，进而得到有购买记录的商品大类的其他行为信息
behav_category = pd.merge(data_buy[['user_id','category_id']], data,
                                 on = ['user_id','category_id'], how = 'left')
# 计算各种商品大类的行为数
behav_category = behav_category[['category_id', 'behavior_type']].groupby('category_id').count().reset_index().rename(columns={'behavior_type':'behavior_count'})

# 统计分析各种商品大类的购买数和产生行为数
if __name__ == '__main__':
    buy_behav_category = pd.merge(buy_category, behav_category, on = 'category_id', how = 'inner')
    buy_behav_category = buy_behav_category.assign(behav_per_buy = buy_behav_category['behavior_count'] / buy_behav_category['buy_count'])

    # 生成散点图
    plt.figure(figsize=(10, 6))
    plt.scatter(buy_behav_category['behav_per_buy'], buy_behav_category['buy_count'])
    plt.xlabel('Behavior per Buy')
    plt.ylabel('Buy Count')
    plt.title('Scatter Plot of Behavior per Buy vs Buy Count')
    plt.grid(True)
    plt.show()
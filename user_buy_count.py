from main import data
import matplotlib.pyplot as plt
import pandas as pd

# 过滤出购买行为的记录
buy_data = data[data['behavior_type'] == 'buy']

# 计算每个用户的购买次数
user_buy_counts = buy_data.groupby('user_id').size()

# 统计每个购买次数的用户数量
purchase_distribution = user_buy_counts.value_counts().sort_index()

# 设置购买次数的上限为 15，并合并大于 15 次购买的用户数量
max_count = 15
greater_than_15_count = purchase_distribution[purchase_distribution.index > max_count].sum()

# 删除索引大于 15 的项
purchase_distribution = purchase_distribution[purchase_distribution.index <= max_count]

# 追加 '>15' 类别
purchase_distribution.loc['>15'] = greater_than_15_count

# 可视化
if __name__ == '__main__':
    plt.figure(figsize=(10, 6))
    plt.bar(purchase_distribution.index.astype(str), purchase_distribution.values)
    plt.xlabel('Total Buy Count')
    plt.ylabel('User Count')
    plt.title('User Distribution by Purchase Count')
    plt.grid(True)
    plt.show()
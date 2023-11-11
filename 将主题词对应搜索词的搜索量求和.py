#!/usr/bin/env python
# coding: utf-8

# In[3]:


cd C:\Users\小帅\Downloads


# In[4]:


import pandas as pd

# 读取Excel文件
df = pd.read_excel('crv_exact-match_us_2023-11-11.xlsx')

# 确保Keyword列和待匹配列是字符串类型
df['Keyword'] = df['Keyword'].astype(str)
df['待匹配'] = df['待匹配'].astype(str)

# 初始化求和列
df['求和'] = 0

# 遍历待匹配列中的每一行
for index, row in df.iterrows():
    # 获取待匹配列中的单词列表
    match_words = row['待匹配'].lower().split()
    # 初始化求和变量
    sum_volume = 0
    # 遍历Keyword列，查找匹配的单词
    for a_index, a_row in df.iterrows():
        # 如果待匹配列中的所有单词都在Keyword列的字符串中
        if all(word in a_row['Keyword'].lower() for word in match_words):
            # 累加Volume列的值
            sum_volume += a_row['Volume']
    # 将求和结果赋值给求和列
    df.at[index, '求和'] = sum_volume

# 将结果保存回Excel文件
df.to_excel('crv_exact-match_us_2023-11-11（结果）.xlsx', index=False)


# In[ ]:





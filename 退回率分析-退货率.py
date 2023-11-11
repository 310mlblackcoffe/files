#!/usr/bin/env python
# coding: utf-8

# In[4]:


cd C:\Users\小帅\Desktop\退货率调研分析\退货率长期跟踪\退货率周跟进


# In[9]:


import pandas as pd

# 读取三个CSV文件
file1_path = "销量统计-ASIN-20230101-20231106.csv"
file2_path = "FBA退货列表20230101-20231106.csv"
file3_path = "售后问题描述计数20230101-20231106.csv"

df1 = pd.read_csv(file1_path)
df2 = pd.read_csv(file2_path)
df3 = pd.read_csv(file3_path)

# 选择需要的列
df1_selected = df1[["日期ASIN组合", "日期", "sku", "品名", "ASIN", "求和项:销量"]]
df2_selected = df2[["日期ASIN组合", "日期", "sku", "品名", "ASIN", "求和项:退货数量"]]
df3_selected = df3[["日期ASIN组合", "日期", "sku", "品名", "ASIN", "计数项:问题描述"]]

# 分步合并三个数据框
merged_df_12 = pd.merge(df1_selected, df2_selected, on="日期ASIN组合", how="outer")
merged_df = pd.merge(merged_df_12, df3_selected, on="日期ASIN组合", how="outer")

# 保存到新的CSV文件，使用“带BOM的UTF-8”格式
merged_df.to_csv("merged_data-new.csv", index=False, encoding="utf-8-sig")

print("数据处理完成，已保存到merged_data-new.csv文件中。")


# In[ ]:





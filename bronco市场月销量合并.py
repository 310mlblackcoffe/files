#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:\Users\小帅\Downloads\8-9月-bronco\原始数据\验证


# In[23]:


import pandas as pd

# 读取四个EXCEL文件
file1_path = "Product-Automotive-US-bronco-大于20-2023.07-9666（标注车型）（剔除其他车型）（标注产品名称）(排除sport).xlsx"
file2_path = "Product-Automotive-US-bronco-2023.08-大于50（标注车型）（排除其他车型）(排除sport)（标注产品名称）.xlsx"
file3_path = "Product-Automotive-US-bronco-2023.09-大于50（标注车型）（排除其他车型）(排除sport)（标注产品名称）.xlsx"
file4_path = "Product-Automotive-US-bronco-大于20-2023.10-27287（标注车型）（剔除其他车型）（标注产品名称）(排除sport).xlsx"

df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
df3 = pd.read_excel(file3_path)
df4 = pd.read_excel(file4_path)

# 选择需要的列
df1_selected = df1[["ASIN","品牌_7","商品名称_7","bronco/bronco sport_7","7月子体月销量","7月子体月销售额"]]
df2_selected = df2[["ASIN","品牌_8","商品名称_8","bronco/bronco sport_8","8月子体月销量","8月子体月销售额"]]
df3_selected = df3[["ASIN","品牌_9","商品名称_9","bronco/bronco sport_9","9月子体月销量","9月子体月销售额"]]
df4_selected = df4[["ASIN","品牌_10","商品名称_10","bronco/bronco sport_10","10月子体月销量","10月子体月销售额"]]

# 分步合并四个数据框
merged_df_12 = pd.merge(df1_selected, df2_selected, on="ASIN", how="outer")
merged_df_123 = pd.merge(merged_df_12, df3_selected, on="ASIN", how="outer")
merged_df = pd.merge(merged_df_123, df4_selected, on="ASIN", how="outer")

# 保存到新的EXCEL文件
merged_df.to_excel("merged_data-new.xlsx", index=False)

print("数据处理完成，已保存到merged_data-new.xlsx文件中。")


# In[ ]:





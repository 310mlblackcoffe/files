#!/usr/bin/env python
# coding: utf-8

# In[3]:


cd C:\Users\小帅\Downloads\8-9月-bronco\原始数据\验证\10月


# In[4]:


import pandas as pd

# 读取Excel文件
file_path = 'Product-Automotive-US-bronco-大于20-2023.10-27287（标注车型）（剔除其他车型）（标注产品名称）.xlsx'  # 替换成你的文件路径
df = pd.read_excel(file_path)

# 定义一个函数来标注标题
def label_title(row):
    title = row['商品标题'].lower()
    if 'bronco' in title and ('not' in title or "don't" in title or "Excluding" in title):
        return 'bronco'
    elif 'bronco' in title and 'sport' not in title:
        return 'bronco'
    else:
        return 'bronco sport'

# 在DataFrame中添加新的列
df['bronco/bronco sport'] = df.apply(label_title, axis=1)

# 导出带有新列的Excel文件
output_file_path = 'Product-Automotive-US-bronco-大于20-2023.10-27287（标注车型）（剔除其他车型）（标注产品名称）(排除sport).xlsx'  # 替换成你想要的输出文件路径
df.to_excel(output_file_path, index=False)

print("处理完成，已导出到", output_file_path)


# In[ ]:





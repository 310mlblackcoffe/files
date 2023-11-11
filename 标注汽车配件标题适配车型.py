#!/usr/bin/env python
# coding: utf-8

# In[5]:


cd C:\Users\小帅\Downloads\8-9月-bronco\原始数据\验证\10月


# In[6]:


import pandas as pd
import re

# 读取文档1和文档2
df1 = pd.read_excel('品牌k+车型k.xlsx')
df2 = pd.read_excel('Product-Automotive-US-bronco-大于20-2023.10-27287.xlsx')

# 将汽车品牌和车型列转换为字符串类型
df1['品牌'] = df1['品牌'].astype(str)
df1['车型'] = df1['车型'].astype(str)

# 提取汽车品牌和车型列表
car_brands = df1['品牌'].unique()
car_models = df1['车型'].unique()

# 创建一个函数来标注行
def annotate_row(row):
    title = str(row['商品标题'])  # 将商品标题转换为字符串类型
    title_lower = title.lower()
    brand_count = 0
    for brand in car_brands:
        if re.search(r'\b' + re.escape(brand) + r'\b', title, re.IGNORECASE):
            brand_count += 1
            if brand_count > 2:
                return '通用 | 匹配到过多品牌'
    model_count = 0
    for model in car_models:
        if re.search(r'\b' + re.escape(model) + r'\b', title, re.IGNORECASE):
            model_count += 1
    if model_count > 0:
        return '专用'
    else:
        return '通用 | 未匹配到车型'

# 在文档2中添加一列用于标注
df2['标注'] = df2.apply(annotate_row, axis=1)

# 创建一个函数来添加适用的汽车品牌和车型
def add_applicable_info(row):
    if '通用' in row['标注'] and '未匹配到车型' in row['标注']:
        return '未匹配到车型'
    elif '通用' in row['标注'] and '匹配到过多品牌' in row['标注']:
        matching_brands = [brand for brand in car_brands if re.search(r'\b' + re.escape(brand) + r'\b', row['商品标题'])]
        return ', '.join(matching_brands)
    elif '专用' in row['标注']:
        applicable_brands = [brand for brand in car_brands if re.search(r'\b' + re.escape(brand) + r'\b', row['商品标题'])]
        applicable_models = [model for model in car_models if re.search(r'\b' + re.escape(model) + r'\b', row['商品标题'])]
        return ', '.join(applicable_brands) + ' | ' + ', '.join(applicable_models)
    else:
        return ''

# 在文档2中添加一列用于适用的汽车品牌和车型
df2['适用车型'] = df2.apply(add_applicable_info, axis=1)



# 创建一个函数来提取匹配的年份信息
def extract_years(row):
    title = str(row['商品标题'])  # 将商品标题转换为字符串类型
    years = re.findall(r'\b\d{4}\b', title)
    return ' | '.join(years)


# 在文档2中添加一列用于标注的年份信息
df2['年份信息'] = df2.apply(extract_years, axis=1)


# 保存标注和适用车型的文档2
df2.to_excel('Product-Automotive-US-bronco-大于20-2023.10-27287（标注车型）.xlsx', index=False)


# In[ ]:





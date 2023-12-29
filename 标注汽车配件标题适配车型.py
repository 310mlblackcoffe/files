import pandas as pd
import re

# 读取文档1和文档2
df1 = pd.read_excel('品牌k+车型k.xlsx')
df2 = pd.read_excel('maverick全量-2023.11.27-2023.12.27.xlsx')

# 将汽车品牌和车型列转换为字符串类型
df1['品牌'] = df1['品牌'].astype(str)
df1['车型'] = df1['车型'].astype(str)
df1['车种分级'] = df1['车种分级'].astype(str)
df1['标签'] = df1['标签'].astype(str)
df1['座椅配置'] = df1['座椅配置'].astype(str)
df1['动力'] = df1['动力'].astype(str)



# 提取汽车品牌和车型列表
car_brands = df1['品牌'].unique()
car_models = df1['车型'].unique()
car_types = df1['车种分级'].unique()
car_tags = df1['标签'].unique()
car_seats = df1['座椅配置'].unique()
car_power = df1['动力'].unique()


# 创建一个函数来标注行
def annotate_row(row):
    title = str(row['商品标题'])  # 将商品标题转换为字符串类型
    title_lower = title.lower()
    brand_count = 0
    for brand in car_brands:
        if re.search(r'\b' + re.escape(brand) + r'\b', title, re.IGNORECASE):
            brand_count += 1
            if brand_count > 3:
                return '匹配到过多品牌'
    model_count = 0
    for model in car_models:
        if re.search(r'\b' + re.escape(model) + r'\b', title, re.IGNORECASE):
            model_count += 1
    if model_count > 5:
        return '匹配到过多车型'
    elif model_count > 0:
        return '专用'
    else:
        return '未匹配到车型'


# 在文档2中添加一列用于标注
df2['标注'] = df2.apply(annotate_row, axis=1)

def add_applicable_info(row):
    if '未匹配到车型' in row['标注']:
        return '', '', '', '', '', ''
    elif '匹配到过多品牌' in row['标注']:
        applicable_brands = [brand for brand in car_brands if re.search(r'\b' + re.escape(brand) + r'\b', row['商品标题'], re.IGNORECASE)]
        applicable_models = [model for model in car_models if re.search(r'\b' + re.escape(model) + r'\b', row['商品标题'], re.IGNORECASE)]
        return ', '.join(applicable_brands), ', '.join(applicable_models), '', '', '', ''
    elif '匹配到过多车型' in row['标注']:
        applicable_brands = [brand for brand in car_brands if re.search(r'\b' + re.escape(brand) + r'\b', row['商品标题'], re.IGNORECASE)]
        applicable_models = [model for model in car_models if re.search(r'\b' + re.escape(model) + r'\b', row['商品标题'], re.IGNORECASE)]
        return ', '.join(applicable_brands), ', '.join(applicable_models), '', '', '', ''
    elif '专用' in row['标注']:
        applicable_brands = [brand for brand in car_brands if re.search(r'\b' + re.escape(brand) + r'\b', row['商品标题'], re.IGNORECASE)]
        applicable_models = [model for model in car_models if re.search(r'\b' + re.escape(model) + r'\b', row['商品标题'], re.IGNORECASE)]
        matching_model = applicable_models[0] if applicable_models else ''
        matching_info = df1[df1['车型'] == matching_model][['车种分级', '标签', '座椅配置', '动力']]
        return ', '.join(applicable_brands), ', '.join(applicable_models), ', '.join(matching_info['车种分级']), ', '.join(matching_info['标签']), ', '.join(matching_info['座椅配置']), ', '.join(matching_info['动力'])
    else:
        return '', '', '', '', '', ''


# 在文档2中添加列 '适用品牌'、'适用车型'、'车种分级'、'标签'、'座椅配置'、'动力'
df2[['适用品牌', '适用车型', '车种分级', '标签', '座椅配置', '动力']] = df2.apply(add_applicable_info, axis=1, result_type='expand')


# 创建一个函数来提取匹配的年份信息，并排序去重，然后只保留最小值和最大值
def extract_min_max_years(row):
    title = str(row['商品标题'])  # 将商品标题转换为字符串类型
    years = sorted(set(map(int, re.findall(r'\b(?:199|200|201|202)\d\b', title))))
    
    if years:
        min_year = min(years)
        max_year = max(years)
        return f"{min_year} | {max_year}"
    else:
        return ""

# 在文档2中添加一列用于标注的年份信息（经过排序去重，只保留最小值和最大值）
df2['年份信息'] = df2.apply(extract_min_max_years, axis=1)

# 保存标注、适用车型和车种分级的文档2
df2.to_excel('maverick全量-2023.11.27-2023.12.27（标注车型）.xlsx', index=False)

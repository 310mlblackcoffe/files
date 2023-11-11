#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:\Users\小帅\Desktop\bronco市场周报\bronco ABA搜索词趋势


# In[24]:


import pandas as pd

def process_excel(input_file_path, output_file_path):
    # 读取Excel文件
    df = pd.read_excel(input_file_path, skiprows=1)
    
    # 提取所需列
    df_selected = df[['关键词', '关键词翻译', '周搜索量', '现排名', '点击集中度', '点击前三ASIN', '点击前三品牌']].copy()
    
    # 添加“TOP1点击集中度”、“TOP2点击集中度”、“TOP3点击集中度”这几列
    df_selected['TOP1点击集中度'] = df_selected['点击集中度'].apply(lambda x: x.split('\n')[0].split(': ')[1] if pd.notnull(x) and x.split('\n')[0].split(': ')[1] != '-' else None)
    df_selected['TOP2点击集中度'] = df_selected['点击集中度'].apply(lambda x: x.split('\n')[1].split(': ')[1] if pd.notnull(x) and x.split('\n')[1].split(': ')[1] != '-' else None)
    df_selected['TOP3点击集中度'] = df_selected['点击集中度'].apply(lambda x: x.split('\n')[2].split(': ')[1] if pd.notnull(x) and x.split('\n')[2].split(': ')[1] != '-' else None)
    
    # 添加“点击第一ASIN”、“点击第二ASIN”、“点击第三ASIN”这几列
    df_selected['点击第一ASIN'] = df_selected['点击前三ASIN'].apply(lambda x: x.split('、')[0] if pd.notnull(x) and '、' in x else x)
    df_selected['点击第二ASIN'] = df_selected['点击前三ASIN'].apply(lambda x: x.split('、')[1] if pd.notnull(x) and '、' in x and len(x.split('、')) > 1 else None)
    df_selected['点击第三ASIN'] = df_selected['点击前三ASIN'].apply(lambda x: x.split('、')[2] if pd.notnull(x) and '、' in x and len(x.split('、')) > 2 else None)

    # 添加“点击第一品牌”、“点击第二品牌”、“点击第三品牌”这几列
    df_selected['点击第一品牌'] = df_selected['点击前三品牌'].apply(lambda x: x.split('、')[0] if pd.notnull(x) and '、' in x else x)
    df_selected['点击第二品牌'] = df_selected['点击前三品牌'].apply(lambda x: x.split('、')[1] if pd.notnull(x) and '、' in x and len(x.split('、')) > 1 else None)
    df_selected['点击第三品牌'] = df_selected['点击前三品牌'].apply(lambda x: x.split('、')[2] if pd.notnull(x) and '、' in x and len(x.split('、')) > 2 else None)     
    
     # 将除了'关键词'和'关键词翻译'之外的所有列名前加上“31周”
    df_selected.columns = [col if col in ['关键词', '关键词翻译'] else '42周' + col for col in df_selected.columns]   
    
    # 将处理后的内容输出到一个新的Excel文件
    df_selected.to_excel(output_file_path, index=False)
    print(f"Processed data has been saved to {output_file_path}")

# 定义输入和输出文件路径
input_file_path = 'ABAKeywordTrend-US-bronco-2023第42周(1015~1021).xlsx'
output_file_path = 'New-ABAKeywordTrend-US-bronco-2023第42周(1015~1021).xlsx'

# 运行脚本
process_excel(input_file_path, output_file_path)


# In[43]:


import pandas as pd

# 读取十二个XLSX文件
file1_path = "New-ABAKeywordTrend-US-bronco-2023第31周(0730~0805).xlsx"
file2_path = "New-ABAKeywordTrend-US-bronco-2023第32周(0806~0812).xlsx"
file3_path = "New-ABAKeywordTrend-US-bronco-2023第33周(0813~0819).xlsx"
file4_path = "New-ABAKeywordTrend-US-bronco-2023第34周(0820~0826).xlsx"
file5_path = "New-ABAKeywordTrend-US-bronco-2023第35周(0827~0902).xlsx"
file6_path = "New-ABAKeywordTrend-US-bronco-2023第36周(0903~0909).xlsx"
file7_path = "New-ABAKeywordTrend-US-bronco-2023第37周(0910~0916).xlsx"
file8_path = "New-ABAKeywordTrend-US-bronco-2023第38周(0917~0923).xlsx"
file9_path = "New-ABAKeywordTrend-US-bronco-2023第39周(0924~0930).xlsx"
file10_path = "New-ABAKeywordTrend-US-bronco-2023第40周(1001~1007).xlsx"
file11_path = "New-ABAKeywordTrend-US-bronco-2023第41周(1008~1014).xlsx"
file12_path = "New-ABAKeywordTrend-US-bronco-2023第42周(1015~1021).xlsx"


df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)
df3 = pd.read_excel(file3_path)
df4 = pd.read_excel(file4_path)
df5 = pd.read_excel(file5_path)
df6 = pd.read_excel(file6_path)
df7 = pd.read_excel(file7_path)
df8 = pd.read_excel(file8_path)
df9 = pd.read_excel(file9_path)
df10 = pd.read_excel(file10_path)
df11 = pd.read_excel(file11_path)
df12 = pd.read_excel(file12_path)


# 选择需要的列
df1_selected = df1.copy()
df2_selected = df2.copy()
df3_selected = df3.copy()
df4_selected = df4.copy()
df5_selected = df5.copy()
df6_selected = df6.copy()
df7_selected = df7.copy()
df8_selected = df8.copy()
df9_selected = df9.copy()
df10_selected = df10.copy()
df11_selected = df11.copy()
df12_selected = df12.copy()

# 分步合并十二个数据框
merged_df_12 = pd.merge(df1_selected, df2_selected, on="关键词", how="outer")
merged_df_123 = pd.merge(merged_df_12, df3_selected, on="关键词", how="outer")
merged_df_1234 = pd.merge(merged_df_123, df4_selected, on="关键词", how="outer")
merged_df_12345 = pd.merge(merged_df_1234, df5_selected, on="关键词", how="outer")
merged_df_123456 = pd.merge(merged_df_12345, df6_selected, on="关键词", how="outer")
merged_df_1234567 = pd.merge(merged_df_123456, df7_selected, on="关键词", how="outer")
merged_df_12345678 = pd.merge(merged_df_1234567, df8_selected, on="关键词", how="outer")
merged_df_123456789 = pd.merge(merged_df_12345678, df9_selected, on="关键词", how="outer")
merged_df_12345678910 = pd.merge(merged_df_123456789, df10_selected, on="关键词", how="outer")
merged_df_1234567891011 = pd.merge(merged_df_12345678910, df11_selected, on="关键词", how="outer")
merged_df_all = pd.merge(merged_df_1234567891011, df12_selected, on="关键词", how="outer")

# 保存到新的XLSX文件
merged_df_all.to_excel("merged_data-new.xlsx", index=False)

print("数据处理完成，已保存到merged_data-new.xlsx文件中。")


# In[ ]:





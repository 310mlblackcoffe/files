#!/usr/bin/env python
# coding: utf-8

# In[1]:


cd C:\Users\小帅\Downloads


# In[2]:


python chance-cars.py


# In[4]:


import requests
from bs4 import BeautifulSoup
html_content = '''
<img alt="preview for 2023 Honda CR-V: Car and Driver 10Best" title="Video player poster image" loading="lazy" width="2000" height="1000" decoding="async" data-nimg="1" style="color: transparent; width: 100%; height: auto;" sizes="100vw" srcset="https://hips.hearstapps.com/vidthumb/images/honda-cr-v-1673564951.jpg?crop=1.00xw:1.00xh;0,0&amp;resize=640:* 640w, https://hips.hearstapps.com/vidthumb/images/honda-cr-v-1673564951.jpg?crop=1.00xw:1.00xh;0,0&amp;resize=980:* 980w, https://hips.hearstapps.com/vidthumb/images/honda-cr-v-1673564951.jpg?crop=1.00xw:1.00xh;0,0&amp;resize=1024:* 1120w, https://hips.hearstapps.com/vidthumb/images/honda-cr-v-1673564951.jpg?crop=1.00xw:1.00xh;0,0&amp;resize=1120:* 1200w, https://hips.hearstapps.com/vidthumb/images/honda-cr-v-1673564951.jpg?crop=1.00xw:1.00xh;0,0&amp;resize=1200:* 1920w" src="https://hips.hearstapps.com/vidthumb/images/honda-cr-v-1673564951.jpg?crop=1.00xw:1.00xh;0,0&amp;resize=1200:*" class="e1f7ylgd5 css-g939jb exi4f7p0">
'''
soup = BeautifulSoup(html_content, 'html.parser')
for img_tag in soup.find_all('img'):
    img_url = img_tag['src']
    alt_text = img_tag['alt']

    # 使用alt文本作为文件名，并将不合法的文件名字符替换为下划线
    filename = "".join(c if c.isalnum() else "_" for c in alt_text) + ".jpg"

    img_data = requests.get(img_url).content
    with open(filename, 'wb') as handler:
        handler.write(img_data)


# In[31]:


import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 读取Excel文件
excel_path = '机会车型图片html片段.xlsx'
df = pd.read_excel(excel_path)

# 创建文件夹并下载图片
for index, row in df.iterrows():
    folder_name = row['详情标题']
    html_content = row['字段7']
    
    # 使用B列文本作为文件夹名，并将不合法的文件夹名字符替换为下划线
    folder_name = "".join(c if c.isalnum() else "_" for c in folder_name)
    
    # 创建文件夹
    os.makedirs(folder_name, exist_ok=True)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for img_tag in soup.find_all('img'):
        img_url = img_tag['src']
        
        # 获取原始图片文件名
        img_filename = os.path.basename(img_url)
        
        img_filepath = os.path.join(folder_name, img_filename)
        
        # 检查文件是否已存在，如果存在则覆盖
        overwrite_count = 0
        if os.path.exists(img_filepath):
            # 文件已存在,判断是否超过覆盖次数
            if overwrite_count >= 1:
                print(f"文件 {img_filepath} 覆盖次数已达上限,跳过下载。")    
            else:
                # 覆盖次数尚可,打印日志并下载
                overwrite_count += 1
                print(f"文件已存在,这是第 {overwrite_count} 次覆盖下载。")

        
        # 添加重试机制和超时设置
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                img_data = requests.get(img_url, timeout=10).content
                
                with open(img_filepath, 'wb') as handler:
                    handler.write(img_data)
                break  # 成功下载后跳出循环
            except requests.exceptions.ConnectionError as e:
                print(f"下载失败，重试中 ({retry_count + 1}/{max_retries})...")
                retry_count += 1

print("批量处理完成！")


# In[23]:


cd D:\机会车型图片


# In[32]:


import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 读取Excel文件
excel_path = '后羿采集carbuzz机会车型相册链接.xlsx'
df = pd.read_excel(excel_path)

# 创建文件夹并下载图片
for index, row in df.iterrows():
    folder_name = row['车型']
    html_content = row['字段9']
    
    # 使用B列文本作为文件夹名，并将不合法的文件夹名字符替换为下划线
    folder_name = "".join(c if c.isalnum() else "_" for c in folder_name)
    
    # 创建文件夹
    os.makedirs(folder_name, exist_ok=True)
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    for img_tag in soup.find_all('img'):
        img_url = img_tag['src']
        
        # 获取原始图片文件名
        img_filename = os.path.basename(img_url)
        
        img_filepath = os.path.join(folder_name, img_filename)
        
        # 检查文件是否已存在，如果存在则覆盖
        overwrite_count = 0
        if os.path.exists(img_filepath):
            # 文件已存在,判断是否超过覆盖次数
            if overwrite_count >= 1:
                print(f"文件 {img_filepath} 覆盖次数已达上限,跳过下载。")    
            else:
                # 覆盖次数尚可,打印日志并下载
                overwrite_count += 1
                print(f"文件已存在,这是第 {overwrite_count} 次覆盖下载。")

        
        # 添加重试机制和超时设置
        max_retries = 3
        retry_count = 0
        while retry_count < max_retries:
            try:
                img_data = requests.get(img_url, timeout=10).content
                
                with open(img_filepath, 'wb') as handler:
                    handler.write(img_data)
                break  # 成功下载后跳出循环
            except requests.exceptions.ConnectionError as e:
                print(f"下载失败，重试中 ({retry_count + 1}/{max_retries})...")
                retry_count += 1

print("批量处理完成！")


# In[ ]:





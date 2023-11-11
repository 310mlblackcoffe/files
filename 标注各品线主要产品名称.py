#!/usr/bin/env python
# coding: utf-8

# In[10]:


cd C:\Users\小帅\Downloads\8-9月-bronco\原始数据\验证


# In[11]:


import pandas as pd
import re  # 导入re模块

# 读取文档2
df2 = pd.read_excel('product-automotive-us-bronco-2023.09-大于50（标注车型）（排除其他车型）(排除sport).xlsx')

# 创建一个函数来标注商品
def annotate_product(row):
    title = str(row['商品标题'])  # 将商品标题转换为字符串类型
    title_lower = title.lower()
    
    # 定义用于匹配完整单词的正则表达式模式
    word_pattern = r'\b{}\b'.format

    # 使用正则表达式匹配关键词
    if (re.search(word_pattern("floor"), title_lower) or re.search(word_pattern("row liners"), title_lower) or re.search(word_pattern("row liner"), title_lower)) and (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("backrest"), title_lower) or re.search(word_pattern("seat back"), title_lower) or re.search(word_pattern("seats back"), title_lower) or re.search(word_pattern("dog seat liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "后备箱垫+椅背垫+脚垫"
    elif (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("sidewall"), title_lower)) and (re.search(word_pattern("protector"), title_lower) or re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "后备箱两侧垫"
    elif (re.search(word_pattern("floor"), title_lower) or re.search(word_pattern("row liners"), title_lower) or re.search(word_pattern("row liner"), title_lower)) and (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "后备箱垫+脚垫"
    elif (re.search(word_pattern("floor"), title_lower) or re.search(word_pattern("row liners"), title_lower) or re.search(word_pattern("row liner"), title_lower)) and (re.search(word_pattern("backrest"), title_lower) or re.search(word_pattern("seat back"), title_lower) or re.search(word_pattern("seats back"), title_lower) or re.search(word_pattern("dog seat liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "椅背垫+脚垫"
    elif (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("backrest"), title_lower) or re.search(word_pattern("seat back"), title_lower) or re.search(word_pattern("seats back"), title_lower) or re.search(word_pattern("dog seat liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "后备箱垫+椅背垫"
    elif (re.search(word_pattern("cargo cover"), title_lower) or re.search(word_pattern("security shield shade"), title_lower) or re.search(word_pattern("security shade cover shield"), title_lower)):
        return "遮物帘"
    elif (re.search(word_pattern("trunk grocery bag hooks"), title_lower) or re.search(word_pattern("trunk hook"), title_lower) or re.search(word_pattern("trunk hooks"), title_lower)):
        return "后备箱挂钩"
    elif (re.search(word_pattern("floor"), title_lower) or re.search(word_pattern("floorliners"), title_lower) or re.search(word_pattern("row liners"), title_lower) or re.search(word_pattern("row liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "脚垫单品"
    elif (re.search(word_pattern("seat covers"), title_lower) or re.search(word_pattern("seat cover"), title_lower)) and (not re.search(word_pattern("back"), title_lower)) :
        return "座椅套"
    elif (re.search(word_pattern("backrest"), title_lower) or re.search(word_pattern("seat back"), title_lower) or re.search(word_pattern("seats back"), title_lower) or re.search(word_pattern("dog seat liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("mat"), title_lower) or re.search(word_pattern("protector"), title_lower)):
        return "椅背垫单品"
    elif (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower) or re.search(word_pattern("tub rail"), title_lower)) and (re.search(word_pattern("side covers"), title_lower) or re.search(word_pattern("side cover"), title_lower) or re.search(word_pattern("side protector"), title_lower) or re.search(word_pattern("edge protector"), title_lower)):
        return "后备箱侧沿护板"
    elif (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        return "后备箱垫单品"

    elif (re.search(word_pattern("car cover"), title_lower) or re.search(word_pattern("car covers"), title_lower)):
        return "车衣"
    elif (re.search(word_pattern("snow cover"), title_lower) or re.search(word_pattern("snow covers"), title_lower)):
        return "雪挡"
    elif (re.search(word_pattern("rain guard"), title_lower) or re.search(word_pattern("rain guards"), title_lower) or re.search(word_pattern("side window visor deflectors"), title_lower)):
        return "晴雨挡"
    elif (re.search(word_pattern("roof"), title_lower) or re.search(word_pattern("top"), title_lower)) and (re.search(word_pattern("sunshade"), title_lower) or re.search(word_pattern("sun shade"), title_lower)):
        return "车顶遮阳"
    elif (re.search(word_pattern("mud flaps"), title_lower) or re.search(word_pattern("mud flap"), title_lower) or re.search(word_pattern("mudguard"), title_lower) or re.search(word_pattern("mudguards"), title_lower) or re.search(word_pattern("mud guards"), title_lower) or re.search(word_pattern("splash guards"), title_lower)):
        return "挡泥板"
    elif (re.search(word_pattern("windshield"), title_lower) or re.search(word_pattern("window"), title_lower) or re.search(word_pattern("windows"), title_lower)) and (re.search(word_pattern("sunshade"), title_lower) or re.search(word_pattern("shades"), title_lower) or re.search(word_pattern("sun shade"), title_lower) or re.search(word_pattern("sun visor"), title_lower) or re.search(word_pattern("sunshades"), title_lower)):
        return "遮阳挡"
    elif (re.search(word_pattern("front"), title_lower) or re.search(word_pattern("rear"), title_lower) or re.search(word_pattern("interior"), title_lower)) and (re.search(word_pattern("ceiling lights"), title_lower) or re.search(word_pattern("ceiling light"), title_lower) or re.search(word_pattern("reading lights"), title_lower) or re.search(word_pattern("dome lights"), title_lower) or re.search(word_pattern("dome light"), title_lower) or re.search(word_pattern("roof map light"), title_lower)):
        return "阅读灯/内顶灯"
    elif (re.search(word_pattern("glove box"), title_lower)) and (re.search(word_pattern("dividers"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("partition"), title_lower)):
        return "手套箱隔板"
    elif (re.search(word_pattern("dash"), title_lower) or re.search(word_pattern("dashboard"), title_lower) or re.search(word_pattern("screen"), title_lower)) and (re.search(word_pattern("holder"), title_lower) or re.search(word_pattern("mount"), title_lower) or re.search(word_pattern("bracket"), title_lower)):
        return "仪表台支架"
    elif (re.search(word_pattern("dash"), title_lower) or re.search(word_pattern("dashboard"), title_lower) or re.search(word_pattern("screen"), title_lower)) and (re.search(word_pattern("pad"), title_lower) or re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("mat"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("storage"), title_lower) or re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("organizer"), title_lower)):
        return "仪表台储物垫"

    elif (not re.search(word_pattern("side"), title_lower)) and (re.search(word_pattern("console"), title_lower) or re.search(word_pattern("armrest"), title_lower)) and (re.search(word_pattern("storage box"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower)):
        return "扶手箱储物盒"
    elif (re.search(word_pattern("side storage"), title_lower)) and (re.search(word_pattern("center console"), title_lower) or re.search(word_pattern("shifter box"), title_lower) or re.search(word_pattern("gear shift"), title_lower)) and (not re.search(word_pattern("door side"), title_lower)) and (re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("storage box"), title_lower)):
        return "中控侧挂盒"

    elif (re.search(word_pattern("side door"), title_lower) or re.search(word_pattern("door side"), title_lower) or re.search(word_pattern("door handle"), title_lower) or re.search(word_pattern("door storage pockets"), title_lower)) and (re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizer"), title_lower)):
        return "车门拓展储物盒"
    elif (re.search(word_pattern("armrest cover"), title_lower) or re.search(word_pattern("center console cover"), title_lower) or re.search(word_pattern("armrest cushion"), title_lower) or re.search(word_pattern("armrest pad"), title_lower)):
        return "扶手箱套"
    elif (re.search(word_pattern("speaker pods"), title_lower)):
        return "吊舱音响外壳"

    elif (re.search(word_pattern("rear door"), title_lower) or re.search(word_pattern("tailgate"), title_lower)) and (re.search(word_pattern("table"), title_lower)):
        return "尾门折叠工作台"
    elif (re.search(word_pattern("soft top"), title_lower)) and (re.search(word_pattern("window storage bag"), title_lower)):
        return "软顶窗户收纳包"
    elif (re.search(word_pattern("pinch weld covers"), title_lower) or re.search(word_pattern("pinch weld cover"), title_lower)):
        return "侧裙边"
    elif (re.search(word_pattern("grille lamps"), title_lower) or re.search(word_pattern("grille light"), title_lower) or re.search(word_pattern("grille lights"), title_lower)):
        return "中网小黄灯"
    elif (re.search(word_pattern("roof racks"), title_lower) or re.search(word_pattern("roof rack"), title_lower) or re.search(word_pattern("cross bars"), title_lower) or re.search(word_pattern("cross bar"), title_lower)):
        return "行李架"
    elif (re.search(word_pattern("wireless charging"), title_lower) or re.search(word_pattern("wireless charger"), title_lower) or re.search(word_pattern("wireless chargers"), title_lower)) and (re.search(word_pattern("pad"), title_lower) or re.search(word_pattern("tray"), title_lower)):
        return "中控无线充电板"
    elif (re.search(word_pattern("running boards"), title_lower) or re.search(word_pattern("side step"), title_lower) or re.search(word_pattern("side steps"), title_lower) or re.search(word_pattern("nerf bars"), title_lower) or re.search(word_pattern("nerf bar"), title_lower) or re.search(word_pattern("step bars"), title_lower) or re.search(word_pattern("rock rails"), title_lower)or re.search(word_pattern("step rails"), title_lower)):
        return "岩轨踏板"
    elif (re.search(word_pattern("wiper blade"), title_lower) or re.search(word_pattern("wiper blades"), title_lower)):
        return "雨刷片"
    elif (re.search(word_pattern("tail lights"), title_lower) or re.search(word_pattern("tail light"), title_lower) or re.search(word_pattern("rear lamps"), title_lower) or re.search(word_pattern("brake light"), title_lower) or re.search(word_pattern("brake lights"), title_lower) or re.search(word_pattern("window lights"), title_lower)):
        return "尾灯"
    elif (re.search(word_pattern("hard top"), title_lower) or re.search(word_pattern("hardtop"), title_lower) or re.search(word_pattern("roof top"), title_lower) or re.search(word_pattern("roof panel"), title_lower)) and (re.search(word_pattern("storage bag"), title_lower)):
        return "硬顶收纳包"
    elif (re.search(word_pattern("door storage bags"), title_lower) or re.search(word_pattern("door storage bag"), title_lower) or re.search(word_pattern("door bag"), title_lower) or re.search(word_pattern("door bags"), title_lower)):
        return "车门收纳包"

    elif (re.search(word_pattern("roll bar"), title_lower) or re.search(word_pattern("d-pillar"), title_lower)) and (re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("covers"), title_lower)):
        return "d柱护板"
    elif (re.search(word_pattern("crash bar"), title_lower)) and (re.search(word_pattern("end caps"), title_lower) or re.search(word_pattern("end cap"), title_lower) or re.search(word_pattern("stopper cover"), title_lower)):
        return "前桥皮塞"
    elif (re.search(word_pattern("trail sight"), title_lower) or re.search(word_pattern("trail sights"), title_lower)) and (re.search(word_pattern("lights"), title_lower) or re.search(word_pattern("light"), title_lower)):
        return "机盖把手灯"

    elif (re.search(word_pattern("tube door"), title_lower) or re.search(word_pattern("tube doors"), title_lower) or re.search(word_pattern("tubular doors"), title_lower) or re.search(word_pattern("half doors"), title_lower)):
        return "管门"
    elif (re.search(word_pattern("winch"), title_lower)) and (re.search(word_pattern("bracket"), title_lower) or re.search(word_pattern("plate"), title_lower)):
        return "绞盘架"

    elif (re.search(word_pattern("bull bar"), title_lower) or re.search(word_pattern("front bumper"), title_lower) or re.search(word_pattern("grille guard"), title_lower) or re.search(word_pattern("brush guard"), title_lower)):
        return "小牛栏"

    elif (re.search(word_pattern("bumper sill"), title_lower) or re.search(word_pattern("tailgate sill"), title_lower) or re.search(word_pattern("trunk sill"), title_lower) or re.search(word_pattern("trunk door sill"), title_lower) or re.search(word_pattern("rear bumper protector"), title_lower)):
        return "后护板"
    elif (re.search(word_pattern("fog light"), title_lower) or re.search(word_pattern("fog lights"), title_lower) or re.search(word_pattern("fog bumper lamps"), title_lower) or re.search(word_pattern("fog lamps"), title_lower)):
        return "雾灯"
    elif (re.search(word_pattern("daytime running light"), title_lower) or re.search(word_pattern("daytime running lights"), title_lower) or re.search(word_pattern("daytime running lamp"), title_lower) or re.search(word_pattern("daytime running lamps"), title_lower)):
        return "日行灯"
    elif (re.search(word_pattern("puddle lights"), title_lower) or re.search(word_pattern("puddle light"), title_lower) or re.search(word_pattern("welcome lights"), title_lower) or re.search(word_pattern("welcome light"), title_lower) or re.search(word_pattern("door projection lights"), title_lower)):
        return "水坑灯"
    
    elif (re.search(word_pattern("hitch"), title_lower)):
        return "拖车挂钩+孔塞"
    elif (re.search(word_pattern("transmission"), title_lower) or re.search(word_pattern("chassic"), title_lower) or re.search(word_pattern("gearbox"), title_lower)) and (re.search(word_pattern("skid plate"), title_lower) or re.search(word_pattern("splash shield"), title_lower) or re.search(word_pattern("guard"), title_lower)):
        return "变速箱下护板"

    elif (re.search(word_pattern("door edge guards"), title_lower) or re.search(word_pattern("door sill"), title_lower) or re.search(word_pattern("door entry"), title_lower)):
        return "外置门槛条"
    elif (re.search(word_pattern("fuse box cover"), title_lower) or re.search(word_pattern("fuse box holder"), title_lower) or re.search(word_pattern("wire harness organizer"), title_lower) or re.search(word_pattern("fuse block"), title_lower) or re.search(word_pattern("fuse panel covers"), title_lower)):
        return "保险盒防水盖"
    elif (re.search(word_pattern("foot rest"), title_lower) or re.search(word_pattern("brake pedal"), title_lower) or re.search(word_pattern("pedal covers"), title_lower) or re.search(word_pattern("gas pedal"), title_lower)):
        return "休息踏板"
    elif (re.search(word_pattern("footwell"), title_lower)) and (re.search(word_pattern("lighting"), title_lower) or re.search(word_pattern("light"), title_lower) or re.search(word_pattern("lights"), title_lower)):
        return "脚窝灯"
    elif (re.search(word_pattern("license plate"), title_lower)) and (re.search(word_pattern("frame"), title_lower) or re.search(word_pattern("frames"), title_lower) or re.search(word_pattern("bracket"), title_lower) or re.search(word_pattern("holder"), title_lower)):
        return "车牌架"
    elif (re.search(word_pattern("hubcap"), title_lower) or re.search(word_pattern("hubcaps"), title_lower) or re.search(word_pattern("hub caps"), title_lower) or re.search(word_pattern("hub center cap"), title_lower) or re.search(word_pattern("wheel skins"), title_lower) or re.search(word_pattern("wheel covers"), title_lower)) :
        return "轮毂罩"
    elif (re.search(word_pattern("decor cover"), title_lower) or re.search(word_pattern("panel trim"), title_lower)) :
        return "装饰盖板"

    elif (re.search(word_pattern("hood"), title_lower) or re.search(word_pattern("bonnet"), title_lower)) and (re.search(word_pattern("lift supports"), title_lower) or re.search(word_pattern("struts"), title_lower) or re.search(word_pattern("support kit"), title_lower) or re.search(word_pattern("support bar"), title_lower) or re.search(word_pattern("assist"), title_lower) or re.search(word_pattern("prop rods"), title_lower) or re.search(word_pattern("hydraulic"), title_lower)):
        return "机盖液压杆"
    elif (re.search(word_pattern("window"), title_lower)) and (re.search(word_pattern("lift supports"), title_lower) or re.search(word_pattern("strut"), title_lower) or re.search(word_pattern("struts"), title_lower) or re.search(word_pattern("support kit"), title_lower) or re.search(word_pattern("support bar"), title_lower) or re.search(word_pattern("assist"), title_lower) or re.search(word_pattern("prop rods"), title_lower) or re.search(word_pattern("hydraulic"), title_lower)):
        return "后窗液压杆"
    
    elif (re.search(word_pattern("trunk"), title_lower) or re.search(word_pattern("tailgate"), title_lower)) and (re.search(word_pattern("lift supports"), title_lower) or re.search(word_pattern("strut"), title_lower) or re.search(word_pattern("struts"), title_lower) or re.search(word_pattern("support kit"), title_lower) or re.search(word_pattern("support bar"), title_lower) or re.search(word_pattern("assist"), title_lower) or re.search(word_pattern("prop rods"), title_lower) or re.search(word_pattern("hydraulic"), title_lower)):
        return "尾门液压杆"


    elif (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("lamp"), title_lower) or re.search(word_pattern("light"), title_lower) or re.search(word_pattern("lights"), title_lower) or re.search(word_pattern("lamps"), title_lower)):
        return "后舱灯"
    
    elif (re.search(word_pattern("rear"), title_lower)) and (re.search(word_pattern("dual"), title_lower)) and (re.search(word_pattern("cup holder"), title_lower)):
        return "后排过桥水杯座"
    elif (re.search(word_pattern("cup holder"), title_lower)) and (not re.search(word_pattern("coaster"), title_lower)) and (not re.search(word_pattern("liner"), title_lower)) and (not re.search(word_pattern("liners"), title_lower)):
        return "水杯座"

    else:
        return ""

# 在文档2中添加一列用于标注
df2['商品名称'] = df2.apply(annotate_product, axis=1)

# 保存带有标注的文档2
df2.to_excel('product-automotive-us-bronco-2023.09-大于50（标注车型）（排除其他车型）(排除sport1111111111).xlsx', index=False)


# In[ ]:





# In[ ]:







import pandas as pd
import re  # 导入re模块

# 读取文档2
df2 = pd.read_excel('maverick全量-2023.11.27-2023.12.27（标注车型）（剔除通用）.xlsx')

# 创建一个函数来标注商品
def annotate_product(row):
    title = str(row['商品标题'])  # 将商品标题转换为字符串类型
    title_lower = title.lower()
    
    # 定义用于匹配完整单词的正则表达式模式
    word_pattern = r'\b{}\b'.format

    # 初始化一个列表来收集所有匹配的类别
    matched_categories = []


    # 使用正则表达式匹配关键词，并将所有匹配的类别添加到列表中

    if (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("sidewall"), title_lower)) and (re.search(word_pattern("protector"), title_lower) or re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        matched_categories.append("后备箱两侧垫")


    if (re.search(word_pattern("tailgate mat"), title_lower) or re.search(word_pattern("tailgate pad"), title_lower) or re.search(word_pattern("tailgate liner"), title_lower)):
        matched_categories.append("尾门垫")
    if (re.search(word_pattern("bed mat"), title_lower) or re.search(word_pattern("bed liner"), title_lower) or re.search(word_pattern("bed mats"), title_lower)):
        matched_categories.append("后斗垫")
    if (re.search(word_pattern("tailgate"), title_lower)) and (re.search(word_pattern("mold"), title_lower) or re.search(word_pattern("mould"), title_lower) or re.search(word_pattern("molding"), title_lower) or re.search(word_pattern("moulding"), title_lower)) and (re.search(word_pattern("cap"), title_lower) or re.search(word_pattern("caps"), title_lower)) and (not re.search(word_pattern("clips"), title_lower)) :
        matched_categories.append("尾门护盖")
    if (re.search(word_pattern("bed rail"), title_lower)) and (re.search(word_pattern("cap"), title_lower) or re.search(word_pattern("caps"), title_lower)) and (not re.search(word_pattern("clips"), title_lower)) :
        matched_categories.append("护栏盖")
    if (re.search(word_pattern("tonneau covers"), title_lower) or re.search(word_pattern("tonneau cover"), title_lower)):
        matched_categories.append("后斗盖")
    if (re.search(word_pattern("bed extender"), title_lower)):
        matched_categories.append("后斗延长器")
    if (re.search(word_pattern("bed rails"), title_lower) or re.search(word_pattern("bed rail"), title_lower)):
        matched_categories.append("车斗护栏")
    if (re.search(word_pattern("tailgate"), title_lower) or re.search(word_pattern("bed"), title_lower)) and (re.search(word_pattern("ramp"), title_lower) or re.search(word_pattern("slides"), title_lower) or re.search(word_pattern("slide"), title_lower)) :
        matched_categories.append("尾门坡道")


    if (re.search(word_pattern("tent"), title_lower) or re.search(word_pattern("camping"), title_lower)):
        matched_categories.append("露营装备")
    if (re.search(word_pattern("skid plates"), title_lower) or re.search(word_pattern("skid plate"), title_lower)):
        matched_categories.append("车底防滑板")
    if (re.search(word_pattern("wheel well"), title_lower) or re.search(word_pattern("wheel-well"), title_lower) or re.search(word_pattern("inner fender"), title_lower)) and (re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("liner"), title_lower)) :
        matched_categories.append("车轮罩内衬")
    if (re.search(word_pattern("rocker panels"), title_lower) or re.search(word_pattern("rocker panel"), title_lower)):
        matched_categories.append("侧岩板")

    if (re.search(word_pattern("side skirts"), title_lower) or re.search(word_pattern("side skirt"), title_lower)):
        matched_categories.append("侧裙条")

    if (re.search(word_pattern("bed"), title_lower) or re.search(word_pattern("truck"), title_lower) or re.search(word_pattern("cargo"), title_lower)) and (re.search(word_pattern("dividers"), title_lower) or re.search(word_pattern("divider"), title_lower)) :
        matched_categories.append("货箱隔板")

    if (re.search(word_pattern("stake pocket"), title_lower) or re.search(word_pattern("bed hole"), title_lower)) and (re.search(word_pattern("covers"), title_lower) or re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("plug"), title_lower) or re.search(word_pattern("plugs"), title_lower)) :
        matched_categories.append("插口盖")


    if (re.search(word_pattern("hood protector"), title_lower) or re.search(word_pattern("hood deflector"), title_lower) or re.search(word_pattern("bug deflector"), title_lower) or re.search(word_pattern("hood guard"), title_lower) or re.search(word_pattern("hood shield"), title_lower)):
        matched_categories.append("引擎盖护板")

    if (re.search(word_pattern("hood scoop"), title_lower) or re.search(word_pattern("hood scoops"), title_lower)):
        matched_categories.append("引擎盖进气冲压器")



    if (re.search(word_pattern("towing mirrors"), title_lower) or re.search(word_pattern("towing mirror"), title_lower)):
        matched_categories.append("拖车镜")
    if (re.search(word_pattern("lug nuts"), title_lower) or re.search(word_pattern("lug nut"), title_lower)):
        matched_categories.append("轮毂螺帽")
    if (re.search(word_pattern("spoilers"), title_lower) or re.search(word_pattern("spoiler"), title_lower)):
        matched_categories.append("尾翼")

    if (re.search(word_pattern("cargo cover"), title_lower) or re.search(word_pattern("security shield shade"), title_lower) or re.search(word_pattern("security shade cover shield"), title_lower)):
        matched_categories.append("遮物帘")
    if (re.search(word_pattern("trunk grocery bag hooks"), title_lower) or re.search(word_pattern("trunk hook"), title_lower) or re.search(word_pattern("trunk hooks"), title_lower)):
        matched_categories.append("后备箱挂钩")
    if (re.search(word_pattern("floor"), title_lower) or re.search(word_pattern("floorliners"), title_lower) or re.search(word_pattern("row liners"), title_lower) or re.search(word_pattern("row liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        matched_categories.append("脚垫")
    if (re.search(word_pattern("seat covers"), title_lower) or re.search(word_pattern("seat cover"), title_lower)) and (not re.search(word_pattern("back"), title_lower)) :
        matched_categories.append("座椅套")
    if (re.search(word_pattern("backrest"), title_lower) or re.search(word_pattern("seat back"), title_lower) or re.search(word_pattern("seats back"), title_lower) or re.search(word_pattern("dog seat liner"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("mat"), title_lower) or re.search(word_pattern("protector"), title_lower)):
        matched_categories.append("椅背垫")
    if (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower) or re.search(word_pattern("tub rail"), title_lower)) and (re.search(word_pattern("side covers"), title_lower) or re.search(word_pattern("side cover"), title_lower) or re.search(word_pattern("side protector"), title_lower) or re.search(word_pattern("rail cover"), title_lower) or re.search(word_pattern("edge protector"), title_lower)):
        matched_categories.append("后备箱侧沿护板")
    if (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("liner"), title_lower) or re.search(word_pattern("liners"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("mat"), title_lower)):
        matched_categories.append("后备箱垫")

    if (re.search(word_pattern("car cover"), title_lower) or re.search(word_pattern("car covers"), title_lower)):
        matched_categories.append("车衣")
    if (re.search(word_pattern("snow cover"), title_lower) or re.search(word_pattern("snow covers"), title_lower)):
        matched_categories.append("雪挡")
    if (re.search(word_pattern("rain guard"), title_lower) or re.search(word_pattern("rain guards"), title_lower) or re.search(word_pattern("side window visor deflectors"), title_lower) or re.search(word_pattern("window deflectors"), title_lower)):
        matched_categories.append("晴雨挡")
    if (re.search(word_pattern("roof"), title_lower) or re.search(word_pattern("top"), title_lower)) and (re.search(word_pattern("sunshade"), title_lower) or re.search(word_pattern("sun shade"), title_lower)):
        matched_categories.append("车顶遮阳")
    if (re.search(word_pattern("mud flaps"), title_lower) or re.search(word_pattern("mud flap"), title_lower) or re.search(word_pattern("mudguard"), title_lower) or re.search(word_pattern("mudguards"), title_lower) or re.search(word_pattern("mud guards"), title_lower) or re.search(word_pattern("splash guards"), title_lower)):
        matched_categories.append("挡泥板")

    if (re.search(word_pattern("fender flares"), title_lower) or re.search(word_pattern("fender flare"), title_lower)) and (not re.search(word_pattern("mud flap"), title_lower) or not re.search(word_pattern("mud guards"), title_lower)) :
        matched_categories.append("轮眉")
    if (re.search(word_pattern("hitch steps"), title_lower) or re.search(word_pattern("hitch step"), title_lower)) :
        matched_categories.append("拖车钩脚踏")

    if (re.search(word_pattern("windshield"), title_lower) or re.search(word_pattern("window"), title_lower) or re.search(word_pattern("windows"), title_lower)) and (re.search(word_pattern("sunshade"), title_lower) or re.search(word_pattern("shades"), title_lower) or re.search(word_pattern("sun shade"), title_lower) or re.search(word_pattern("sun visor"), title_lower) or re.search(word_pattern("sunshades"), title_lower)):
        matched_categories.append("遮阳挡")
    if (re.search(word_pattern("front"), title_lower) or re.search(word_pattern("rear"), title_lower) or re.search(word_pattern("interior"), title_lower)) and (re.search(word_pattern("ceiling lights"), title_lower) or re.search(word_pattern("ceiling light"), title_lower) or re.search(word_pattern("reading lights"), title_lower) or re.search(word_pattern("dome lights"), title_lower) or re.search(word_pattern("dome light"), title_lower) or re.search(word_pattern("roof map light"), title_lower)):
        matched_categories.append("阅读灯/内顶灯")
    if (re.search(word_pattern("glove box"), title_lower)) and (re.search(word_pattern("dividers"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("partition"), title_lower)):
        matched_categories.append("手套箱隔板")
    if (re.search(word_pattern("dash"), title_lower) or re.search(word_pattern("dashboard"), title_lower) or re.search(word_pattern("screen"), title_lower)) and (re.search(word_pattern("holder"), title_lower) or re.search(word_pattern("mount"), title_lower) or re.search(word_pattern("bracket"), title_lower)):
        matched_categories.append("仪表台支架")

    if (re.search(word_pattern("phone"), title_lower) or re.search(word_pattern("cellphone"), title_lower)) and (re.search(word_pattern("holder"), title_lower) or re.search(word_pattern("mount"), title_lower) or re.search(word_pattern("bracket"), title_lower)):
        matched_categories.append("手机支架")

    if (re.search(word_pattern("dash"), title_lower) or re.search(word_pattern("dashboard"), title_lower) or re.search(word_pattern("screen"), title_lower)) and (re.search(word_pattern("pad"), title_lower) or re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("mat"), title_lower) or re.search(word_pattern("mats"), title_lower) or re.search(word_pattern("storage"), title_lower) or re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("storage box"), title_lower)):
        matched_categories.append("仪表台储物垫")

    if (re.search(word_pattern("center console"), title_lower) or re.search(word_pattern("shifter box"), title_lower) or re.search(word_pattern("armrest"), title_lower) or re.search(word_pattern("gear shift"), title_lower)) and (re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizers"), title_lower)  or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("storage box"), title_lower)):
        matched_categories.append("中控储物盒")

    if (re.search(word_pattern("underseat"), title_lower) or re.search(word_pattern("under seat"), title_lower)) and (re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("organizers"), title_lower) or re.search(word_pattern("storage box"), title_lower)):
        matched_categories.append("座椅下储物盒")


    if (re.search(word_pattern("Tailgate"), title_lower) or re.search(word_pattern("Cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("organizers"), title_lower) or re.search(word_pattern("storage box"), title_lower)):
        matched_categories.append("货厢储物盒")

    if (re.search(word_pattern("wheel well"), title_lower)) and (re.search(word_pattern("tray"), title_lower) or re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizer"), title_lower) or re.search(word_pattern("organizers"), title_lower) or re.search(word_pattern("storage"), title_lower)):
        matched_categories.append("车轮凹槽储物箱")

    if (re.search(word_pattern("side door"), title_lower) or re.search(word_pattern("door side"), title_lower) or re.search(word_pattern("door handle"), title_lower) or re.search(word_pattern("door storage pockets"), title_lower)) and (re.search(word_pattern("pocket"), title_lower) or re.search(word_pattern("pockets"), title_lower) or re.search(word_pattern("organizer"), title_lower)):
        matched_categories.append("车门拓展储物盒")
    if (re.search(word_pattern("armrest cover"), title_lower) or re.search(word_pattern("center console cover"), title_lower) or re.search(word_pattern("armrest cushion"), title_lower) or re.search(word_pattern("armrest pad"), title_lower)):
        matched_categories.append("扶手箱套")
    if (re.search(word_pattern("speaker pods"), title_lower)):
        matched_categories.append("吊舱音响外壳")

    if (re.search(word_pattern("rear door"), title_lower) or re.search(word_pattern("tailgate"), title_lower)) and (re.search(word_pattern("table"), title_lower)):
        matched_categories.append("尾门折叠工作台")
    if (re.search(word_pattern("soft top"), title_lower)) and (re.search(word_pattern("window storage bag"), title_lower)):
        matched_categories.append("软顶窗户收纳包")


    if (re.search(word_pattern("snugtop cap"), title_lower) or re.search(word_pattern("snugtop caps"), title_lower) or re.search(word_pattern("canopies"), title_lower) or re.search(word_pattern("canopy"), title_lower) or re.search(word_pattern("toppers"), title_lower) or re.search(word_pattern("topper"), title_lower)):
        matched_categories.append("顶篷")

    if (re.search(word_pattern("tie-down"), title_lower) or re.search(word_pattern("tie down"), title_lower)) and (re.search(word_pattern("anchor"), title_lower) or re.search(word_pattern("anchors"), title_lower)):
        matched_categories.append("车斗锚栓")


    if (re.search(word_pattern("pinch weld covers"), title_lower) or re.search(word_pattern("pinch weld cover"), title_lower)):
        matched_categories.append("侧裙边")
    if (re.search(word_pattern("grille lamps"), title_lower) or re.search(word_pattern("grille light"), title_lower) or re.search(word_pattern("grille lights"), title_lower)):
        matched_categories.append("中网小黄灯")
    if (re.search(word_pattern("roof racks"), title_lower) or re.search(word_pattern("roof rack"), title_lower) or re.search(word_pattern("cross bars"), title_lower) or re.search(word_pattern("cross bar"), title_lower) or re.search(word_pattern("bed rack"), title_lower) or re.search(word_pattern("bed racks"), title_lower)):
        matched_categories.append("行李架")
    if (re.search(word_pattern("wireless charging"), title_lower) or re.search(word_pattern("wireless charger"), title_lower) or re.search(word_pattern("wireless chargers"), title_lower)) and (re.search(word_pattern("pad"), title_lower) or re.search(word_pattern("tray"), title_lower)):
        matched_categories.append("中控无线充电板")
    if (re.search(word_pattern("running boards"), title_lower) or re.search(word_pattern("side step"), title_lower) or re.search(word_pattern("side steps"), title_lower) or re.search(word_pattern("nerf bars"), title_lower) or re.search(word_pattern("nerf bar"), title_lower) or re.search(word_pattern("step bars"), title_lower) or re.search(word_pattern("rock rails"), title_lower)or re.search(word_pattern("step rails"), title_lower)):
        matched_categories.append("岩轨踏板")
    if (re.search(word_pattern("wiper blade"), title_lower) or re.search(word_pattern("wiper blades"), title_lower)):
        matched_categories.append("雨刷片")
    if (re.search(word_pattern("tail lights"), title_lower) or re.search(word_pattern("tail light"), title_lower) or re.search(word_pattern("rear lamps"), title_lower) or re.search(word_pattern("brake light"), title_lower) or re.search(word_pattern("brake lights"), title_lower) or re.search(word_pattern("window lights"), title_lower)):
        matched_categories.append("尾灯")
    if (re.search(word_pattern("hard top"), title_lower) or re.search(word_pattern("hardtop"), title_lower) or re.search(word_pattern("roof top"), title_lower) or re.search(word_pattern("roof panel"), title_lower)) and (re.search(word_pattern("storage bag"), title_lower)):
        matched_categories.append("硬顶收纳包")
    if (re.search(word_pattern("door storage bags"), title_lower) or re.search(word_pattern("door storage bag"), title_lower) or re.search(word_pattern("door bag"), title_lower) or re.search(word_pattern("door bags"), title_lower)):
        matched_categories.append("车门收纳包")

    if (re.search(word_pattern("roll bar"), title_lower) or re.search(word_pattern("d-pillar"), title_lower)) and (re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("covers"), title_lower)):
        matched_categories.append("d柱护板")
    if (re.search(word_pattern("crash bar"), title_lower)) and (re.search(word_pattern("end caps"), title_lower) or re.search(word_pattern("end cap"), title_lower) or re.search(word_pattern("stopper cover"), title_lower)):
        matched_categories.append("前桥皮塞")
    if (re.search(word_pattern("trail sight"), title_lower) or re.search(word_pattern("trail sights"), title_lower)) and (re.search(word_pattern("lights"), title_lower) or re.search(word_pattern("light"), title_lower)):
        matched_categories.append("机盖把手灯")

    if (re.search(word_pattern("tube door"), title_lower) or re.search(word_pattern("tube doors"), title_lower) or re.search(word_pattern("tubular doors"), title_lower) or re.search(word_pattern("half doors"), title_lower)):
        matched_categories.append("管门")
    if (re.search(word_pattern("winch"), title_lower)) and (re.search(word_pattern("bracket"), title_lower) or re.search(word_pattern("plate"), title_lower)):
        matched_categories.append("绞盘架")

    if (re.search(word_pattern("bull bar"), title_lower) or re.search(word_pattern("front bumper"), title_lower) or re.search(word_pattern("grille guard"), title_lower) or re.search(word_pattern("brush guard"), title_lower) or re.search(word_pattern("bumper guard"), title_lower)):
        matched_categories.append("小牛栏")

    if (re.search(word_pattern("bumper sill"), title_lower) or re.search(word_pattern("tailgate sill"), title_lower) or re.search(word_pattern("trunk sill"), title_lower) or re.search(word_pattern("trunk door sill"), title_lower) or re.search(word_pattern("bumper protector"), title_lower)):
        matched_categories.append("后护板")
    if (re.search(word_pattern("fog light"), title_lower) or re.search(word_pattern("fog lights"), title_lower) or re.search(word_pattern("fog bumper lamps"), title_lower) or re.search(word_pattern("fog lamps"), title_lower)):
        matched_categories.append("雾灯")
    if (re.search(word_pattern("daytime running light"), title_lower) or re.search(word_pattern("daytime running lights"), title_lower) or re.search(word_pattern("daytime running lamp"), title_lower) or re.search(word_pattern("daytime running lamps"), title_lower)):
        matched_categories.append("日行灯")
    if (re.search(word_pattern("puddle lights"), title_lower) or re.search(word_pattern("puddle light"), title_lower) or re.search(word_pattern("welcome lights"), title_lower) or re.search(word_pattern("welcome light"), title_lower) or re.search(word_pattern("door projection lights"), title_lower)):
        matched_categories.append("水坑灯")
    if (re.search(word_pattern("light bars"), title_lower) or re.search(word_pattern("light bar"), title_lower)):
        matched_categories.append("灯条")
    if (re.search(word_pattern("tail light"), title_lower) or re.search(word_pattern("taillight"), title_lower) or re.search(word_pattern("headlight"), title_lower) or re.search(word_pattern("head light"), title_lower)) and (re.search(word_pattern("covers"), title_lower) or re.search(word_pattern("cover"), title_lower) or re.search(word_pattern("guard"), title_lower) or re.search(word_pattern("guards"), title_lower)) :
        matched_categories.append("灯条")


    if (re.search(word_pattern("hitch"), title_lower) or re.search(word_pattern("tow hook"), title_lower) or re.search(word_pattern("tow hooks"), title_lower)):
        matched_categories.append("拖车挂钩+孔塞")

    if (re.search(word_pattern("air"), title_lower)) and (re.search(word_pattern("filters"), title_lower) or re.search(word_pattern("filter"), title_lower)):
        matched_categories.append("空气滤清器")

    if (re.search(word_pattern("air"), title_lower)) and (re.search(word_pattern("deflectors"), title_lower) or re.search(word_pattern("deflector"), title_lower)):
        matched_categories.append("气流偏导器")



    if (re.search(word_pattern("transmission"), title_lower) or re.search(word_pattern("chassic"), title_lower) or re.search(word_pattern("gearbox"), title_lower)) and (re.search(word_pattern("skid plate"), title_lower) or re.search(word_pattern("splash shield"), title_lower) or re.search(word_pattern("guard"), title_lower)):
        matched_categories.append("变速箱下护板")

    if (re.search(word_pattern("door edge guards"), title_lower) or re.search(word_pattern("door sill"), title_lower) or re.search(word_pattern("door entry"), title_lower)):
        matched_categories.append("外置门槛条")
    if (re.search(word_pattern("fuse box cover"), title_lower) or re.search(word_pattern("fuse box holder"), title_lower) or re.search(word_pattern("wire harness organizer"), title_lower) or re.search(word_pattern("fuse block"), title_lower) or re.search(word_pattern("fuse panel covers"), title_lower)):
        matched_categories.append("保险盒防水盖")
    if (re.search(word_pattern("foot rest"), title_lower) or re.search(word_pattern("brake pedal"), title_lower) or re.search(word_pattern("pedal covers"), title_lower) or re.search(word_pattern("gas pedal"), title_lower)):
        matched_categories.append("休息踏板")
    if (re.search(word_pattern("footwell"), title_lower)) and (re.search(word_pattern("lighting"), title_lower) or re.search(word_pattern("light"), title_lower) or re.search(word_pattern("lights"), title_lower)):
        matched_categories.append("脚窝灯")
    if (re.search(word_pattern("license plate"), title_lower)) and (re.search(word_pattern("frame"), title_lower) or re.search(word_pattern("frames"), title_lower) or re.search(word_pattern("bracket"), title_lower) or re.search(word_pattern("holder"), title_lower)):
        matched_categories.append("车牌架")
    if (re.search(word_pattern("hubcap"), title_lower) or re.search(word_pattern("hubcaps"), title_lower) or re.search(word_pattern("hub caps"), title_lower) or re.search(word_pattern("hub center cap"), title_lower) or re.search(word_pattern("wheel skins"), title_lower) or re.search(word_pattern("wheel covers"), title_lower)) :
        matched_categories.append("轮毂罩")

    if (re.search(word_pattern("center caps"), title_lower) or re.search(word_pattern("center cap"), title_lower)) :
        matched_categories.append("轮毂中心盖")

    if (re.search(word_pattern("decor cover"), title_lower) or re.search(word_pattern("panel trim"), title_lower)) :
        matched_categories.append("装饰盖板")

    if (re.search(word_pattern("hood"), title_lower) or re.search(word_pattern("bonnet"), title_lower)) and (re.search(word_pattern("lift supports"), title_lower) or re.search(word_pattern("struts"), title_lower) or re.search(word_pattern("support kit"), title_lower) or re.search(word_pattern("support bar"), title_lower) or re.search(word_pattern("assist"), title_lower) or re.search(word_pattern("prop rods"), title_lower) or re.search(word_pattern("hydraulic"), title_lower)):
        matched_categories.append("机盖液压杆")
    if (re.search(word_pattern("window"), title_lower)) and (re.search(word_pattern("lift supports"), title_lower) or re.search(word_pattern("strut"), title_lower) or re.search(word_pattern("struts"), title_lower) or re.search(word_pattern("support kit"), title_lower) or re.search(word_pattern("support bar"), title_lower) or re.search(word_pattern("assist"), title_lower) or re.search(word_pattern("prop rods"), title_lower) or re.search(word_pattern("hydraulic"), title_lower)):
        matched_categories.append("后窗液压杆")
    
    if (re.search(word_pattern("trunk"), title_lower) or re.search(word_pattern("tailgate"), title_lower)) and (re.search(word_pattern("lift supports"), title_lower) or re.search(word_pattern("strut"), title_lower) or re.search(word_pattern("struts"), title_lower) or re.search(word_pattern("support kit"), title_lower) or re.search(word_pattern("support bar"), title_lower) or re.search(word_pattern("assist"), title_lower) or re.search(word_pattern("prop rods"), title_lower) or re.search(word_pattern("hydraulic"), title_lower)):
        matched_categories.append("尾门液压杆")


    if (re.search(word_pattern("cargo"), title_lower) or re.search(word_pattern("trunk"), title_lower)) and (re.search(word_pattern("lamp"), title_lower) or re.search(word_pattern("light"), title_lower) or re.search(word_pattern("lights"), title_lower) or re.search(word_pattern("lamps"), title_lower)):
        matched_categories.append("后舱灯")
    
    if (re.search(word_pattern("rear"), title_lower)) and (re.search(word_pattern("dual"), title_lower)) and (re.search(word_pattern("cup holder"), title_lower)):
        matched_categories.append("后排过桥水杯座")
    if (re.search(word_pattern("cup holder"), title_lower)) and (not re.search(word_pattern("coaster"), title_lower)) and (not re.search(word_pattern("liner"), title_lower)) and (not re.search(word_pattern("liners"), title_lower)):
        matched_categories.append("水杯座")


    # 将所有匹配的类别用“+”符号连接
    return '+'.join(matched_categories) if matched_categories else ""


# 在文档2中添加一列用于标注
df2['商品名称'] = df2.apply(annotate_product, axis=1)

# 保存带有标注的文档2
df2.to_excel('maverick全量-2023.11.27-2023.12.27（标注车型）（剔除通用）（标注产品名称）.xlsx', index=False)

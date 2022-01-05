import numpy as np
import pandas as pd
import re
import jieba
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("招聘数据.csv")

thenewdf = df.drop_duplicates(["标题","公司名字","薪资","招聘信息"],keep='first')

thenewdf.to_csv("招聘数据去重.csv",encoding="utf-8",index=None)

df = pd.read_csv("招聘数据去重.csv")

# 为数据框指定行索引
df.index = range(len(df))
# 为数据框指定列索引
df.columns = ["岗位名","公司名字","城市","薪资","招聘信息","公司属性","公司规模","企业性质","招聘发布日期","公司详情页","招聘详情页"]

# =============================================================================================================#
# 一、岗位名字段处理
# 1、岗位名的探索
df["岗位名"].value_counts()
df["岗位名"] = df["岗位名"].apply(lambda x:x.lower())

# 2、数据太多太杂，筛选出目标岗位
target_job = ['java','Java','JAVA','Python','python','c','C','PHP','php','net','NET','ERP','go','iOS',
              'SAP','GIS','IT','ETL','Softerware','kubernete'"嵌入式","软件","架构","助理","算法","经理",
              "校招","校园","安卓","网络","大数据"]
# count()函数的用法，如果某个岗位名求和大于0，就证明包含了这些关键字字眼。否则就是不包含。
index = [df["岗位名"].str.count(i) for i in target_job]
index = np.array(index).sum(axis=0) > 0
job_info = df[index]

# 3、将岗位名称标准化
job_list = ['java','Java','JAVA','Python','python','c','C','PHP','php','net','NET','ERP','go','iOS',
            'SAP','GIS','IT','ETL','Softerware','kubernete',"嵌入式","软件","架构","助理","算法","经理",
            "校招","校园","安卓","网络","大数据"]
job_list = np.array(job_list)
def rename(x=None,name_list=job_list):
    index = [i in x for i in name_list]
    if sum(index) > 0:
        return name_list[index][0]
    else:
        return x
job_info["岗位名"] = job_info["岗位名"].apply(rename)
job_info["岗位名"].value_counts()
# Java语言和校招不规范,进行归一处理
job_info["岗位名"] = job_info["岗位名"].apply(lambda x:re.sub("java","Java",x))
job_info["岗位名"] = job_info["岗位名"].apply(lambda x:re.sub("Java","Java",x))
job_info["岗位名"] = job_info["岗位名"].apply(lambda x:re.sub("JAVA","Java",x))
job_info["岗位名"] = job_info["岗位名"].apply(lambda x:re.sub("校招","校招",x))
job_info["岗位名"] = job_info["岗位名"].apply(lambda x:re.sub("校园","校招",x))

#=============================================================================================================#
# 二、工资字段处理
# 说明：工资数据给出的一般是一个范围，数据也很不标准，例如：“千/月、万/月、万/年”等，下面我们做一个统一后，取数据范围的平均值。
# 像结尾是"天"的一般属于兼职，我们也不考虑。直接删除这样的数据。
job_info["薪资"].str[-1].value_counts()
job_info["薪资"].str[-3].value_counts()

index1 = job_info["薪资"].str[-1].isin(["年","月"])
index2 = job_info["薪资"].str[-3].isin(["万","千"])
job_info = job_info[index1 & index2]

def get_money_max_min(x):
    try:
        if x[-3] == "万":
            z = [float(i)*10000 for i in re.findall("[0-9]+\.?[0-9]*",x)]
        elif x[-3] == "千":
            z = [float(i) * 1000 for i in re.findall("[0-9]+\.?[0-9]*", x)]
        if x[-1] == "年":
            z = [i/12 for i in z]
        return z
    except:
        return x

salary = job_info["薪资"].apply(get_money_max_min)
job_info["最低工资"] = salary.str[0]
job_info["最高工资"] = salary.str[1]
job_info["薪资"] = job_info[["最低工资","最高工资"]].mean(axis=1)

#=============================================================================================================#
# 三、工作地点字段处理
# 正省级城市——4个:北京、上海、天津、重庆
# 副省级城市——15个:广州、武汉、哈尔滨、沈阳、成都、南京、西安、长春、济南、杭州、大连、青岛、深圳、厦门、宁波
# 计划单列市——5个:深圳、大连、青岛、宁波、厦门
# 省会地级市——16个:郑州、石家庄、合肥、长沙、南昌、南宁、昆明、西宁、福州、乌鲁木齐、拉萨、呼和浩特、海口、银川、兰州、贵阳
# 特别行政区——2个:香港、澳门
# 一线城市——4个:北京、上海、广州、深圳
# 新一线城市——15个:成都、杭州、重庆、武汉、西安、苏州、天津、南京、长沙、郑州、东莞、青岛、沈阳、宁波、昆明
feature = ["岗位名","公司名字","城市","薪资","招聘信息","公司属性","公司规模","企业性质","招聘发布日期","公司详情页","招聘详情页"]
final_df = job_info[feature]
final_df.to_csv("test.csv",encoding="utf-8",index=None)

df = pd.read_csv("test.csv")

# 为数据框指定行索引
df.index = range(len(df))
# 为数据框指定列索引
df.columns = ["岗位名","公司名字","城市","薪资","招聘信息","公司属性","公司规模","企业性质","招聘发布日期","公司详情页","招聘详情页"]

target_address = ['北京', '上海', '广州', '深圳', '杭州', '苏州', '长沙',
                '武汉', '天津', '成都', '西安', '东莞', '合肥', '佛山',
                '宁波', '南京', '重庆', '长春', '郑州', '常州', '福州',
                '沈阳', '济南', '宁波', '厦门', '贵州', '珠海', '青岛',
                '中山', '大连', '昆山', '惠州', '昆明', '南昌', '无锡',
                '南宁', '西宁', '海口', '银川', '拉萨', '兰州', '贵阳',
                '香港', '澳门', "哈尔滨","石家庄","乌鲁木齐","呼和浩特"]

index2 = [df["城市"].str.count(i) for i in target_address]
index2 = np.array(index2).sum(axis=0) > 0
job_info = df[index2]

address_list = ['北京', '上海', '广州', '深圳', '杭州', '苏州', '长沙',
                '武汉', '天津', '成都', '西安', '东莞', '合肥', '佛山',
                '宁波', '南京', '重庆', '长春', '郑州', '常州', '福州',
                '沈阳', '济南', '宁波', '厦门', '贵州', '珠海', '青岛',
                '中山', '大连', '昆山', '惠州', '昆明', '南昌', '无锡',
                '南宁', '西宁', '海口', '银川', '拉萨', '兰州', '贵阳',
                '香港', '澳门', "哈尔滨","石家庄","乌鲁木齐","呼和浩特"]
address_list = np.array(address_list)
def rename(x=None,name_list=address_list):
    index2 = [i in x for i in name_list]
    if sum(index2) > 0:
        return name_list[index2][0]
    else:
        return x
job_info["城市"] = job_info["城市"].apply(rename)
job_info["城市"].value_counts()

# =============================================================================================================#
# 四、公司属性处理
# 每个公司的行业字段可能会有多个行业标签，但是默认以第一个作为该公司的行业标签。
job_info["公司属性"] = job_info["公司属性"].str.split("/").str[0]

# =============================================================================================================#
# 五、学历字段的处理
# 根据对数据的观察，可以对数据做如下的处理。
job_info["学历"] = job_info["招聘信息"].apply(lambda x:re.findall("本科|大专|应届生|在校生|硕士|博士",x))
def func(x):
    if len(x) == 0:
        return np.nan
    elif len(x) == 1 or len(x) == 2:
        return x[0]
    else:
        return x[2]
job_info["学历"] = job_info["学历"].apply(func)

# =============================================================================================================#
# 六、经验字段的处理
# 根据对数据的观察，可以对数据做如下的处理。
job_info["工作经验"] = job_info["招聘信息"].str.split("|").str[1]
def jingyan(x):
    the = list(x)
    a = the[0]
    the = re.findall(r"\d+\.?\d*",a)
    if the:
        jy=float(the[0])
    else:
        jy=0
    return jy
job_info["工作经验"] = job_info["工作经验"].apply(jingyan)

# =============================================================================================================#
# 七、公司规模字段处理
def guimo(x):
    the = str(x)
    the = re.findall(r"\d+\.?\d*",the)
    if the:
        gm=float(the[0])
    else:
        gm=""
    return gm
job_info["公司规模"] = job_info["公司规模"].apply(guimo)


# =============================================================================================================#
# 八、构造新数据：清洗干净后的数据
feature = ["岗位名","公司名字","城市","薪资","招聘信息","学历","工作经验","公司属性","公司规模","企业性质","招聘发布日期","公司详情页","招聘详情页"]
final_df = job_info[feature]
final_df.to_csv("test.csv",encoding="gbk",index=None)
import csv
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("test.csv",encoding="gbk",engine="python")

# ==============================================================================#
# 1、公司数和招聘数
title = pd.unique(df["公司名字"])
titlelist = list(title)
count1 = 0
i=0
for theTitle in title:
    count1 += 1
f = open("公司数和招聘数.csv", mode="w", encoding="gbk", newline="")
csv_writer = csv.writer(f)
a1 = {count1}
a2 = {len(df.index)}
csv_writer.writerow(a1)
csv_writer.writerow(a2)

# ==============================================================================#
# 2、不同工作地点的岗位数量
df.sample(48)
df1 = df.groupby("城市").agg({"岗位名":"count"}).reset_index()
df1.sort_values(by="城市",axis=0,inplace=True,ascending=False)
df1[:48].to_csv("不同工作地点的岗位数量.csv",encoding="gbk",index=None)

# ==============================================================================#
# 3、不同岗位的数量
df.sample(23)
df2 = df.groupby("岗位名").agg({"公司名字":"count"}).reset_index()
df2.sort_values(by="岗位名",axis=0,inplace=True,ascending=False)
df2[:23].to_csv("不同工作的岗位数量.csv",encoding="gbk",index=None)

# ==============================================================================#
# 4、不同企业的数量
df.sample(11)
df3 = df.groupby("企业性质").agg({"岗位名":"count"}).reset_index()
df3.sort_values(by="企业性质",axis=0,inplace=True,ascending=False)
df3[:11].to_csv("不同企业的岗位数量.csv",encoding="gbk",index=None)

# ==============================================================================#
# 5、学历与工资
df.sample(5)
cols = [col for col in df.columns if col in['薪资','学历']]
# 分组的列
gp_col = '学历'
# 查询nan的列
df_na = df[cols].isna()
# 根据分组计算平均值
df4 = df.groupby(gp_col)[cols].mean().reset_index()
df4[:5].to_csv("学历与工资.csv",encoding="gbk",index=None)

# ==============================================================================#
# 6、企业与工资
df.sample(11)
cols1 = [col for col in df.columns if col in['薪资','企业性质']]
# 分组的列
gp_col1 = '企业性质'
# 查询nan的列
df_na1 = df[cols1].isna()
# 根据分组计算平均值
df5 = df.groupby(gp_col1)[cols1].mean().reset_index()
df5[:11].to_csv("企业与工资.csv",encoding="gbk",index=None)

# ==============================================================================#
# 6、工作经验与工资
df.sample(20)
cols2 = [col for col in df.columns if col in['薪资','工作经验']]
# 分组的列
gp_col2 = '工作经验'
# 查询nan的列
df_na2 = df[cols2].isna()
# 根据分组计算平均值
df6 = df.groupby(gp_col2)[cols2].mean()
df6[:20].to_csv("工作经验与工资.csv",encoding="gbk",index=None)

# ==============================================================================#
# 7、学历分布
df.sample(5)
df7 = df.groupby("学历").agg({"岗位名":"count"}).reset_index()
df7.sort_values(by="学历",axis=0,inplace=True,ascending=False)
df7[:5].to_csv("学历分布.csv",encoding="gbk",index=None)

# ==============================================================================#
# 8、工作经验分布
df.sample(6)
df8 = df.groupby("工作经验").agg({"岗位名":"count"}).reset_index()
df8.sort_values(by="工作经验",axis=0,inplace=True,ascending=False)
df8[:6].to_csv("工作经验分布.csv",encoding="gbk",index=None)

# ==============================================================================#
# 9、公司属性分布
df.sample(11)
df9 = df.groupby("公司属性").agg({"岗位名":"count"}).reset_index()
df9.sort_values(by="公司属性",axis=0,inplace=True,ascending=False)
df9[:11].to_csv("公司属性分布.csv",encoding="gbk",index=None)

# ==============================================================================#
# 10、不同地区的薪资
df.sample(48)
cols3 = [col for col in df.columns if col in['薪资','城市']]
# 分组的列
gp_col3 = '城市'
# 查询nan的列
df_na3 = df[cols3].isna()
# 根据分组计算平均值
df6 = df.groupby(gp_col3)[cols3].mean().reset_index()
df6[:48].to_csv("不同地区工资.csv",encoding="gbk",index=None)




























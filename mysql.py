import pymysql
import pandas as pd
def run_sql(path):
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='Sr12250421',
        db='data',
        charset='utf8'
    )

    cursor = connection.cursor()
    file=open(path,encoding='gbk')  #文件路径有中文，所以，先使用open打开一下
    df=pd.read_csv(file,encoding='gbk')
    print(df.head())

    for i in range(df.shape[0]):
        data=df.iloc[i]
        data=(data["岗位名"],data["公司名字"],data["城市"],data["薪资"],data["招聘信息"],data["学历"],data["工作经验"],
              data["公司属性"],data["公司规模"],data["企业性质"],data["招聘发布日期"],data["公司详情页"],data["招聘详情页"])
        sql = "insert into thedata(job,company,area,money,info,study,work,comp,big,compa,date,more1,more2) values " + str(data) + ";"
        print(sql)
        try:
            cursor.execute(sql)  #执行sql语句
            connection.commit() #连接提交
        except:
            connection.rollback()

    cursor.close()
    connection.close()
    return

if __name__ == '__main__':
    path=r'test.csv'
    run_sql(path)
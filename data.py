import pandas as pd

class SourceDataDemo:

    def __init__(self):
        self.title = '计算机行业招聘大数据'
        df = pd.read_csv("公司数和招聘数.csv", delim_whitespace=True, names=["数据"])
        temp = list(df["数据"])
        self.counter = {'name': '招聘信息数', 'value': int(temp[1])}
        self.counter2 = {'name': '招聘企业数', 'value': int(temp[0])}
        df = pd.read_csv("不同工作的岗位数量.csv", encoding='gbk')
        temp1 = list(df["岗位名"])
        temp2 = list(df["公司名字"])
        self.echart1_data = {
            'title': '各岗位招聘数',
            'data': [
                {"name": temp1[0], "value": temp2[0]},
                {"name": temp1[1], "value": temp2[1]},
                {"name": temp1[2], "value": temp2[2]},
                {"name": temp1[3], "value": temp2[3]},
                {"name": temp1[4], "value": temp2[4]},
                {"name": temp1[5], "value": temp2[5]},
                {"name": temp1[6], "value": temp2[6]},
                {"name": temp1[7], "value": temp2[7]},
                {"name": temp1[8], "value": temp2[8]},
                {"name": temp1[9], "value": temp2[9]},
                {"name": temp1[10], "value": temp2[10]},
                {"name": temp1[11], "value": temp2[11]},
                {"name": temp1[12], "value": temp2[12]},
                {"name": temp1[13], "value": temp2[13]},
                {"name": temp1[14], "value": temp2[14]},
                {"name": temp1[15], "value": temp2[15]}
            ]
        }
        df = pd.read_csv("不同企业的岗位数量.csv", encoding='gbk')
        temp1 = list(df["企业性质"])
        temp2 = list(df["岗位名"])
        self.echart2_data = {
            'title': '各企业招聘数',
            'data': [
                {"name": temp1[0], "value": temp2[0]},
                {"name": temp1[1], "value": temp2[1]},
                {"name": temp1[2], "value": temp2[2]},
                {"name": temp1[3], "value": temp2[3]},
                {"name": temp1[4], "value": temp2[4]},
                {"name": temp1[5], "value": temp2[5]},
                {"name": temp1[6], "value": temp2[6]},
                {"name": temp1[7], "value": temp2[7]},
                {"name": temp1[8], "value": temp2[8]},
                {"name": temp1[9], "value": temp2[9]},
                {"name": temp1[10], "value": temp2[10]}
            ]
        }
        df = pd.read_csv("学历分布.csv", encoding='gbk')
        temp1 = list(df["学历"])
        temp2 = list(df["岗位名"])
        self.echarts3_1_data = {
            'title': '学历需求',
            'data': [
                {"name": temp1[0], "value": temp2[0]},
                {"name": temp1[1], "value": temp2[1]},
                {"name": temp1[2], "value": temp2[2]},
                {"name": temp1[3], "value": temp2[3]},
                {"name": temp1[4], "value": temp2[4]}
            ]
        }
        df = pd.read_csv("工作经验分布.csv", encoding='gbk')
        temp1 = list(df["工作经验"])
        temp2 = list(df["岗位名"])
        self.echarts3_2_data = {
            'title': '工作经验需求（单位：年）',
            'data': [
                {"name": temp1[0], "value": temp2[0]},
                {"name": temp1[1], "value": temp2[1]},
                {"name": temp1[2], "value": temp2[2]},
                {"name": temp1[3], "value": temp2[3]},
                {"name": temp1[4], "value": temp2[4]},
                {"name": temp1[5], "value": temp2[5]}
            ]
        }
        df = pd.read_csv("公司属性分布.csv", encoding='gbk')
        temp1 = list(df["公司属性"])
        temp2 = list(df["岗位名"])
        self.echarts3_3_data = {
            'title': '公司属性分布',
            'data': [
                {"name": temp1[0], "value": temp2[0]},
                {"name": temp1[1], "value": temp2[1]},
                {"name": temp1[2], "value": temp2[2]},
                {"name": temp1[3], "value": temp2[3]},
                {"name": temp1[4], "value": temp2[4]},
                {"name": temp1[5], "value": temp2[5]},
                {"name": temp1[6], "value": temp2[6]},
                {"name": temp1[7], "value": temp2[7]},
                {"name": temp1[8], "value": temp2[8]},
                {"name": temp1[9], "value": temp2[9]},
                {"name": temp1[10], "value": temp2[10]}
            ]
        }
        df = pd.read_csv("学历与工资.csv", encoding='gbk')
        df1 = pd.read_csv("学历分布.csv", encoding='gbk')
        temp1 = list(df["薪资"])
        temp2 = list(df1["岗位名"])
        self.echart4_data = {
            'title': '学历与薪资和需求',
            'data': [
                {"name": "平均薪资",
                 "value": [temp1[1], temp1[2], temp1[3], temp1[4], temp1[0]]},
                {"name": "需求",
                 "value": [temp2[3], temp2[2], temp2[1], temp2[0], temp2[4]]},
            ],
            'xAxis': ['在校生', '大专', '本科', '硕士', '博士'],
        }
        df = pd.read_csv("企业与工资.csv", encoding='gbk')
        temp1 = list(df["企业性质"])
        temp2 = list(df["薪资"])
        self.echart5_data = {
            'title': '不同企业平均薪资',
            'data': [
                {"name": temp1[0], "value": temp2[0]},
                {"name": temp1[1], "value": temp2[1]},
                {"name": temp1[2], "value": temp2[2]},
                {"name": temp1[3], "value": temp2[3]},
                {"name": temp1[4], "value": temp2[4]},
                {"name": temp1[5], "value": temp2[5]},
                {"name": temp1[6], "value": temp2[6]},
                {"name": temp1[7], "value": temp2[7]},
                {"name": temp1[8], "value": temp2[8]},
                {"name": temp1[9], "value": temp2[9]},
                {"name": temp1[10], "value": temp2[10]}
            ]
        }
        df = pd.read_csv("工作经验与工资.csv", encoding='gbk')
        temp1 = list(df["工作经验"])
        temp2 = list(df["薪资"])
        self.echart6_data = {
            'title': '工作经验与薪资',
            'data': [
                {"name": str(int(temp1[0]))+"至"+str(int(temp1[1]))+"年", "value": temp2[0], "value2": 30000 - temp2[0], "color": "01", "radius": ['20%', '30%']},
                {"name": str(int(temp1[1]))+"至"+str(int(temp1[2]))+"年", "value": temp2[1], "value2": 30000 - temp2[1], "color": "02", "radius": ['29%', '40%']},
                {"name": str(int(temp1[2]))+"至"+str(int(temp1[3]))+"年", "value": temp2[2], "value2": 30000 - temp2[2], "color": "03", "radius": ['39%', '50%']},
                {"name": str(int(temp1[3]))+"至"+str(int(temp1[4]))+"年", "value": temp2[3], "value2": 30000 - temp2[3], "color": "04", "radius": ['49%', '60%']},
                {"name": str(int(temp1[4]))+"至"+str(int(temp1[5]))+"年", "value": temp2[4], "value2": 30000 - temp2[4], "color": "05", "radius": ['59%', '70%']},
                {"name": str(int(temp1[5]))+"年及以上", "value": temp2[5], "value2": 30000 - temp2[5], "color": "06", "radius": ['69%', '80%']}
            ]
        }
        df = pd.read_csv("不同工作地点的岗位数量.csv", encoding='gbk')
        temp1 = list(df["城市"])
        temp2 = list(df["岗位名"])
        self.map_1_data = {
            'symbolSize': 20000,
            'data': [
                {
                    "name": temp1[0],
                    "value": int(temp2[0])
                },
                {
                    "name": temp1[1],
                    "value": int(temp2[1])
                },
                {
                    "name": temp1[2],
                    "value": int(temp2[2])
                },
                {
                    "name": temp1[3],
                    "value": int(temp2[3])
                },
                {
                    "name": temp1[4],
                    "value": int(temp2[4])
                },
                {
                    "name": temp1[5],
                    "value": int(temp2[5])
                },
                {
                    "name": temp1[6],
                    "value": int(temp2[6])
                },
                {
                    "name": temp1[7],
                    "value": int(temp2[7])
                },
                {
                    "name": temp1[8],
                    "value": int(temp2[8])
                },
                {
                    "name": temp1[9],
                    "value": int(temp2[9])
                },
                {
                    "name": temp1[10],
                    "value": int(temp2[10])
                },
                {
                    "name": temp1[11],
                    "value": int(temp2[11])
                },
                {
                    "name": temp1[12],
                    "value": int(temp2[12])
                },
                {
                    "name": temp1[13],
                    "value": int(temp2[13])
                },
                {
                    "name": temp1[14],
                    "value": int(temp2[14])
                },
                {
                    "name": temp1[15],
                    "value": int(temp2[15])
                },
                {
                    "name": temp1[16],
                    "value": int(temp2[16])
                },
                {
                    "name": temp1[17],
                    "value": int(temp2[17])
                },
                {
                    "name": temp1[18],
                    "value": int(temp2[18])
                },
                {
                    "name": temp1[19],
                    "value": int(temp2[19])
                },
                {
                    "name": temp1[20],
                    "value": int(temp2[20])
                },
                {
                    "name": temp1[21],
                    "value": int(temp2[21])
                },
                {
                    "name": temp1[22],
                    "value": int(temp2[22])
                },
                {
                    "name": temp1[23],
                    "value": int(temp2[23])
                },
                {
                    "name": temp1[24],
                    "value": int(temp2[24])
                },
                {
                    "name": temp1[25],
                    "value": int(temp2[25])
                },
                {
                    "name": temp1[26],
                    "value": int(temp2[26])
                },
                {
                    "name": temp1[27],
                    "value": int(temp2[27])
                },
                {
                    "name": temp1[28],
                    "value": int(temp2[28])
                },
                {
                    "name": temp1[29],
                    "value": int(temp2[29])
                },
                {
                    "name": temp1[30],
                    "value": int(temp2[30])
                },
                {
                    "name": temp1[31],
                    "value": int(temp2[31])
                },
                {
                    "name": temp1[32],
                    "value": int(temp2[32])
                },
                {
                    "name": temp1[33],
                    "value": int(temp2[33])
                },
                {
                    "name": temp1[34],
                    "value": int(temp2[34])
                },
                {
                    "name": temp1[35],
                    "value": int(temp2[35])
                },
                {
                    "name": temp1[36],
                    "value": int(temp2[36])
                },
                {
                    "name": temp1[37],
                    "value": int(temp2[37])
                },
                {
                    "name": temp1[38],
                    "value": int(temp2[38])
                },
                {
                    "name": temp1[39],
                    "value": int(temp2[39])
                },
                {
                    "name": temp1[40],
                    "value": int(temp2[40])
                },
                {
                    "name": temp1[41],
                    "value": int(temp2[41])
                },
                {
                    "name": temp1[42],
                    "value": int(temp2[42])
                },
                {
                    "name": temp1[43],
                    "value": int(temp2[43])
                },
                {
                    "name": temp1[44],
                    "value": int(temp2[44])
                }
            ]
        }

    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echart2(self):
        data = self.echart2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        return echart

    @property
    def echarts3_1(self):
        data = self.echarts3_1_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_2(self):
        data = self.echarts3_2_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echarts3_3(self):
        data = self.echarts3_3_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart4(self):
        data = self.echart4_data
        echart = {
            'title': data.get('title'),
            'names': [i.get("name") for i in data.get('data')],
            'xAxis': data.get('xAxis'),
            'data': data.get('data'),
        }
        return echart

    @property
    def echart5(self):
        data = self.echart5_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def echart6(self):
        data = self.echart6_data
        echart = {
            'title': data.get('title'),
            'xAxis': [i.get("name") for i in data.get('data')],
            'data': data.get('data'),
        }
        return echart

    @property
    def map_1(self):
        data = self.map_1_data
        echart = {
            'symbolSize': data.get('symbolSize'),
            'data': data.get('data'),
        }
        return echart


class SourceData(SourceDataDemo):

    def __init__(self):
        """
        按照 SourceDataDemo 的格式覆盖数据即可
        """
        super().__init__()
        self.title = '计算机行业招聘大数据'

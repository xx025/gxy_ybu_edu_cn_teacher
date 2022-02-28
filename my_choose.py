

import json


data = json.load(open('json/teachers_url.json', encoding='utf8'))

need_major = ["计算机技术", "计算机应用技术"]

need_th = set()
for i in data:
    if i["major_name"] in need_major:
        for k in i["supervisor"]:
            need_th.add(k["name"])

data_2 = json.load(open('json/data.json', encoding='utf8'))

data_3 = []
for i in data_2:
    if i["姓名"] in need_th:
        data_3.append(i)

data_4 = []
for i in data_3:
    data_4.append([k[1] for k in i.items()])





# @File    : DownImg.py.py
# coding: utf8

import json
import os
import re

os.makedirs('./image/', exist_ok=True)


def urllib_download(IMAGE_URL, ID, imgtype):
    from urllib.request import urlretrieve
    urlretrieve(IMAGE_URL, './image/' + ID + imgtype)
    return True


def request_download(IMAGE_URL, ID, imgtype):
    import requests
    r = requests.get(IMAGE_URL)
    with open('./image/' + ID + imgtype, 'wb') as f:
        f.write(r.content)
        return True


def chunk_download(IMAGE_URL, ID, imgtype):
    import requests
    r = requests.get(IMAGE_URL, stream=True)
    with open('./image/' + ID + imgtype, 'wb') as f:
        for chunk in r.iter_content(chunk_size=32):
            f.write(chunk)
            return True


def imgDown(url, filenem, imgtype, age=""):
    if os.path.exists("./image/" + filenem + imgtype):
        return True  # 文件已存在
    else:
        print(age + "文件不存在，开始下载:" + filenem + imgtype)
        if urllib_download(url, filenem, imgtype):
            return True
        elif request_download(url, filenem, imgtype):
            return True
        elif chunk_download(url, filenem, imgtype):
            return True
        else:
            return False


data_2 = json.load(open('../json/data.json', encoding='utf8'))

data_4 = []
for i in data_2:
    if i['照片'] != None:
        data_4.append([i['姓名'], i['照片']])

for i in data_4:
    imgTYPE = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', i[1])[0]
    if imgDown(url=i[1], filenem=i[0], imgtype=imgTYPE):
        pass
    else:
        print("失败", i)

"""
此脚本可获取https://gxy.ybu.edu.cn/yjsjy/dsjj.htm，研究生导师姓名和对应个人主页超链接

将获取到的信息输出到文件：teachers_url.json 和url.json

"""

import json

from urllib.request import Request, urlopen

from bs4 import BeautifulSoup
from requests import RequestException


def get_one_page(url, headers):
    req = Request(url=url, headers=headers, method='POST')
    try:
        response = urlopen(req)
        if response.getcode() == 200:
            return BeautifulSoup(str(response.read(), 'utf-8'), features="html.parser")
        return None
    except RequestException:
        return None


def is_title(element):
    return len(element.select(".MsoNormal strong  span")) > 0


def get_title(element):
    return element.select(".MsoNormal strong  span")[0].text


def get_teachers(element):
    def get_name(element):
        try:
            return element.select("p span")[0].text
        except:
            return None

    def get_url(element):
        try:
            return element.select("p a")[0].get('href')
        except:
            return None

    teachers = []
    for i in element.select("td"):
        name = get_name(i)
        if name is not None and name != '':
            teachers.append({"name": name, "url": get_url(i)})

    return teachers


def main():
    headers = json.load(open('json/headers.json'))
    headers = headers[0]
    url = 'https://gxy.ybu.edu.cn/yjsjy/dsjj.htm'
    data = []
    url_ter = {}
    filename = 'json/teachers_url.json'
    if __name__ == '__main__':
        soup = get_one_page(url=url, headers=headers)
        tbody = soup.select('.v_news_content tbody tr')

        for i in tbody:
            if is_title(i):
                data.append({"major_name": get_title(i)})
            else:
                if len(data) > 0:
                    if "supervisor" not in data[len(data) - 1]:
                        data[len(data) - 1]["supervisor"] = []
                    teachers = get_teachers(element=i)
                    data[len(data) - 1]["supervisor"].extend(teachers)
                    for i in teachers:
                        if i["name"] not in url_ter:
                            url_ter[i["name"]] = i['url']
        with open(filename, 'w', encoding='UTF-8') as f:
            json.dump(data, f, ensure_ascii=False)

        with open("json/url.json", 'w', encoding='UTF-8') as f:
            json.dump(url_ter, f, ensure_ascii=False)


main()

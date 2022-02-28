import json
import time

from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.chrome.options import Options

options = Options()

options.page_load_strategy = 'normal'


def driver_select(ddriver: WebDriver, css_s, dtype='text', i=0):
    if dtype == 'text':
        try:
            return ddriver.find_elements_by_css_selector(css_s)[i].text
        except:
            return None

    else:
        try:
            return ddriver.find_elements_by_css_selector(css_s)[i].get_attribute(dtype)
        except:
            return None


def get_info(d_driver: WebDriver, url):
    d_driver.get(url)
    time.sleep(3)
    return {'姓名': driver_select(d_driver, "#profile_xm"),
            '照片': driver_select(d_driver, "#avatar_show img", 'src', 0),
            '国籍': driver_select(d_driver, "#profile_country"),
            '职称': driver_select(d_driver, "#profile_zc"),
            '荣誉称号': driver_select(d_driver, "#profile_dslx"),
            '电话': driver_select(d_driver, '#collapse-nav-li span', i=3),
            '邮箱': driver_select(d_driver, '#collapse-nav-li span', i=7),
            '所在学科': driver_select(d_driver, "#profile_xk"),
            '研究方向': driver_select(d_driver, "#profile_yjbm"),
            '目前就职': driver_select(d_driver, "#profile_yjfx"),
            '所在科室': driver_select(d_driver, "#profile_ejbm"),
            '主页地址': driver_select(d_driver, "#profile_ejbm a", 'href')
            }


if __name__ == '__main__':

    ddriver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)  # chrome插件路径

    urls = json.load(open('json/url.json', encoding='utf-8'))

    mydata = []
    for j in urls.items():
        if j[1] is not None:
            one_info = get_info(d_driver=ddriver, url=j[1])
            print(one_info)
            mydata.append(one_info)

    with open("json/data.json", 'w', encoding='UTF-8') as f:
        json.dump(mydata, f, ensure_ascii=False)
    ddriver.quit()

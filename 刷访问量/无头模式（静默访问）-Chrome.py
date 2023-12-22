# -*- coding = utf-8 -*-
# @Time:2023/3/28 17:54
# @Author:CK
# @File:无头模式（静默访问）-Chrome
# @Software:PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def chrome_get(url):
    op = Options()
    op.add_argument('-headless')
    op.add_experimental_option('excludeSwitches', ['enable-logging']) # 无日志模式
    op.add_experimental_option("prefs", {"profile.managed_default_content_settings.images":2}) # 不加载图片
    op.add_argument('--incognito') # 无痕，防止浏览多次呗限制访问
    op.add_argument('disable-infobars') # 禁止显示“chrome正受到自动测试软件的控制”提示
    op.add_argument('--test-type')
    op.add_argument('--ignore-certificate-errors') # 与上面一条合并使用：忽略证书错误
    op.add_argument('--no-first-run') # 不打开首页
    op.add_argument('--window-size=0,0') # 设置初始窗口大小
    driver = webdriver.Chrome(options=op)
    driver.get(url)
    driver.quit()

url = input("请输入url：")
jsq = 0
while True:
    chrome_get(url)
    jsq += 1
    print('\r', url, '的访问次数：', jsq, end='', flush=True)
# -*- coding = utf-8 -*-
# @Time:2023/3/28 18:02
# @Author:CK
# @File:无头模式（静默访问）-Firefox
# @Software:PyCharm

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def edge_get(url):
    op = Options()
    op.add_argument('-headless') # 无头模式
    op.add_argument('--incognito') # 无痕，防止浏览多次呗限制访问
    op.add_argument('disable-infobars') # 禁止显示“xxx正受到自动测试软件的控制”提示
    op.add_argument('--test-type')
    op.add_argument('--ignore-certificate-errors') # 与上面一条合并使用：忽略证书错误
    op.add_argument('--no-first-run') # 不打开首页
    op.add_argument('--window-size=0,0') # 设置初始窗口大小
    driver = webdriver.Firefox(options=op)
    driver.get(url)
    driver.quit()

url = input("请输入url：")
jsq = 0
while True:
    jsq += 1
    edge_get(url)
    print('\r',url,'的访问次数：', jsq , end='', flush=True)
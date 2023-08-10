from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service  # 新增
import gameme as ga
import time
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
yanzheng = ['../resource/yanzheng.png', '../resource/yanzheng1.png']

for i in range(6, 300):

    # 打开列表啊网页
    url = 'https://www.2bulu.com/track/list-%25E4%25B9%2589%25E4%25B9%258C%25E5%25B8%2582-----'+str(i)+'.htm?sortType=2'#以该链接为例
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
    }
    service = Service(executable_path='E:/anaconda/envs/game/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1920, 1080)
    driver.get(url)
    driver.implicitly_wait(0.5)

    if i > 1:
        # 登录
        name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/ul[2]/li[1]/input")
        name.send_keys('your name')
        code = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/ul[2]/li[3]/input")
        code.send_keys('your code')
        ga.movepng(yanzheng, 0.95, 0.5)
        lo_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/span')

        lo_button.click()
        time.sleep(2)

    content = driver.find_elements(By.CLASS_NAME, "guiji_discription")# 通过标签名称进行定位

    # 获取每一页的每个轨迹链接
    href = []
    for k in content:
        href_ = k.find_element(By.TAG_NAME, "a").get_attribute('href')
        href.append(href_)
        print(href_)

    if i == 1:
        # 登录
        login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/ul/li[4]")
        login.click()
        name = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/ul[2]/li[1]/input")
        name.send_keys('your name')
        code = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/ul[2]/li[3]/input")
        code.send_keys('your code')
        ga.movepng(yanzheng, 0.95, 0.5)
        lo_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/span')

        lo_button.click()
        time.sleep(2)

    # 下载该数据
    for i in href:
        driver.get(i)
        time.sleep(2)
        ga.clickpng('../resource/download.png', 0.95, 1)
        ga.clickpng('../resource/local.png', 0.95, 1)
        ga.movepng(yanzheng, 0.95, 1)
        ga.clickpng('../resource/KML.png', 0.95, 1)
        time.sleep(2)




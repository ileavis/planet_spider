from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# 设置并初始化WebDriver
def setup_driver():
    # 配置 Edge 选项
    edge_options = Options()
    edge_options.add_argument("--start-maximized")  # 最大化窗口
    edge_options.add_argument("--disable-notifications")  # 禁用通知

    # 指定 EdgeDriver 路径
    service = Service('/Users/paynejlli/Downloads/edgedriver_mac64_m1/msedgedriver')  # 请替换为你的 EdgeDriver 路径

    # 创建 WebDriver 对象
    driver = webdriver.Edge(service=service, options=edge_options)
    return driver


# 等待登录成功
def wait_for_login(driver):
    # 等待user-container元素出现，表示登录成功
    WebDriverWait(driver, 50).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='user-container']"))
    )


# 点击“精华”选项卡
def click_highlight_tab(driver):
    # 点击“精华”选项卡
    highlight_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "//div[@class='menu-container']//div[contains(text(), '精华') and contains(@class, 'item ng-star-inserted')]"))
    )
    highlight_tab.click()


# 获取页面源代码
# 获取页面源代码并滚动加载所有精华文章
def get_page_source(driver, url):
    # 打开目标网页
    driver.get(url)

    # # 等待扫码登录成功
    # wait_for_login(driver)

    # # 点击“精华”选项卡
    # click_highlight_tab(driver)

    # 初始化一个变量来保存上一次的文章数量
    previous_post_count = 0

    while True:
        # 等待精华文章加载完成
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='topic-container']"))
        )

        # 模拟滚动到底部
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 等待新内容加载
        time.sleep(5)  # 等待额外时间确保内容完全加载

        # 获取当前的文章数量
        current_post_count = len(driver.find_elements(By.XPATH, "//div[@class='talk-content-container']"))

        # 如果文章数量没有变化，说明已经加载完毕
        if current_post_count == previous_post_count:
            break

        # 更新文章数量
        previous_post_count = current_post_count

    # 获取最终页面源代码
    page_source = driver.page_source
    return page_source


# 解析页面源代码
def parse_page_source(page_source):
    # 使用 BeautifulSoup 解析页面
    soup = BeautifulSoup(page_source, 'html.parser')

    # 提取精华帖子的内容
    posts_content = []
    for container in soup.find_all('div', class_='talk-content-container'):
        post = container.find('div', class_='content')
        posts_content.append(post.get_text(strip=True))
        posts_content.append("\n \n ====================分割线=======================  \n \n")

    return posts_content


# 将精华文章存储到本地文件
def save_to_file(posts_content, filename='highlight_posts.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for content in posts_content:
            file.write(content + '\n')

def after_login(driver, url):
    # 打开目标网页
    driver.get(url)

    # 等待扫码登录成功
    wait_for_login(driver)


# 主函数
def main():
    url = 'https://wx.zsxq.com/group/15552545485212'

    # 设置 WebDriver
    driver = setup_driver()

    try:
        after_login(driver, url)

        # 获取页面源代码
        page_source = get_page_source(driver, url)

        # 解析页面源代码
        posts_content = parse_page_source(page_source)

        # 保存精华文章到本地文件
        save_to_file(posts_content)

        print("精华文章已成功保存到本地文件。")
    finally:
        # 关闭浏览器
        driver.quit()


if __name__ == "__main__":
    main()

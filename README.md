# 精华文章抓取工具

## 介绍
这是一个使用Python编写的脚本，用于自动抓取指定网页上的精华文章，并将其保存到本地文件中。该脚本使用了Selenium库来模拟浏览器操作，并使用BeautifulSoup库来解析页面源代码。

## 功能
- 自动打开指定网页并登录（如果需要）
- 点击“精华”选项卡以加载相关内容
- 模拟滚动到底部以加载所有精华文章
- 解析页面源代码并提取精华帖子的内容
- 将提取到的精华文章保存到本地文件中

## 使用方法
1. 确保已安装Python环境，并安装所需的库：
    ```bash
    pip install selenium beautifulsoup4
    ```
2. 下载对应浏览器的WebDriver，我这里用的是Edge,因此下载[EdgeDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)，并将其路径替换到脚本中的相应位置。
3. 修改脚本中的目标URL为你想要抓取的网页地址。
4. 运行脚本：
    ```bash
    python planet_spider.py
    ```

## 注意事项
- 请确保你有权抓取和使用该网站的内容。
- 如果网站有反爬虫机制，可能需要添加额外的处理逻辑。
- 由于网页结构可能会变化，如果脚本无法正常工作，请检查XPath等选择器。
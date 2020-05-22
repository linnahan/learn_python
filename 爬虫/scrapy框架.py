'''scrapy的使用步骤
步骤1：创建一个工程和Spider模板
\>scrapy startproject Demo
\>cd Demo
\>scrapy genspider stocks Demo.com
进一步修改spiders/stocks.py文件
步骤2：编写Spider
配置stocks.py文件
修改对返回页面的处理
修改对新增URL爬取请求的处理
步骤3：编写Item Pipeline
配置pipelines.py文件
定义对爬取项(Scraped Item)的处理类
配置ITEM_PIPELINES选项
步骤4：优化配置策略'''

'''Scrapy爬虫的数据类型
Request类、Response类、Item类'''
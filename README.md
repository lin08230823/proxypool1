# proxypool1

基于 django 制作的 IP 池，本项目使用 requests+bs4 爬取数据，依托 django 数据库系统保存，通过网络请求从数据库内获取 IP。

## 运行环境

- python 3+
- django 1.10
- linux/windows

## 运行依赖包

- requests
- bs4
- lxml
- selenium
- PhantomJS

## 下载使用

`git clone https://github.com/lin08230823/proxypool1.git`

进入项目文件夹

创建超级用户

`python manage.py createsuperuser`

依次输入用户名和密码即可

## 运行 django 项目

`$ python manage.py runserver`

访问首页: http://127.0.0.1:8000/proxy/

### 运行爬虫任务
#### 1、windows 下计划任务

将 run_spider.py 加入计划任务

参考: http://mp.weixin.qq.com/s/JKFvnmtlEqaE8GxbX6Fpyw

#### 2、linux-cron

命令行下

`$ crontab -e `

添加计划任务，示例

`0 */4 * * *  python3 run_spider.py`

表示每 4 个小时运行一遍爬取任务

#### 2、手动运行

进入项目文件夹

`$ python manage.py runserver`

进入 http://127.0.0.1:8000/proxy/work/
手动点击 Start 按钮运行


## 项目说明

### 爬取 IP

#### 爬取流程

请求网站 --> 获得代理 --> 存入数据库

#### 文件说明

爬虫文件在 spider 文件夹下

验证、去重整理等文件在 utils 文件夹下

#### 目前爬取的网站

- IP181
- 快代理
- 66 代理
- 西刺代理

### 验证 IP

#### 文件说明

验证 IP 文件在 utils 文件夹下 VerifyProxy.py

#### 验证流程

请求 3 个网站，全部通过 --> 验证成功

### 整理 IP

#### 文件说明

整理数据库内 IP 的文件为 utils 文件夹下的 SortDt.py

#### 整理流程

清除重复的 IP

删除连续验证失败超过 5 次的 IP

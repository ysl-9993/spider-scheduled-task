# spider-scheduled-task

![Package Version]

这是一款微信文章采集的开源定时任务工具，基于([wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter))，支持自定义输出路径、定时时间、请求ip等参数，需要定期维护X-Auth-Key。

## 项目结构
```txt
SPIDER-SCHEDULED-TASK/
├── logs/                          # 运行日志目录
├── output/                        # 爬虫结果输出目录
│   ├── article_content/           # 文章内容文件输出目录
│   ├── article_list/              # 文章列表文件输出目录
│   └── final_output/              # 最终结果输出目录
├── .env                           # 环境变量配置文件
├── datetime_util.py               # 时间戳转换模块
├── log_util.py                    # 日志工具模块
├── main.py                        # 项目入口文件
├── README.md                      # 项目说明文档
├── requirement.txt                # 项目依赖清单
├── target_accounts.json           # 目标公众号账号配置
├── xls_headers.json               # Excel表头配置
└── project_structure.txt          # 项目结构说明
```

## 操作步骤

### 1. 安装依赖

```bash
pip install -r requirement.txt
```

### 2. 配置环境变量
在项目根目录修改`.env`文件，配置以下环境变量：
- 请求地址：`API_BASE_URL`项目运行的ip地址和端口号，默认值为`http://127.0.0.1:3000/`
- api密钥：`X-Auth-Key`登录后获取的密钥，失效后需要重新登录获取，具体获取方式参考[wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter)的说明文档。
- 其他环境变量按需配置

### 3. 运行项目

```bash
python main.py
```

### 4. 维护X-Auth-Key
`X-Auth-Key`过期后，重新登录获取最新X-Auth-Key。在`.env`文件中更新`X-Auth-Key`值。

## 声明
- 本项目基于[wechat-article-exporter](https://github.com/wechat-article/wechat-article-exporter)，感谢原作者的贡献。
- 本项目仅用于学习和研究，不涉及任何商业用途。
- 本项目的所有代码均遵循MIT开源协议，您可以在遵守协议的前提下自由使用、修改和分发本项目的代码。

## 最后
- 如果本项目对您有帮助，欢迎给个star，欢迎二次开发，欢迎提交issue。

<!-- Definitions -->
[Package Version]: https://img.shields.io/github/package-json/v/ysl-9993/spider-scheduled-task

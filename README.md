# rad_getURL

## rad 简介
rad，全名 Radium，名字来源于放射性元素——镭, 从一个URL开始，辐射到一整个站点空间



rad 文档：https://github.com/chaitin/rad

> 一款专为安全扫描而生的浏览器爬虫



下载地址
https://github.com/chaitin/rad/releases


## rad_getURL 作用


目前 rad 不支持批量扫描，但已经支持扫描结果导出，因此使用 python 控制 rad 进行批量扫描

## rad_getURL 使用



将 rad_getURL.py 放在 rad 同一文件夹。



创建 url.txt , 里面放入支持 rad 解析的 domain / ip 格式

```python
python3 rad_getURL.py
```


运行后会将 rad 扫描的结果导入到 url.txt 中每一行  domain / ip  的 txt 格式



最后根据自己需要合并成一个文件：

```bash
cat filter_*.txt > final.txt
```



## rad_getURL 优化



具体参考 rad 自带的 rad_config.yml配置文件的参数配置

```yml
enable-image-display: false                  # 启用图片显示，适用于需要验证码登录的情况，启用wait-login自动开启
load-wait: 2                                 # 页面加载完毕后的等待时间，单位秒，网速不佳时可尝试调大该值
exec-path: ""                                # 启动chrome的路径，为空会自动在默认路径寻找
disable-headless: false                      # 禁用无头模式
request-config:                              # 请求头配置
  user-agent: ""                             # 请求user-agent配置
  headers:                                   # 请求header配置
  - key: ""                                  # header的key
    value: ""                                # header的value
  cookies:                                   # 请求cookie配置
  - name: ""                                 # cookie的name
    value: ""                                # cookie的value
restrictions-on-urls:                        # 对爬取的URL的一些限制项
  disallowed-suffix: []                      # 不允许的文件后缀
  disallowed-keywords-in-path-and-query: []  # 不允许的URL关键字
  disallowed-domain: []                      # 不允许的域名
  disallowed-urls: []                        # 不允许的URL（正则）
  allowed-domains: []                        # 允许的域名，起始目标会被自动加入其中
  allowed-urls: []                           # 允许的URL（正则）
restrictions-on-requests:                    # 对请求行为的一些限制项
  max-concurrent: 10                         # 最大页面并发（不大于10）
  max-depth: 5                               # 最大页面深度限制
  max-click-depth: 5                         # 一个页面中最大点击深度限制
  max-count-of-page: 1000                    # 最多爬取的页面数量限制
  max-click-or-event-trigger: 1000           # 单个页面中最大点击或事件触发次数(不大于10000)
  click-or-event-interval: 1000              # 点击间隔，单位毫秒
```

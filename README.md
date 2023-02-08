# nonebot2磁力搜索插件

## 整活, 不会真的有人找bot要磁力链接吧

功能: 磁力搜索, 通过机器人帮你寻找 电影 或者 学习资料

使用的磁力站: https://clm9.me

安装方式:
    
    pip install nonebot_plugin_BitTorrent
    nb plugin install nonebot_plugin_BitTorrent
    Download Zip

env配置项:

    magnet_max_num     返回多少条结果, 类型int, 默认3                   例: magnet_max_num = 3
    clm_cookie         网站的cookie, 类型string, 自己手动从浏览器拿     例: clm_cookie = "challenge=245e59e7113b306df50012730449181e; _ga=GA1.1.795400257.1664117811; _ga_W7KV15XZN0=GS1.1.1664165687.2.1.1664165691.0.0.0"
    clm_useragent      网站的user-agent, 类型string, 自己手动从浏览器拿  例: clm_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50"
    
    注: clm_cookie和clm_useragent必须配置当前ip所获取到的
    
    
指令:

    磁力搜索 xxx | bt xxx   (xxx为关键词)
    例如: 磁力搜索 真夏の夜の淫夢



cookie以及user-agent的拿法:

    浏览器进入: https://clm9.me
    edge按f12, 点击又上角那个">>"符号, 进入那个"网络"
    按ctrl+r刷新元素
    随便点击一个文件, 在请求标头里面找到cookie
    cookie冒号后面的就是cookie, 可以把他放进env里面了
    user-agent同理
    


这个网站的cookie和user-agent我不太确定能用多久, 失效了就换cookie以及user-agent试试看

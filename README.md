# nonebot2磁力搜索插件

安装方式:

    Download Zip

env配置项:

    magnet_max_num     返回多少条结果, 类型int, 默认3                     例:magnet_max_num = 3
    clm_cookie         网站的cookie, 类型string, 自己手动从浏览器拿        例: clm_cookie = "challenge=8b11e0a1c25a29ca8cd6b530e64c5294; ex=1; _ga=GA1.1.1219749203.1655966067; _ga_W7KV15XZN0=GS1.1.1655966067.1.1.1655966427.0"


cookie的拿法:

    浏览器进入: https://clm9.me/
    edge按f12, 点击又上角那个">>"符号, 进入那个"网络"
    按ctrl+r刷新元素
    随便点击一个文件, 在请求标头里面找到cookie
    cookie冒号后面的就是cookie, 可以把他放进env里面了


这个网站的cookie我不太确定能用多久, 失效了就换cookie试试看

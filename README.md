# nonebot2磁力搜索插件

功能: 磁力搜索, 通过机器人帮你寻找 电影 或者 学习资料

使用的磁力站: https://cili.site

安装方式:
    
    pip install nonebot_plugin_BitTorrent
    nb plugin install nonebot_plugin_BitTorrent
    Download Zip
    git clone https://github.com/Special-Week/nonebot_plugin_BitTorrent.git

env配置项:

    magnet_max_num    # 返回多少条结果, 类型int, 默认3, 最大12               例: magnet_max_num = 3
    onebot_group_forward_msg    # 在onebotv11适配器下是否转发消息, 类型bool, 默认False, 仅支持onebot  例: onebot_group_forward_msg = True


​    
​    
指令:

    磁力搜索 xxx | bt xxx   (xxx为关键词)
    例如: 磁力搜索 真夏の夜の淫夢
          bt 真夏の夜の淫夢
    注: 响应器是由on_command生成的, 需要带上env中配置的COMMAND_START前缀(默认["/"], 可设置空字符串[""])


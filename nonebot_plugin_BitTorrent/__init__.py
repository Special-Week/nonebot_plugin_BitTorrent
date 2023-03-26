from nonebot import on_command

from .utils import bittorrent

# 声明一个响应器, 优先级10, 向下阻断
on_command("磁力搜索", aliases={'bt'}, priority=10, block=True,handlers=[bittorrent.main])


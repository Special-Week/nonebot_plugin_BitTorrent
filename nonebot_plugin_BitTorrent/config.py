from nonebot import get_driver
from pydantic import BaseSettings


class Config(BaseSettings):
    magnet_max_num: int = 3
    onebot_group_forward_msg: bool = False

    class Config:
        extra = "ignore"


# 实例化配置对象
config = Config.parse_obj(get_driver().config)

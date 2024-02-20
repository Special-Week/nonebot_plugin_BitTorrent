from nonebot import get_driver
from pydantic import BaseModel, parse_obj_as


class Config(BaseModel):
    magnet_max_num: int = 3
    onebot_group_forward_msg: bool = False



# 实例化配置对象
config = parse_obj_as(Config, get_driver().config.dict())
from loguru import logger
from nonebot import get_driver


class EnvException(Exception):
    pass


"""为了解决同时兼容pydantic v1和v2, 于是我觉得不使用pydantic了 ("""


class Config:
    def __init__(self) -> None:
        """
        没有什么情况是if解决不了的，如果有，那就if嵌套 (
        """

        whole_config = get_driver().config
        try:
            self.max_num = int(whole_config.magnet_max_num)
            if self.max_num < 1 or self.max_num > 12:
                raise EnvException
        except Exception:
            logger.warning("配置文件中的 magnet_max_num 不合法或为空，已使用默认值 3")
            self.max_num = 3

        try:
            self.forward_msg = str(whole_config.onebot_group_forward_msg)
            if self.forward_msg in {"True", "true"}:
                self.forward_msg = True
            elif self.forward_msg in {"False", "false"}:
                self.forward_msg = False
            else:
                raise EnvException
        except Exception:
            logger.warning(
                "配置文件中的 onebot_group_forward_msg 不合法或为空，已使用默认值 False"
            )
            self.forward_msg = False


config = Config()

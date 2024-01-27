import asyncio
import contextlib
from typing import Any, Coroutine, List

from bs4 import BeautifulSoup, Tag
from httpx import AsyncClient
from loguru import logger
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.internal.adapter import Bot, Event, Message
from nonebot.matcher import Matcher
from nonebot.params import CommandArg

from .config import config


class BitTorrent:
    magnet_url = "https://cili.site"

    async def main(
        self,
        bot: Bot,
        matcher: Matcher,
        event: Event,
        msg: Message = CommandArg(),
    ) -> None:
        """主函数, 用于响应命令"""

        print("开始搜索")
        keyword: str = msg.extract_plain_text()
        if not keyword:
            await matcher.finish("虚空搜索?来点车牌gkd")
        try:
            data: List[str] = await self.get_items(keyword)
        except Exception as e:
            await matcher.finish("搜索失败, 下面是错误信息:\n" + repr(e))
        if not data:
            await matcher.finish("没有找到结果捏, 换个关键词试试吧")
        # 如果开启了群消息转发, 且消息来自onebotv11的群消息
        if config.onebot_group_forward_msg and isinstance(event, GroupMessageEvent):
            messages: List = [
                {
                    "type": "node",
                    "data": {
                        "name": "bot",
                        "uin": bot.self_id,
                        "content": i,
                    },
                }
                for i in data
            ]
            await bot.call_api(
                "send_group_forward_msg", group_id=event.group_id, messages=messages
            )
        else:
            await matcher.finish("\n".join(data))

    async def get_items(self, keyword) -> List[str]:
        search_url: str = f"{self.magnet_url}/search?q={keyword}"
        async with AsyncClient() as client:
            try:
                resp = await client.get(search_url)
            except Exception as e:
                logger.error(repr(e))
                return [f"获取{search_url}失败， 错误信息：{repr(e)}"]
        soup = BeautifulSoup(resp.text, "lxml")
        tr = soup.find_all("tr")
        if not tr:
            return []
        a_list: list[Any] = [i.find_all("a") for i in tr]
        href_list: list[str] = [self.magnet_url + i[0].get("href") for i in a_list if i]
        maxnum: int = min(len(href_list), config.magnet_max_num)
        tasks: List[Coroutine] = [self.get_magnet(i) for i in href_list[:maxnum]]
        return await asyncio.gather(*tasks)

    async def get_magnet(self, search_url: str) -> str:
        try:
            async with AsyncClient() as client:
                resp = await client.get(search_url)
            soup = BeautifulSoup(resp.text, "lxml")
            dl = soup.find("dl", class_="dl-horizontal torrent-info col-sm-9")
            h2 = soup.find("h2", class_="magnet-title")
            if isinstance(dl, Tag) and isinstance(h2, Tag):
                dt = dl.find_all("dt")
                dd = dl.find_all("dd")
                target: str = (
                    f"标题 :: {h2.text}\n磁力链接 :: magnet:?xt=urn:btih:{dd[0].text}\n"
                )
                for i in range(1, min(len(dt), len(dd))):
                    dt_temp: str = (dt[i].text).split("\n")[0]
                    dd_temp: str = (dd[i].text).split("\n")[0]
                    if not dd_temp:
                        with contextlib.suppress(Exception):
                            dd_temp = (dd[i].text).split("\n")[1]
                    target += f"{dt_temp}: {dd_temp}\n"
                logger.info(f"{target}\n====================================")
                return target
            return f"获取{search_url}失败"
        except Exception as e:
            return f"获取{search_url}失败， 错误信息：{repr(e)}"


# 实例化
bittorrent = BitTorrent()

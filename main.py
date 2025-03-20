from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
from pywebshot import screenshot

url1 = "https://v2.xxapi.cn/api/screenshot?url=https://helldiverscompanion.com/#"
url2 = "https://v2.xxapi.cn/api/screenshot?url=https://helldiverscompanion.com/#overview"
output = "example.png"


@register("zb", "灵煞", "网页截图", "v1")
class wangyejituPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        
    @filter.command_group("zb")
    def zb(self):
        pass    
    
    @zb.command("qx")
    async def qx(self, event: AstrMessageEvent):
        
        try:
            s = screenshot(url=url1, output=output)
            yield event.image_result({s})        
        except s as e:
            print(f"请求失败")
            yield event.plain_result("请求失败")
        
    @zb.command("mo")
    async def mo(self, event: AstrMessageEvent):
        
        try:
            s = screenshot(url=url2, output=output)
            yield event.image_result({s})            
        except s as e:
            yield event.plain_result("请求失败")
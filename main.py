from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger
import requests

url1 = "https://v2.xxapi.cn/api/screenshot?url=https://helldiverscompanion.com/#"
url2 = "https://v2.xxapi.cn/api/screenshot?url=https://helldiverscompanion.com/#overview"
headers = {
    'User-Agent': 'xiaoxiaoapi/1.0.0 (https://xxapi.cn)'
}

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
            response = requests.get(
                url1,
                headers=headers,
                timeout=10
            )
        
            # 检查HTTP状态码
            response.raise_for_status()
        
            # 解析JSON响应
            json_data = response.json()
        
            # 检查API返回状态码
            if json_data.get('code') == 200:
                a = json_data.get('data')
                yield event.image_result({a})
            else:
                print(f"API错误：{json_data.get('msg', '未知错误')} (代码：{json_data.get('code')})")
                yield event.plain_result("未知错误")
            
        except requests.exceptions.RequestException as e:
            print(f"请求失败")
            yield event.plain_result("请求失败")
        
    @zb.command("mo")
    async def mo(self, event: AstrMessageEvent):
        
        try:
            response = requests.get(
                url2,
                headers=headers,
                timeout=10
            )
        
            # 检查HTTP状态码
            response.raise_for_status()
        
            # 解析JSON响应
            json_data = response.json()
        
            # 检查API返回状态码
            if json_data.get('code') == 200:
                a = json_data.get('data')
                yield event.image_result({a})
            else:
                print(f"API错误：{json_data.get('msg', '未知错误')} (代码：{json_data.get('code')})")
                yield event.plain_result("未知错误")
            
        except requests.exceptions.RequestException as e:
            print(f"请求失败")
            yield event.plain_result("请求失败")
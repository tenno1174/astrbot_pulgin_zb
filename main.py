import asyncio
from playwright.async_api import async_playwright
from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api.message_components import Image
#灵煞修改绝地潜兵专用版
url2 = "https://helldiverscompanion.com/#overview"
url1 = "https://helldiverscompanion.com/#"

@register("webscreenshot", "沙北", "网页截图", "1.0.0")
class WebpageScreenshotPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)
        self.enabled = True  # 插件初始状态为启用

    #@filter.command("启用截图")
    #async def enable_screenshot(self, event: AstrMessageEvent):
    #    """
    #    启用网页截图功能。
    #    """
    #    self.enabled = True
    #    yield event.plain_result("网页截图功能已启用。")

    #@filter.command("禁用截图")
    #async def disable_screenshot(self, event: AstrMessageEvent):
    #    """
    #    禁用网页截图功能。
    #    """
    #    self.enabled = False
    #    yield event.plain_result("网页截图功能已禁用。")

    @filter.command("qx")
    async def qx(self, event: AstrMessageEvent):
        """
        获取指定网页的截图。

        :param event: 消息事件对象
        :param url: 要截图的网页URL
        :param width: 截图宽度（可选）
        :param height: 截图高度（可选）
        """
        #if not self.enabled:
        #    yield event.plain_result("网页截图功能当前已禁用。")
        #    return

        try:
        #    # 检查URL是否包含协议头，如果没有则添加
        #    if not url.startswith("http://") and not url.startswith("https://"):
        #        url = "https://" + url

        #    # 检查宽度和高度是否同时提供
        #    if width is not None and height is None:
        #        yield event.plain_result("请同时提供宽度和高度。")
        #        return
        #    if width is None and height is not None:
        #        yield event.plain_result("请同时提供宽度和高度。")
        #        return

            # 设置默认宽度和高度
            viewport_width = 1920  # 默认PC宽度
            viewport_height = 1080  # 默认PC高度

            #if width is not None and height is not None:
            #    try:
            #        viewport_width = int(width)
            #        viewport_height = int(height)
            #    except ValueError:
            #        yield event.plain_result("宽度和高度必须是整数。")
            #        return

            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page(viewport={"width": viewport_width, "height": viewport_height})
                await page.goto(url1)
                await page.wait_for_load_state('networkidle')
                
                # 截图
                screenshot_path = "screenshot.png"
                await page.screenshot(path=screenshot_path, full_page=True)
                await browser.close()

            yield event.image_result(screenshot_path)

        except Exception as e:
            yield event.plain_result(f"获取截图失败: {str(e)}")
            
    @filter.command("mo")
    async def mo(self, event: AstrMessageEvent):
        """
        获取指定网页的截图。

        :param event: 消息事件对象
        :param url: 要截图的网页URL
        :param width: 截图宽度（可选）
        :param height: 截图高度（可选）
        """
        #if not self.enabled:
        #    yield event.plain_result("网页截图功能当前已禁用。")
        #    return

        try:
        
            # 设置默认宽度和高度
            viewport_width = 1920  # 默认PC宽度
            viewport_height = 1080  # 默认PC高度

            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page(viewport={"width": viewport_width, "height": viewport_height})
                await page.goto(url2)
                await page.wait_for_load_state('networkidle')
                
                # 截图
                screenshot_path = "screenshot.png"
                await page.screenshot(path=screenshot_path, full_page=True)
                await browser.close()

            yield event.image_result(screenshot_path)

        except Exception as e:
            yield event.plain_result(f"获取截图失败: {str(e)}")        


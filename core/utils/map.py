import base64
import folium
import urllib.parse
from playwright.async_api import async_playwright

class Map:
    @classmethod
    async def generate(cls, location: list):
        map = folium.Map(location=location, zoom_start=5, zoom_control=False)
        folium.Marker(location=location).add_to(map)

        html_str = map.get_root().render()
        data_uri = "data:text/html;charset=utf-8," + urllib.parse.quote(html_str)

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
        
            await page.set_viewport_size({"width": 640, "height": 360})
            await page.goto(data_uri, wait_until="networkidle")

            screenshot_bytes = await page.screenshot(type="png")
        
            screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        
            await browser.close()

        return screenshot_base64

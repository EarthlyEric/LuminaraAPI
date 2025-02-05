import asyncio
import base64
import folium
import urllib.parse
from playwright.async_api import async_playwright

async def generate_map_image(location: list):
    map = folium.Map(location=location, zoom_start=5, zoom_control=False)
    folium.Marker(location=location).add_to(m)

    # 2. 取得地圖的 HTML 字串，並轉成 data URI
    html_str = map.get_root().render()
    data_uri = "data:text/html;charset=utf-8," + urllib.parse.quote(html_str)

    # 3. 啟動 Pyppeteer 的無頭瀏覽器
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        await page.set_viewport_size({"width": 640, "height": 360})
        await page.goto(data_uri, wait_until="networkidle")

        screenshot_bytes = await page.screenshot(type="png")
        
        screenshot_base64 = base64.b64encode(screenshot_bytes).decode("utf-8")
        
        await browser.close()

    # 將取得的 base64 字串轉成 bytes 回傳
    return screenshot_base64


# 測試使用範例
if __name__ == '__main__':
    # 使用 asyncio.run 在非同步環境中執行 generate_map_image
    image_bytes = asyncio.run(generate_map_image([0, 0]))
    
    # 儲存圖片 (例如轉回原始二進位資料，寫成檔案)
    import base64
    with open("screenshot.png", "wb") as f:
        f.write(base64.b64decode(image_bytes))
    
    print("地圖圖片已儲存為 screenshot.png")

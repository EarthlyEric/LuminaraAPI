import os
import asyncio
import uuid
import folium
from selenium import webdriver

class Map():
    @classmethod
    async def generate(cls, location: list):
        map = folium.Map(location=location, zoom_start=5,zoom_control=False)
        folium.Marker(location=location).add_to(map)

        filename = str(uuid.uuid4())
        temp_dir = os.path.abspath("./temp")
        
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        map.save(os.path.join(temp_dir, f"{filename}.html"))

        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')

        driver =  webdriver.Chrome(options=options)
        driver.get("file://" + os.path.abspath(f"./temp/{filename}.html"))
        await asyncio.sleep(4)
        driver.set_window_size(1280, 720)
        screenshot = driver.get_screenshot_as_base64().encode("utf-8")
        driver.quit()
        os.remove(os.path.join(temp_dir, f"{filename}.html"))
        return screenshot

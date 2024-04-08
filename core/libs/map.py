import os
import asyncio
import uuid
import folium
from selenium import webdriver
from concurrent.futures.thread import ThreadPoolExecutor
from pyvirtualdisplay import Display


class Map():
    @classmethod
    async def generate(cls, location: list):
        map = folium.Map(location=location, zoom_start=5)
        pin = folium.Marker(location=location).add_to(map)

        filename = str(uuid.uuid4())
        temp_dir = os.path.abspath("./temp")
        
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        map.save(os.path.join(temp_dir, f"{filename}.html"))

        display = Display(visible=0, size=(1280, 720))
        display.start()

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  
        options.add_argument("--disable-gpu") 
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-infobars")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')

        driver =  webdriver.Chrome(options=options)
        driver.get("file://" + os.path.abspath(f"/temp/{filename}.html"))
        await asyncio.sleep(2)
        driver.set_window_size(1280, 720)
        screenshot = driver.get_screenshot_as_base64()
        driver.quit()
        display.stop()

        return screenshot

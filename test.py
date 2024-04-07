import time
import os
from selenium import webdriver
from PIL import Image
from io import BytesIO
import folium

m = folium.Map(location=[35.709635, 139.810851], zoom_start=5)
pin = folium.Marker(location=[35.709635, 139.810851])

m.save("map.html")
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get("file://" + os.path.abspath("map.html"))
time.sleep(5)
width = driver.execute_script("return document.body.scrollWidth")
height = driver.execute_script("return document.body.scrollHeight")
driver.set_window_size(width, height)
screenshot = driver.get_screenshot_as_png()
driver.quit()
with open("page_screenshot.png", "wb") as f:
    f.write(screenshot)
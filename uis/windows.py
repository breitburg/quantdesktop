import pystray

icon = pystray.Icon('test name')

width = height = 16
color1 = (0, 0, 0)
color2 = (0, 255, 255)
from PIL import Image

image = Image.open("../assets/icon.png")

icon.icon = image

icon.run()
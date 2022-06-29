from datetime import date

from PIL import Image, ImageDraw, ImageFont

width = 512
height = 512


def create_cover():
    last_changed = date.today()

    title = "Discover Weekly Archive"
    m2 = "Last Changed = {last_changed}".format(last_changed=last_changed)

    font1 = ImageFont.truetype("consolab.ttf", size=32)
    font2 = ImageFont.truetype("consolab.ttf", size=18)

    img = Image.new('RGB', (width, height), color='blue')

    imgDraw = ImageDraw.Draw(img)

    imgDraw.text((10, 10), title, font=font1, fill=(255, 255, 0))
    imgDraw.text((10, 430), m2, font=font2, fill=(255, 255, 0))

    img.save('cover.jpeg')

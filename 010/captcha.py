from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndColor():
    return (random.randint(0, 128), random.randint(0, 128), random.randint(0, 128))


def rndColor2():
    return (random.randint(128, 255), random.randint(128, 255), random.randint(128, 255))


def rndChar():
    return chr(random.randint(65, 90))


if __name__ == '__main__':
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(r'..\000\SourceCodePro.ttf', size=36)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndColor())
    for x in range(4):
        draw.text((60 * x + 10, 10), rndChar(), fill=rndColor2(), font=font)

    image = image.filter(ImageFilter.BLUR)
    image.save('captcha.jpg')

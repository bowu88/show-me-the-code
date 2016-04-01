from PIL import Image, ImageFont, ImageDraw

im = Image.open('pic.jpg')
w, h = im.size
font = ImageFont.truetype('SourceCodePro.ttf', 36)
draw = ImageDraw.Draw(im)
draw.text((w * 0.9, h * 0.1), '15', font=font, fill='red')
im.save("num.jpg", 'jpeg')

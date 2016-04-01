from PIL import Image

im = Image.open('resolution.jpg')
w, h = im.size
wtimes = float(w) / 1136
htimes = float(h) / 640
if wtimes > 1 or htimes > 1:
    times = wtimes if wtimes > htimes else htimes
else:
    times = 1
print(times)
print((int(w / times), int(h / times)))
im.resize((int(w / times), int(h / times)))
im.save('change_resolution.jpg', 'jpeg')


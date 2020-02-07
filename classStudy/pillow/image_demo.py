from PIL import Image

im = Image.open("202552lc7.jpg")
# im.save("202552lc7.png")  # 进行格式转换
print(type(im))

r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save("202552lc71.jpg")

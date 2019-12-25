from PIL import Image

im = Image.open("202552lc7nrivdbhhcr7ch.jpg")
print(im.mode)  # RGB

new_im = Image.new("RGB", (128, 128), "#FF0000")
new_im.save("test01.jpg")


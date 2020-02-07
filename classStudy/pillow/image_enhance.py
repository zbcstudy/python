from PIL import Image, ImageEnhance

im = Image.open("202552lc7.jpg")
om = ImageEnhance.Contrast(im)
om.enhance(10).save("2025_enhance.jpg")

from PIL import Image, ImageFilter

im = Image.open("202552lc7.jpg")
om = im.filter(ImageFilter.CONTOUR)
om.save("2025_filter.jpg")

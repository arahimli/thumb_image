from PIL import Image
img = Image.open('Screenshot_2.png')
img.show()
img.thumbnail((800,500))
# img.save('Glacier-National-Park-US-thumb.jpg')
new_img = img.resize((800,500))
new_img.save("car_resized-resize-thumb.png", "PNG", optimize=True)
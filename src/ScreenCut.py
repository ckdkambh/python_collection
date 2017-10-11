from PIL import ImageGrab

im = ImageGrab.grab()

im.save("D:\\screen_cut.jpg", 'jpeg')
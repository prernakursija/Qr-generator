'''we going to use a python library like qrcode and convert url to qr
'''
import qrcode
url=input("Enter your url: ")

filename=input("Enter your file name you want to save it as: ")
if not (filename.endswith(".png")):
    filename=filename+".png"

img = qrcode.make(url)
img.save("{filename}")
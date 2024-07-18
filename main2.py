import qrcode

img = qrcode.make("some data")
img.save("normalQR.png")

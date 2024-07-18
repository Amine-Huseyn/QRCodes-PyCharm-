import segno
qrcode = segno.make_qr("hello world")
qrcode.save("colorfulQR.png",
            scale=7,
            border=4,
            light= "F34723",
            dark = "BOEOE6")
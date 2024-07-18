import segno
qrcode = segno.make_qr("hello world")
qrcode.save("colorfulQR.png",
            scale=7,
            border=4,
            light= "C0C0C0",
            dark = "FF99CC")


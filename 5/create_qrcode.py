import qrcode

image = qrcode.make("https://sajjadaemmi.ir")

image.save("my_website.png")
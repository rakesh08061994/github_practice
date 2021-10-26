# pip install pyqrcode

import pyqrcode
# from pyqrcode import QRCode

# string that will represent in qr code
s = "9887211207"
# Generate QR code
url = pyqrcode.create(s)

# Create an save the .png file
url.svg("number.jpeg",scale=8)
# print(pyqrcode.__doc__)
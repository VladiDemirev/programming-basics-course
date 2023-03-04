import pyqrcode
import png
from pyqrcode import QRCode

address = "https://www.babykoala.bg/"
url = pyqrcode.create(address)
url.png("koala.png", scale=8)
import pyqrcode
url = pyqrcode.QRCode('https://www.python.org/',error='H')
url.png('url2.png',scale=2)
url.png('url3.png',scale=3)
import qrcode
data = input()
qr = qrcode.make()
qr.save('qrcode.png')
print('QR code generated successfully')
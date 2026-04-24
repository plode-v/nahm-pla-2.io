import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data('https://www.nahmplathaidishes.com/menu.html')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("nahmpla_menu_qr_black.png")
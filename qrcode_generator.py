import qrcode

def generate_qr_code(data, filename='qrcode.png'):
    # Create a QR Code object with the specified data
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # Controls how many pixels each "box" of the QR code is
        border=4  # The thickness of the border (default is 4)
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Example usage
data = input("Enter the data for the QR code: ")
generate_qr_code(data)

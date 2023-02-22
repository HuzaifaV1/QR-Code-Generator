# Import the qrcode library
import qrcode

# Define a function to create a QR code from text
def generate_qrcode(text):
    # Create a new QRcode object
    qr = qrcode.QRCode(        
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )

    # Add the text to the QR code
    qr.add_data(text)
    # Create the QR code image `fit=True` tells the library to adjust the size of the QR code to fit all the data
    qr.make(fit=True)
    # Create a image of the QR code with black boxes and a white background 
    image = qr.make_image(fill_color='black', back_color='white')
    # Save the image to a file named 'qrcode.png'
    image.save('qrcode.png')

generate_qrcode('https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley')

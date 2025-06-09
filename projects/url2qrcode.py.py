# ================================================
# CUSTOM QR CODE GENERATOR – DETAILED EXPLANATION
# ================================================

# Required Libraries:
# - `qrcode`: For generating QR codes
# - `Pillow (PIL)`: For manipulating image pixels (custom styling)

# Install with:
# pip install qrcode[pil] Pillow

import qrcode                  # Main library for QR code generation
from PIL import Image, ImageDraw  # For editing the image

# -----------------------------------------------
# STEP 1: Take user input (any URL or text)
# -----------------------------------------------
url = input("Enter the URL or text to encode in QR Code: ")

# -----------------------------------------------
# STEP 2: Configure QR Code settings
# -----------------------------------------------

# We use a QRCode object to customize settings
qr = qrcode.QRCode(
    version=1,  # Controls size: 1 = 21x21 modules, 2 = 25x25, etc.
    error_correction=qrcode.constants.ERROR_CORRECT_H,  
    # Error correction level:
    # L: 7% recovery
    # M: 15%
    # Q: 25%
    # H: 30% (most robust but larger)
    
    box_size=10,  # Pixel size of each box/module
    border=4      # How many boxes thick the border should be
)

# Add data to the QR object
qr.add_data(url)
qr.make(fit=True)  # Optimize layout

# -----------------------------------------------
# STEP 3: Generate QR image (with base colors)
# -----------------------------------------------

# Create initial image — we choose some base colors
base_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# NOTE: Even though we use black/white here, we will override it pixel-by-pixel

# -----------------------------------------------
# STEP 4: Apply Custom Styling (Pixel by Pixel)
# -----------------------------------------------

# Get pixel access object (so we can change pixels)
pixels = base_img.load()
width, height = base_img.size

# Now loop through every pixel and change black pixels only
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        if (r, g, b) == (0, 0, 0):  # Only style the black parts (QR data)
            if (x + y) % 2 == 0:
                pixels[x, y] = (128, 0, 128)  # Purple
            else:
                pixels[x, y] = (0, 128, 0)    # Green
        else:
            pixels[x, y] = (255, 255, 255)    # White background (optional cleanup)

# -----------------------------------------------
# STEP 5: Save the final QR image
# -----------------------------------------------

base_img.save("fancy_qr_code.png")
print("✅ Fancy QR Code saved as 'fancy_qr_code.png'")

# -----------------------------------------------
# BONUS KNOWLEDGE: What Else Can You Add?
# -----------------------------------------------

# 1. ✅ Insert a Logo at the center (Branding)
# 2. ✅ Support for transparent PNGs (use 'RGBA')
# 3. ✅ Add gradients / random colors
# 4. ✅ Auto-detect and validate input URL
# 5. ✅ Make a GUI using Tkinter or PyQt
# 6. ✅ Batch QR code generator from CSV
# 7. ✅ Convert text to QR and back using ZBar (decoding)

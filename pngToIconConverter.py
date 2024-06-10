from PIL import Image

def convert_png_to_ico(png_path, output_ico_path):
    # Open the PNG image
    png_image = Image.open(png_path)

    # Convert PNG to ICO format (must be a square image)
    png_image.save(output_ico_path)
    print(f"Conversion completed. ICO file saved as {output_ico_path}")

# Example usage
png_path = "C://Users//Administrator//Desktop//GUI_TKinter//logo_image.png"
output_ico_path = "C://Users//Administrator//Desktop//GUI_TKinter//logo_image.ico"
convert_png_to_ico(png_path, output_ico_path)

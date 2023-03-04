import PIL
import os

def convert_webp_to_png(webp_file):
  # Open the webp image using PIL.Image.open()
  im = PIL.Image.open(webp_file)
  # Get the file name without extension
  file_name = os.path.splitext(webp_file)[0]
  # Add '.png' to the file name
  png_file = file_name + '.png'
  # Save the image as png using PIL.Image.save()
  im.save(png_file, format="png", lossless=True)

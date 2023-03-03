import PIL
import os
import imghdr

def convert_tiff_to_png(tiff_file):
  # Open the tiff image using PIL.Image.open()
  im = PIL.Image.open(tiff_file)
  # Get the file name without extension
  file_name = os.path.splitext(tiff_file)[0]
  # Add '.png' to the file name
  png_file = file_name + '.png'
  # Save the image as png using PIL.Image.save()
  im.save(png_file, format="png", lossless=True)

# a sensor for detecting any 
def tiff_sensor(Uploaded_image):
  image_type = imghdr.what(Uploaded_image)
  if  image_type == 'tiff':
    return convert_tiff_to_png(Uploaded_image)
  else:
    return None
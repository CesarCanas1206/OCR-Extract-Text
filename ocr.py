
# import the necessary packages
from PIL import Image
import pytesseract
import cv2
import os
# construct the argument parse and parse the arguments
def extract_text(image_path):

	# load the example image and convert it to grayscale
	image = cv2.imread(image_path)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
	# apply OCR to it
	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)
	# load the image as a PIL/Pillow image, apply OCR, and then delete
	# the temporary file
	x=Image.open(filename)
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	custom_config = r'-l eng'
	text = pytesseract.image_to_string(x, config=custom_config)
	os.remove(filename)
	result_txt = "{}.txt".format(os.getpid())
	with open(result_txt,'w') as file:
		file.write(text)
	cv2.waitKey(0)
 
image_path = 'a.jpg'
 
extract_text(image_path)

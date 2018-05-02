from PIL import Image
import cv2
import pytesseract
import numpy
def ReadImage(image):
	img = cv2.imread(image,1) 
	img = cv2.resize(img,(605, 819)) 
	cv2.imwrite('./images/newimage.png',img)    
	img=Image.open('./images/newimage.png')
	area = (20, 630, 605, 819)
	img =img.crop(area) 
	img.save("./images/cropped_picture.jpg") 
	word=pytesseract.image_to_string(Image.open('./images/cropped_picture.jpg'))
	print (word)


# OCR-Tesseract
Convert Image To HTML Text Format 
.
.
.
#Prerequisite
1. Install Python Newer Version.
2. Install OCR-Tesseract as per your system platform.
 https://github.com/UB-Mannheim/tesseract/wiki
.
.
.
#Setup
For Windows **After installation of the "Tesseract" Add the path of the folder into the Envroinment Variable.**
.
.
**Some changes in the script you have to make**
Again Paste Tesseract Folder Path At This Line 
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\iam_kazi\AppData\Local\Tesseract-OCR\tesseract.exe'
.
.
Provide Your Image Folder Path For Source (**It will iterate all images at onces, Do not provide image name**)
listfiles = os.listdir("C:\Data")
.
.
Again paste same path to open image 
img=Image.open("C:\\Data\\"+x) **make sure give double backlashes**
.
.
In My Script, Basically it adds <br> tag after every line.
You can make changes as per your need
.
.
.
Thank You! Enjoy!

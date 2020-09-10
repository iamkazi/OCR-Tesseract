# OCR-Tesseract
Convert Image To HTML Text Format 
.
.
.
<br>
#Prerequisite
<br>
1. Install Python Newer Version.
<br>
2. Install OCR-Tesseract as per your system platform.
<br>
 https://github.com/UB-Mannheim/tesseract/wiki
.
.
.
<br>
#Setup
<br>
For Windows **After installation of the "Tesseract" Add the path of the folder into the Envroinment Variable.**
.
.
<br>
**Some changes in the script you have to make**
<br>
Again Paste Tesseract Folder Path At This Line 
<br>
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\iam_kazi\AppData\Local\Tesseract-OCR\tesseract.exe'
.
.
<br>
Provide Your Image Folder Path For Source (**It will iterate all images at onces, Do not provide image name**)
listfiles = os.listdir("C:\Data")
.
.
<br>
Again paste same path to open image 
<br>
img=Image.open("C:\\Data\\"+x) **make sure give double backlashes**
.
.
<br>
In My Script, Basically it adds br tag after every line.
<br>
You can make changes as per your need
.
.
.
<br>
Thank You! Enjoy!

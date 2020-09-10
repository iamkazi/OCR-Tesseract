import pytesseract
from PIL import Image
import os
#download tesseract from  https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\iam_kazi\AppData\Local\Tesseract-OCR\tesseract.exe'

listfiles = os.listdir("C:\Data")
for x in listfiles:
        img=Image.open("C:\\Data\\"+x)
        img = img.convert ('L')
        text=pytesseract.image_to_string(img) 

        li = text.split('\n')
        for y in range(len(li)):
                if("\n" in li[y]):
                        li[y]=li[y].strip("\n")
                elif("\x0c" in li[y]):
                        li[y]=li[y].strip("\x0c")
                elif("''" in li[y]):
                        li[y]=li[y].strip("''")    
                elif(" " in li[y] or "  "):
                        li[y]=li[y].strip()     
                else:
                    pass

        li = list(filter(('').__ne__,li))
        
        with open (x[:-4]+'.html','w') as file:
                file.write("""<!DOCTYPE html>
        <html>
        <head>
                <title></title>
        </head>
        <body>
        """)
                if(li): 
                        for y in li:
                                file.write(y+"<br>")
                file.write("""</body>
        </html>""")

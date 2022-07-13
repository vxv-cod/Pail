import numpy
# from numpy import array
from PIL import Image
import png
# convertFromimage
print('-------------------------------')
def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r') #Opens the file in read-mode
    text = file.read() #Reads the file and assigns the value to a variable
    file.close() #Closes the file (read session)
    file = open(fileName, 'w') #Opens the file again, this time in write-mode
    file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
    # and writes the whole output when done, wiping over the old contents of the file
    file.close() #Closes the file (write session)

img = Image.open("Yad_vxv.png").convert("L")
imgarr = numpy.array(img)
hhh = list(imgarr)
handle = open("Time_fail.txt", "w")
handle.write(str(hhh))
handle.close()
ReplaceLineInFile('Time_fail.txt', ', dtype=uint8), array', '), ')
ReplaceLineInFile('Time_fail.txt', '[array', '')
ReplaceLineInFile('Time_fail.txt', ', dtype=uint8)]', ')')
text = open('Time_fail.txt', 'r').read()

handle = open("Цифря.py", "w")
handle.write('from numpy import array\nimport png\na = ')
handle.write(text +'\n')
handle.write('fff = png.from_array(a, mode="L")\nfff.save("Code_image.png")')
handle.close()
print('-------------------------------')


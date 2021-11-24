#TODO: Make the file size normal and proportions
#TODO: Make the final element a comment. 


import csv

file_CSV = open("placeSpreadsheetHereAsCSVFile/testClass.csv")
data_CSV = csv.reader(file_CSV)
list_CSV = list(data_CSV)

import PIL
from PIL import Image, ImageDraw, ImageFont
newLine = 15
gap = 40
spacing = 0
rectColor = "gray"
y = 1000
listCount = 1
#studentCount = 1

studentTotal = len(list_CSV)

for studentCount in range(2, studentTotal):
   
   listCount = 1
   #y = 100
   y = 250
   spacing = 0
   H1Font = ImageFont.truetype('FreeMono.ttf', 40)
   H2Font = ImageFont.truetype('FreeMono.ttf', 30)
   H3Font = ImageFont.truetype('FreeMono.ttf', 20)
   
   img = Image.new('RGB', (900, 700), color = 'gray')
   d = ImageDraw.Draw(img)
   d.text((10,10), "Progress Report For " + list_CSV[studentCount][0], font=H1Font, fill=(255,255,0))
   d.text((10,50), list_CSV[0][0] + " class", font=H2Font, fill=(255,255,0))
   d.text((10,80), "Week of " + list_CSV[0][1] + " to " + list_CSV[0][2], font=H2Font, fill=(255,255,0))

   #d.rectangle((0, 0, 20, 20), fill=("green"), outline=("black"))
   for columnName in list_CSV[1][1:]:
      #TODO: dynamically find the y spacing 
      d.text((spacing, y), columnName, font=H3Font, fill=("black"))
      #TODO: update this spacing wiht some dynamic thing so I can add an arbitrary amount

      spacing += 200
      listCount += 1
      if (listCount == 3):
          y = 450
          spacing = 0

   spacing = 0
   #y = 150

   listCount = 1
   #y = 150
   #y = 500
   #spacing = 0
   y = 250
   spacing = 0

   
   #create text and boxes
   d.text((10, 120), "Meeting Expectations", font=H3Font, fill="black")
   d.text((310, 120), "Needs Adjustment", font=H3Font, fill="black")
   d.text((580, 120), "Needs Improvement", font=H3Font, fill="black")

   #d.rectangle([(20, 150), (220, 220)], fill=("green"), outline=("black"))
   d.rectangle([(90, 150), (140, 190)], fill=("green"), outline=("black"))
   d.rectangle([(380, 150), (430, 200)], fill=("yellow"), outline=("black"))
   d.rectangle([(650, 150), (700, 200)], fill=("red"), outline=("black"))


   
   for progressRow in list_CSV[studentCount][1:]:
       #ONCE IT WORKS THE FIRST TIMEfor progressElem in progressRow:
       for progressElem in progressRow:
           if progressElem == '3':
               rectColor = "green"
           if progressElem == '2':
               rectColor = "yellow"
           if progressElem == '1':
               rectColor = "red"
           d.rectangle([(spacing, y+50), (spacing+50, y+100)], fill=(rectColor), outline=("black"))
           listCount = listCount + 1
           spacing += 200
           if (listCount == 3):
               y = 470
               spacing = 0

   img.save('studentReportsWillPopulateHere' + '/' + str(studentCount - 1) + ' progressReport ' + list_CSV[studentCount][0] +  '.png')

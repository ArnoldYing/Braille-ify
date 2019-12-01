from tkinter import *
from lxml import html
import requests
import braille
import time

#run this method with array to produce output in braille
def notEmpty(array):
    countEmpty = 0
    for r in range(3):
        for c in range(2):
            if array[r][c] == 0:
                countEmpty += 1
    return countEmpty != 6

def convertAndRun(thisArray, c):
    class sixDot:
        def __init__(self, window, xcor, ycor, array):
            size = 6 #size of button
            on = "red"  #on color
            off = "black" #off color
            empty = "white"
            shift = 40
            countEmpty = 0
            for r in range(3):
                for c in range(2):
                    if array[r][c] == 0:
                        countEmpty+=1
            if countEmpty == 6:
                for r in range(3):
                    for c in range(2):
                        b = Button(window, text="demo", fg=empty, bg=empty, relief=RIDGE, font=("arial", size, "bold"))
                        b.place(x=xcor + (c - 1) * shift, y=ycor + (r - 1) * shift)
            else:
                for r in range(3):
                    for c in range(2):
                        if array[r][c] == 1:
                            b = Button(window, text="demo", fg=on, bg=on, relief=RIDGE, font=("arial", size, "bold"))
                        else:
                            b = Button(window, text="demo", fg=off, bg=off, relief=RIDGE, font=("arial", size, "bold"))
                        b.place(x=xcor + (c - 1) * shift, y=ycor + (r - 1) * shift)

    window = Tk()
    window.geometry("2600x300")
    window.title("Text to Braille")

    for i in range(len(thisArray)):
        gap = 100
        if notEmpty(thisArray[i]):
            sixDot(window, 50 + gap * i, 100, thisArray[i])
            char = c[i]
            text = Button(window, text=char, fg='white', bg='black', relief=RIDGE, font=("arial", 19, "bold"))
            text.place(x=25+gap*i, y=240)

    Button(window, text="Quit", command=quit).pack()
    window.mainloop()



page = requests.get('http://en.wikipedia.org/wiki/Fortnite')
tree = html.fromstring(page.content)
tableOfContent = tree.xpath('//*[@id="toc"]/ul/li/a/span[@class="toctext"]/text()')
subTitles = tree.xpath('//h2/span[@class="mw-headline"]/text()')
content = tree.xpath('//div[@class="mw-parser-output"]/p/text() | //div[@class="mw-parser-output"]/p/*/text() |'
                     ' //div[@class="mw-parser-output"]/p/*/*/text()')
for c in content:
    arr = braille.textToAsciiBraille(c)
    convertAndRun(arr, c)

from tkinter import *
from lxml import html
import requests
import braille
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions, MetadataOptions, ConceptsOptions
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import time

# Authentication via IAM
authenticator = IAMAuthenticator('fvqo2-7Ubmnf5rmImg7ycQkj3IW9Op2J3bQtsCmqLqf_')
service = NaturalLanguageUnderstandingV1(
      version='2018-03-16',
      authenticator=authenticator)
service.set_service_url('https://gateway.watsonplatform.net/natural-language-understanding/api')


def notEmpty(array):
    countEmpty = 0
    for r in range(3):
        for c in range(2):
            if array[r][c] == 0:
                countEmpty += 1
    return countEmpty != 6


# run this method with array to produce output in braille
def convertAndRun(thisArray, c):
    class sixDot:
        def __init__(self, window, xcor, ycor, array):
            size = 6 #size of button
            on = "red"  #on color
            off = "black" #off color
            shift = 40

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
            text = Button(window, text=char, fg='white', bg='black', relief=RIDGE, font=("arial", 16, "bold"))
            text.place(x=25+gap*i, y=240)
    
    Button(window, text="Quit", command=quit).pack()
    window.mainloop()


response = service.analyze(
    url='https://en.wikipedia.org/wiki/Fortnite',
    features=Features(metadata=MetadataOptions()),
    return_analyzed_text=True).get_result()

print(response['analyzed_text'])

strArr = response['analyzed_text'].split()

for c in strArr:
    arr = braille.textToAsciiBraille(c)
    convertAndRun(arr, c)

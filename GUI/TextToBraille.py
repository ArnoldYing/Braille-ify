from tkinter import *

def convertAndRun(array):
    class sixDot:
        def __init__(self, window, xcor, ycor, array):
            size = 6 #size of button
            on = "red"  #on color
            off = "black" #off color

            for r in range(3):
                for c in range(2):
                    if array[r][c] == 1:
                        b = Button(window, text="demo", fg=on, bg=on, relief=RIDGE, font=("arial", size, "bold"))
                    else:
                        b = Button(window, text="demo", fg=off, bg=off, relief=RIDGE, font=("arial", size, "bold"))
                    shift = 40
                    b.place(x=xcor + (c - 1) * shift, y=ycor + (r - 1) * shift)

    window = Tk()
    window.geometry("2600x300")
    window.title("Text to Braille")

    for i in range(len(array)):
        gap = 150
        sixDot(window, 50 + gap * i, 100, array[i])

    window.mainloop()

array = [[[1, 1], [1, 0], [1, 0]], [[1, 1], [1, 0], [1, 0]], [[1, 1], [1, 0], [0, 0]], [[1, 1], [1, 0], [1, 0]]]
convertAndRun(array)

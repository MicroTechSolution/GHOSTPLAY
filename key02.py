import numpy as np
from cv2 import *
from PIL import ImageGrab
from tkinter import *

from tkinter import messagebox


signal = 1

def startThings():
    while signal == 1:

        img = ImageGrab.grab()
        img_gp = np.array(img)
        frame = cvtColor(img_gp, COLOR_BGR2GRAY)
        imshow('img', frame)
        if waitKey(1) & 0XFF == ord('q'):
            break

    img.release()
    destroyAllWindows()

top = Tk()



top.mainloop()

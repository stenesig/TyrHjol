import tkinter as tk
from PIL import ImageTk
from PIL import Image
import random
from time import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
flag = True

NUMBER_OF_RESULTS = 14
WHEEL_PATH = "images/hjolv2.png"


class SimpleApp(object):
    def __init__(self, master, filename, **kwargs):
        self.master = master
        self._geom = "200x200+0+0"
        pad = 3
        master.geometry(
            "{0}x{1}+0+0".format(
                master.winfo_screenwidth() - pad, master.winfo_screenheight() - pad
            )
        )
        master.bind("<Escape>", self.toggle_geom)
        self.filename = filename
        self.canvas = tk.Canvas(master, width=1000, height=1000)
        self.canvas.pack()

        self.update = self.draw().__next__
        master.after(1, self.update)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

    def draw(self):
        image = Image.open(self.filename)
        image_bar = Image.open("images/blackbar.png").convert("RGBA")
        image = image.resize((800, 800), Image.ANTIALIAS)
        image_bar = image_bar.resize((100, 20), Image.ANTIALIAS)
        angle = random.randint(0, 360)
        diff = random.randint(20, 40)
        diff_time = time()
        while True:
            if diff <= 0:
                diff = 0
                lst = [
                    360 * (x / NUMBER_OF_RESULTS) for x in range(0, NUMBER_OF_RESULTS)
                ]
                angle = lst[min(range(len(lst)), key=lambda i: abs(lst[i] - angle))]
            tobediplayed = image.rotate(angle)
            tobediplayed.paste(image_bar, (750, 390), image_bar)
            tkimage = ImageTk.PhotoImage(tobediplayed)
            canvas_obj = self.canvas.create_image(500, 500, image=tkimage)

            self.master.after_idle(self.update)
            yield
            self.canvas.delete(canvas_obj)
            angle -= diff
            angle %= 360
            if time() - diff_time > 0.5:
                diff -= 2
                diff_time = time()
            if GPIO.input(10) == GPIO.HIGH and flag == True:
                angle = random.randint(0, 360)
                diff = random.randint(20, 40)
                diff_time = time()
                flag = False

            if GPIO.input(10) != GPIO.HIGH:
                flag = True                


root = tk.Tk()
app = SimpleApp(root, WHEEL_PATH)
root.mainloop()

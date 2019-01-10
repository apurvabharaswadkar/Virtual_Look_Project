from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import askcolor
from PIL import Image, ImageTk
from tkinter import filedialog
import os
import numpy as np
import cv2 as cv
from tkinter import messagebox


def AspectRatio(w, h, fixed_w, fixed_h):
    # Aspect Ratio adjustment
    ratio = w/h
    if (w > fixed_w or h > fixed_h):
        diff_w = abs(fixed_w - w)
        diff_h = abs(fixed_h - h)
    else:
        diff_w = 0
        diff_h = 0
    print(diff_w)
    print(diff_h)

    new_h = (h - diff_h)
    new_w = int(ratio*new_h)

    if(new_w > fixed_w):
        new_h = int(fixed_w/ratio)
    new_w = fixed_w
    return new_w, new_h

class HCI_GUI(object):


    def __init__(self):

        self.root = Tk()
        self.root.title("Virtual Fit")
        self.root.geometry('1000x1000')
        self.root.configure(background='white')
        self.root.propagate(0)

        # Create Canvas
        self.c1 = Canvas(self.root, bg='white', width=900, height=900, bd=0, highlightthickness=0)
        self.c1.place(x=20, y=20, anchor='center')

        # Create Title
        self.img = Image.open('yo.jpg')

        # self.img = self.img.resize((new_w, new_h), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.img = ImageTk.PhotoImage(self.img)

        self.title = Label(self.root, height=120, width=700, image=self.img, anchor='center',
                           bg='white')
        self.title.image = self.img
        self.title.place(x=50, y=20)

        # Label for Place holder - Person
        self.im = Image.open('download12.png')
        self.im = self.im.resize((400, 400), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.im = ImageTk.PhotoImage(self.im)

        self.l = Label(self.root, height=600, width=600, image=self.im, anchor='center', bg='white')

        self.l.image = self.im
        self.l.place(x=20, y=130)

        # Label for Place holder - hats
        self.im1 = Image.open('Cart.png')
        self.im1 = self.im1.resize((200, 200), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.im1 = ImageTk.PhotoImage(self.im1)

        self.l1 = Label(self.root, height=200, width=200, image=self.im1, anchor='center', bg='white')

        self.l1.image = self.im1
        self.l1.place(x=700, y=350)

        # Create Add button
        self.pic3 = Image.open('Add.png')
        self.pic3 = self.pic3.resize((60, 60), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.pic3 = ImageTk.PhotoImage(self.pic3)

        self.Add_button = Button(self.root, command=self.add_func, font=("MS Serif Bold", 15),
                                    fg='brown', bg='white', height=60, image=self.pic3, text='Add',
                                    compound=LEFT, padx=10)
        self.Add_button.place(x=750, y=600)


        self.pic1 = Image.open('go.jpg')
        self.pic1 = self.pic1.resize((60, 60), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.pic1 = ImageTk.PhotoImage(self.pic1)

        # Create Browse button
        self.pic = Image.open('search_b.jpg')
        self.pic = self.pic.resize((60, 60), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.pic = ImageTk.PhotoImage(self.pic)

        self.browse_button = Button(self.root, command=self.browse_func, font=("MS Serif Bold", 15),
                                    fg='brown', bg='white', height=60, image=self.pic, text='Browse',
                                    compound=LEFT, padx=10)
        self.browse_button.place(x=250, y=750)

        self.pic1 = Image.open('go.jpg')
        self.pic1 = self.pic1.resize((60, 60), Image.ANTIALIAS)  # The (60, 60) is (height, width)
        self.pic1 = ImageTk.PhotoImage(self.pic1)




        # Check button
        self.check_button = Button(self.root, command=self.Check_Look, font=("MS Serif Bold", 15),
                                    fg='brown', bg='white', height=60, image=self.pic1, text='Go',
                                    compound=LEFT, padx=10)
        self.check_button.place(x=750, y=700)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.fname = None
        self.fname1 = None
        self.img = None
        self.tmpimg = None
        self.tmpimg1 = None
        # self.pic = None
        # self.pic1 =None

    def add_func(self):
        self.fname1 = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                               filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"),
                                                          ("gif files", "*.gif"), ("jpeg files1", "*.jpeg")))

        if (self.fname1):

            self.tmpimg1 = Image.open(self.fname1)
            tmp_im_w1, tmp_im_h1 = self.tmpimg1.size

            print(tmp_im_w1)
            print(tmp_im_h1)
            # Aspect ratio
            new_tmpim_w1, new_tmpim_h1 = AspectRatio(tmp_im_w1, tmp_im_h1, 200, 200)
            print(new_tmpim_w1)
            print(new_tmpim_h1)
            self.tmpimg1 = self.tmpimg1.resize((new_tmpim_w1, new_tmpim_h1),
                                             Image.ANTIALIAS)  # The (60, 60) is (height, width)
            self.tmpimg1 = ImageTk.PhotoImage(self.tmpimg1)

            self.l1.configure(image=self.tmpimg1)

        else:
            pass

    def browse_func(self):

        self.fname = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select file",
                                                filetypes=(("jpeg files", "*.jpg"), ("png files", "*.png"),
                                                           ("gif files", "*.gif"), ("jpeg files1", "*.jpeg")))

        if (self.fname):

            self.tmpimg = Image.open(self.fname)
            tmp_im_w, tmp_im_h = self.tmpimg.size


            # Aspect ratio
            new_tmpim_w, new_tmpim_h = AspectRatio(tmp_im_w, tmp_im_h, 600, 600)
            print(new_tmpim_w)
            print(new_tmpim_h)
            self.tmpimg = self.tmpimg.resize((new_tmpim_w, new_tmpim_h), Image.ANTIALIAS)  # The (60, 60) is (height, width)
            self.tmpimg = ImageTk.PhotoImage(self.tmpimg)

            self.l.configure(image = self.tmpimg)

        else:
            pass

    def Check_Look(self):

        # Get the face coordinates
        face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
        image1 = cv.imread(self.fname)
        gray = cv.cvtColor(image1, cv.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in faces:
            cv.rectangle(image1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Calculate face_width, face_height and center
        face_width = (x + w - x)
        face_height = y + h - y
        face_center_x = int((x + x + w) / 2)
        face_center_y = int((y + y + h) / 2)

        # Make Hat image transparent
        img = Image.open(self.fname1)
        name_png = self.fname +".png"
        img = img.save(name_png)
        img = Image.open(name_png)
        # img = Image.open('hat_blck.png')
        # img = img.save('images1p.png')
        # img = Image.open('images1p.png')
        img = img.convert("RGBA")
        datas = img.getdata()

        # Make the image transparent
        newData = []
        for item in datas:
            if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
            else:
                newData.append(item)

        img.putdata(newData)
        img.save("test5.png", "PNG")

        # Load the girl image using Pillow
        img3 = Image.open(self.fname)
        w_img3, h_img3 = img3.size

        # Resize the hat transparent image using pillow
        img = Image.open('test5.png')

        # TODO: Resize the hat images according to aspect ratio
        # TODO: Remove the gap between hat and head if possible
        img = img.resize((face_width, int(0.6 * face_height)), Image.ANTIALIAS)

        shift_x = int((w_img3 - face_width) / 2)

        img4 = Image.new("RGB", (512, 512), "white")
        # Paste the transparent image on the hat image
        img4.paste(img, (shift_x, 0), img)
        # Paste the girls image on new image
        img4.paste(img3, (0, int(0.6 * face_height)), img3)
        img4_width,img4_height=img4.size

        # Aspect Ratio adjustment
        if(img4_width>600 or img4_height >600):
            diff_w = abs(600-img4_width)
            diff_h = abs(600-img4_height)
        else:
            diff_w =0
            diff_h =0

        new_img4_w = img4_width-diff_w
        new_img4_h = img4_width-diff_h

        img4 = img4.resize((new_img4_w, new_img4_h), Image.ANTIALIAS)
        img4.save("final.png", "PNG")
        self.pic2= Image.open('final.png')
        self.pic2 = ImageTk.PhotoImage(self.pic2)

        # img4.show()
        self.l.configure(image = self.pic2)

if __name__ == '__main__':
    ge = HCI_GUI()
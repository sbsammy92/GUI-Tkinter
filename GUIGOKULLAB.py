import tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as tmsg
import customtkinter
import csv

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

root = customtkinter.CTk()

root.title("Gokul Lab GUI")
root.geometry("1800x1200")

root['background'] = "white"


def getvals():
    print("Submitting form")
    header = ['Ash','VM','C','H','S','N','Rp','Rw','Vitrinite','Liptinite','Basicity Index','Output']
    data = [myslider1.get(), myslider2.get(), myslider3.get(), myslider4.get(), myslider5.get(), myslider6.get(),
            slider1.get(), slider2.get(), slider3.get(), slider4.get(), slider5.get(), w.get()]

    with open('records.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        # write the data
        writer.writerow(header)
        writer.writerow(data)
    # with open("records.txt", "w") as f:
    #     f.write(f"{myslider1.get(),myslider2.get(),myslider3.get(),myslider4.get(),myslider5.get(),myslider6.get(),slider1.get(),slider2.get(),slider3.get(),slider4.get(),slider5.get(),w.get()}\n ")


def myfunc():
    pass


def help():
    a = tmsg.showinfo("Help", "Developed by Samyak, Gokul Lab(IITH)")


def rate():
    value = tmsg.askquestion("Review", "Was your Experience Good?")
    if value == "yes":
        msg = "Great. Shower us with more money!!"
    else:
        msg = "Tell us what went wrong. We will Try to resolve the issue."

    tmsg.showinfo("Experience", msg)


mainmenu = Menu(root)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="New Project", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
mainmenu.add_cascade(label="File", menu=m1)
# mymenu.add_command(label="Exit", command=exit)


m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_separator()
m2.add_command(label="Paste", command=myfunc)
m2.add_command(label="Find", command=myfunc)
mainmenu.add_cascade(label="Edit", menu=m2)
root.config(menu=mainmenu)

m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=rate)
mainmenu.add_cascade(label="Help", menu=m3)

f0 = customtkinter.CTkFrame(root)
Label(f0, text="Model-1", font="Roboto 40").pack()
f0.pack()

canvas = Canvas(root, width=1800, height=30, bg="white")
canvas.create_line(0, 25, 1800, 25, width=10, fill='powder blue')
canvas.pack()

labelframe = LabelFrame(root, text="Inputs", relief="raised", font="Gothic 15 bold")
labelframe.pack(side=tkinter.LEFT)
f3 = Frame(labelframe, padx=20)
myslider1 = Scale(f3, label="Ash:", from_=3.3, to=12.91, resolution=0.1, orient="horizontal", length=500,
                  troughcolor="powder blue", sliderlength=20, tickinterval=(12.91 - 3.3), font="Roboto 10")
myslider1.pack()
myslider2 = Scale(f3, label="VM:", from_=15.875, to=39.6, resolution=0.01, orient="horizontal", length=500,
                  troughcolor="powder blue", tickinterval=(39.6 - 15.875), font="Roboto 10")
myslider2.pack()
myslider3 = Scale(f3, label="C:", from_=77.13, to=92.12, resolution=0.01, orient="horizontal", length=500,
                  troughcolor="powder blue", tickinterval=(92.12 - 77.13), font="Roboto 10")
myslider3.pack()
myslider4 = Scale(f3, label="H:", from_=3.91, to=6.12, resolution=0.01, orient="horizontal", length=500,
                  troughcolor="powder blue", tickinterval=(6.12 - 3.91), font="Roboto 10")
myslider4.pack()
myslider5 = Scale(f3, label="N:", from_=0.89, to=2.86, resolution=0.01, orient="horizontal", length=500,
                  troughcolor="powder blue", tickinterval=(2.86 - 0.89), font="Roboto 10")
myslider5.pack()
myslider6 = Scale(f3, label="S:", from_=0.23, to=2.75, resolution=0.01, orient="horizontal", length=500,
                  troughcolor="powder blue", tickinterval=(2.75 - 0.23), font="Roboto 10")
myslider6.pack()
variable = StringVar(f3)
variable.set("Choose Output")  # default value

w = customtkinter.CTkComboBox(f3, values=["CSN", "IST", "ST", "Max Contraction", "Max Fluidity", "Max Dilation"],
                              variable=variable, button_color="powder blue")
w.pack(pady=20)
f3.pack(anchor="nw", side=tkinter.LEFT)
# f5 = Frame(labelframe,pady=260)
# button = customtkinter.CTkButton(master=f5,width=120,
#                                  height=62,
#                                  border_width=0,
#                                  corner_radius=8,
#                                  text="RUN",text_font="Comicsans", fg_color="grey")
# button.pack(padx=20, pady=10)
# f5.pack(anchor="ne", side=tkinter.RIGHT)


f4 = Frame(labelframe, padx=10)
slider1 = Scale(f4, label="Rp:", from_=0.58, to=5.8, resolution=0.01, orient="horizontal", length=500,
                troughcolor="powder blue", tickinterval=(5.8 - 0.58), font="Roboto 10")
slider1.pack()
slider2 = Scale(f4, label="Rw:", from_=0.008, to=4.81, resolution=0.01, orient="horizontal", length=500,
                troughcolor="powder blue", tickinterval=(4.81 - 0.008), font="Roboto 10")
slider2.pack()
slider3 = Scale(f4, label="Vitrinite:", from_=33, to=99, resolution=0.01, orient="horizontal", length=500,
                troughcolor="powder blue", tickinterval=(99 - 33), font="Roboto 10")
slider3.pack()
slider4 = Scale(f4, label="Liptinite:", from_=5.5, to=9, resolution=0.01, orient="horizontal", length=500,
                troughcolor="powder blue", tickinterval=(9 - 5.5), font="Roboto 10")
slider4.pack()
slider5 = Scale(f4, label="BI:", from_=0.03, to=0.56, resolution=0.01, orient="horizontal", length=500,
                troughcolor="powder blue", tickinterval=(0.56 - 0.03), font="Roboto 10")
slider5.pack()
button = customtkinter.CTkButton(master=f4, width=120,
                                 height=62,
                                 border_width=0,
                                 corner_radius=8,
                                 text="Run", text_font="Roboto 15", fg_color="powder blue", text_color="black", command=getvals)
button.pack(padx=20, pady=70)
f4.pack(anchor="ne", side=tkinter.RIGHT)

labelframe1 = LabelFrame(root, text="Outputs", relief="raised", font="Gothic 15 bold")
labelframe1.pack(side=tkinter.RIGHT)
img = Image.open("2.png")
photo = ImageTk.PhotoImage(img)
mylabel2 = Label(labelframe1, image=photo)
mylabel2.pack()
f6 = Frame(labelframe1, padx=300)
button2 = customtkinter.CTkButton(master=f6, width=120,
                                  height=62,
                                  border_width=0,
                                  corner_radius=8,
                                  text="Generate \nOutput", fg_color="powder blue", text_font="Roboto 15", text_color="black")
button2.pack(padx=20, pady=10)
f6.pack()
root.mainloop()

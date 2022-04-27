import tkinter
from tkinter.filedialog import asksaveasfile, askopenfile
from tkinter.messagebox import showerror

FILE_NAME = tkinter.NONE


def new_file():
    global FILE_NAME
    FILE_NAME = "Untitled"
    text.delete('1.0', tkinter.END)


def save_file():
    data = text.get('1.0', tkinter.END)
    out = open(FILE_NAME, 'w')
    out.write(data)
    out.close()


def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', tkinter.END)
    try:
        out.write(data.rstrip())
    except Exception:
        showerror(title="Oops!", message="Unable to save file....")


def open_file():
    global FILE_NAME
    inp = askopenfile(mode="r")
    if inp is None:
        return
    FILE_NAME = inp.name
    data = inp.read()
    text.delete('1.0', tkinter.END)
    text.insert('1.0', data)

def chenge_fonts(foont):
        text["font"]=fonts[foont]["font"]


root = tkinter.Tk()
root.title("JPad v0.1b")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)

text = tkinter.Text(root, width=400, height=400)
text.pack()

menuBar = tkinter.Menu(root)
fileMenu = tkinter.Menu(menuBar, tearoff=0)
fileMenu.add_command(label="New", command=new_file)
fileMenu.add_command(label="Open", command=open_file)
fileMenu.add_command(label="Save", command=save_file)
fileMenu.add_command(label="Save As", command=save_as)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

font_menu = tkinter.Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Font", menu=font_menu)
font_menu.add_command(label="Arial", command=lambda:chenge_fonts("Arial"))
font_menu.add_command(label="Times New Roman", command=lambda:chenge_fonts("TNR"))

fonts = {
    "Arial":{
        "font": "Arial"
    },
    "TNR":{
        "font":("Times New Roman", 14, "bold")
    }
}


root.config(menu=menuBar)
root.mainloop()

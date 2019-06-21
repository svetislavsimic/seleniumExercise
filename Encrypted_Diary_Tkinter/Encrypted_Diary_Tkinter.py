import tkinter as tk
import tkinter.scrolledtext as tkst
import tkinter.font as tkFont
from tkinter import messagebox
from tkinter import filedialog
import os
from cryptography.fernet import Fernet
import sys
class PassCheck:
    def __init__(self):
        self.win = tk.Tk()
        self.passvar = tk.StringVar()
        self.password = "123456789"
        self.tb = tk.Entry(master=self.win, textvariable=self.passvar)
        self.tb.pack()
        self.verifybutton = tk.Button(master=self.win, command=self.passverify, text="OK")
        self.verifybutton.pack()
        self.tb.focus_set()
        self.win.mainloop()

    def passverify(self):
        self.password_query = str(self.passvar.get())
        print(self.password_query)
        if self.password != self.password_query:
            sys.exit()
        else:
            self.win.destroy()

class App:
    def __init__(self, filename=None):
        self.win = tk.Tk()

        self.key = b'F8z-KuTE1YqpwSp412SMMJuZPHaTH60d_8HYG4eKMpo='
        self.arb = Fernet(self.key)
        self.win.protocol("WM_DELETE_WINDOW", self.Exit)
        self.customFont = tkFont.Font(
            family="Comic Sans MS", size=14
        )
        self.filename = filename

        frame1 = tk.Frame(
            master=self.win,
             background = 'green'
        )
        frame1.pack(fill='both', expand='yes')
        self.editArea = tkst.ScrolledText(
            master=frame1,
            wrap=tk.WORD,
            font=self.customFont,
        )
        self.editArea.pack(padx=3, pady=3, fill=tk.BOTH, expand=True)
        self.editArea.focus_set()

        menubar = tk.Menu(self.win)
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.Open)
        filemenu.add_command(label="Save", command=self.Save)

        filemenu.add_command(label="Rename", command=self.Rename)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Exit)
        menubar.add_cascade(label="File",  menu=filemenu)
        fontMenu=tk.Menu(menubar, tearoff=1)
        fontMenu.add_command(label="IncreaseFont", command=self.IncreaseFont)
        fontMenu.add_command(label="DecreaseFont", command=self.DecreaseFont)
        menubar.add_cascade(label="Font", menu=fontMenu)
        searchMenu= tk.Menu(menubar, tearoff= 0)
        searchMenu.add_command(label="Find", command = self.search())
        menubar.add_cascade(label="Search", menu=searchMenu )
        self.win.config(menu=menubar)
        try:
            self.win.iconbitmap("icon.png")
        except:
            pass
        self.win.mainloop()

    def IncreaseFont(self):
        size = self.customFont['size']
        self.customFont.configure(size=size + 2)

    def DecreaseFont(self):
        size = self.customFont['size']
        if size-2>0:
            self.customFont.configure(size=size - 2)


    def Open(self):
        cwd = os.getcwd()
        if tk.messagebox.askyesno("Is your file encrypted", "Is your file encrypted?"):
            self.filename = filedialog.askopenfilename(initialdir=cwd, title="Select file",
                                                       filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            print(self.filename)
            if not self.filename:
                return
            with open(self.filename, mode='r') as f:
                data = f.read()
                datatoken = bytes(data, 'utf-8')
                self.editArea.insert('1.0', (self.arb.decrypt(datatoken).decode('utf-8')))
        else:
            self.filename = filedialog.askopenfilename(initialdir=cwd, title="Select file",
                                           filetypes=(("txt files", "*.txt"), ("all files", "*.*")))
            print(self.filename)
            if not self.filename:
                return
            with open(self.filename,mode='r') as f:
                self.editArea.insert('1.0', f.read())

    def Save(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:  # asksaveasfile return `None` if dialog closed with "cancel".
            return
        print(f)
        print(type(f))
        with f:
            text2save = str(self.editArea.get(1.0, "end"))  # starts from `1.0`, not `0.0`
            token = self.arb.encrypt(bytes(text2save, 'utf-8'))
            f.write(token.decode('utf-8'))

    def Exit(self):
        if tk.messagebox.askokcancel("Exit", "Are you sure?"):
            self.win.destroy()
    def Rename(self):
        pass
    def search(self):
        pass


PassCheck()
App()

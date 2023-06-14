import tkinter.ttk
import tkinter.messagebox
import Rickroll


class Page(tkinter.Frame):
    def __init__(self, root):
        super().__init__()
        self.root = root
        tkinter.ttk.Label(self, text="You totally won't get rickrolled if you press the button.").pack()
        tkinter.ttk.Label(self, text="The button below is definitely not suspicious.").pack()
        tkinter.ttk.Button(self, text="Not a Rickroll", takefocus=False, command=self.ask).pack()
        self.pack()

    def ask(self):
        if tkinter.messagebox.askyesno("Question", "Do you want to not get rickrolled?\nYou can definitely click 'Yes'."):
            self.pack_forget()
            Rickroll.Rickroll(self.root)

import tkinter
import tkinter.ttk
import Lyrics


class Window(tkinter.Toplevel):
    def __init__(self, button):
        super().__init__()
        self.button = button
        self.protocol("WM_DELETE_WINDOW", self.close)
        self.resolution = [400, 355]
        self.button.config(state="disabled")
        self.title("Lyrics")
        self.geometry("{}x{}".format(*self.resolution))
        self.minsize(*self.resolution)
        scroll = tkinter.ttk.Scrollbar(self)
        scroll.pack(side="right", fill="y")
        content = tkinter.Text(self, yscrollcommand=scroll.set)
        content.pack(expand=True, fill="both")
        scroll.config(command=content.yview)
        content.insert("end", "".join(Lyrics.lyrics))
        content.config(state="disabled")
        self.attributes("-topmost", True)
        self.lift()
        self.focus()

    def close(self):
        self.destroy()
        self.button.config(state="normal")

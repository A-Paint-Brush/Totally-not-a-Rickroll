import tkinter
import Home_Page


class GUI(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resolution = [600, 400]
        self.geometry("{}x{}".format(*self.resolution))
        self.minsize(*self.resolution)
        self.title("Totally not a Rickroll")
        Home_Page.Page(self)
        self.mainloop()


if __name__ == "__main__":
    GUI()

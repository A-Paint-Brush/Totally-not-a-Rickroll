import tkinter
import tkinter.ttk
import tkinter.font
import tkinter.messagebox
import pygame.mixer
import Lyrics_Window
import Path
import Video
import Timer
pygame.mixer.init()
pygame.mixer.music.load(Path.resource_path(".\\Sound\\Rickroll.wav"))
find_length = pygame.mixer.Sound(Path.resource_path(".\\Sound\\Rickroll.wav")).get_length()


class Rickroll(tkinter.Frame):
    def __init__(self, root):
        super().__init__()
        self.video_parser = Video.Video(Path.resource_path(".\\Video\\Rickroll.mp4"), find_length * 1000)
        self.root = root
        self.countdown = 120
        self.rickroll_timer = Timer.Timer()
        self.image = tkinter.Canvas(self)
        self.image.pack(expand=True, fill="both")
        font = tkinter.font.Font(family="Segoe UI", size=14)
        tkinter.ttk.Label(self, text="You've been rickrolled!", font=font).pack()
        self.show_lyrics = tkinter.ttk.Button(self, text="Show Lyrics", takefocus=False, command=self.lyrics)
        self.show_lyrics.pack()
        self.closable = False
        self.root.protocol("WM_DELETE_WINDOW", self.no_escape)
        self.next_frame_id = None
        self.next_tick_id = None
        self.minimise_id = None
        self.root.attributes("-topmost", True)
        self.pack(expand=True, fill="both")
        self.root.update_idletasks()
        self.rickroll_timer.reset()
        self.check_time()
        self.no_minimise()
        self.start_non_rickroll()

    def no_minimise(self):
        if self.root.state() == "iconic":
            self.root.deiconify()
        self.minimise_id = self.root.after(100, self.no_minimise)

    def start_non_rickroll(self):
        self.rickroll_timer.reset()
        pygame.mixer.music.play()
        self.get_next()
        self.tick()

    def lyrics(self):
        Lyrics_Window.Window(self.show_lyrics)

    def get_next(self):
        self.video_parser.tick(pygame.mixer.music.get_pos())
        self.next_frame_id = self.root.after(5, self.get_next)

    def tick(self):
        if not pygame.mixer.music.get_busy():
            self.video_parser.reset()
            pygame.mixer.music.play()
        size = [self.image.winfo_width(), self.image.winfo_height()]
        frame = self.video_parser.get_frame(*size)
        self.image.delete("all")
        self.image.create_image(size[0] / 2 - frame.width() / 2, size[1] / 2 - frame.height() / 2, image=frame,
                                anchor="nw")
        self.next_tick_id = self.root.after(5, self.tick)

    def check_time(self):
        if self.rickroll_timer.get_time() >= self.countdown:
            self.closable = True
            tkinter.messagebox.showinfo("Info", "You can close the window now :)")
        else:
            self.root.after(250, self.check_time)

    def no_escape(self):
        if self.closable:
            self.root.after_cancel(self.minimise_id)
            self.root.after_cancel(self.next_frame_id)
            self.root.after_cancel(self.next_tick_id)
            self.video_parser.close()
            pygame.mixer.music.stop()
            self.root.destroy()
        else:
            tkinter.messagebox.showerror("There's no escape!", "Did you really think you can escape this rickroll so "
                                                               "easily?\nYou have to watch this rickroll for 2 minutes "
                                                               "before you can close this program. >:)")

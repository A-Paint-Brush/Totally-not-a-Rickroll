import PIL.ImageTk
import PIL.Image


class Image:
    def __init__(self):
        self.temp_img = None

    def get_image(self, img, width, height):
        original_size = img.size
        size = [0, 0]
        if original_size[1] * (width / original_size[0]) < height:
            size[0] = width
            size[1] = int(original_size[1] * (width / original_size[0]))
        else:
            size[0] = int(original_size[0] * (height / original_size[1]))
            size[1] = height
        img = img.resize(size)
        self.temp_img = PIL.ImageTk.PhotoImage(img)
        return self.temp_img

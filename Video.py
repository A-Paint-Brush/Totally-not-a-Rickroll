import imageio
import PIL.Image
import Resize


class Video:
    def __init__(self, path, length):
        self.video = imageio.get_reader(path)
        self.frame_count = self.video.count_frames()
        self.resize = Resize.Image()
        self.frame_number = -1
        self.total_audio_f = length
        self.sync_ratio = self.total_audio_f / self.frame_count
        self.iterable = None
        self.video_frame = None
        self.temp_img = None
        self.get_iterable()
        self.tick(0)

    def get_iterable(self):
        self.iterable = self.video.iter_data()

    def tick(self, audio_frame):
        try:
            frame = int(audio_frame / self.sync_ratio)
            while self.frame_number < frame:
                self.video_frame = next(self.iterable)
                self.frame_number += 1
        except StopIteration:
            pass

    def reset(self):
        self.get_iterable()
        self.frame_number = -1

    def get_frame(self, width, height):
        img = self.resize.get_image(PIL.Image.fromarray(self.video_frame), width, height)
        return img

    def close(self):
        self.video.close()

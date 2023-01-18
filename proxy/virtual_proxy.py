class Bitmap:
    def __init__(self, filename):
        self.filename = filename
        print(f"Loading image from {filename}")

    def draw(self):
        print(f"Drawing image {self.filename}")


class LazyBitmap:
    def __init__(self, filename):
        self.filename = filename
        self._bitmap = None

    def draw(self):
        if not self._bitmap:
            self._bitmap = Bitmap(self.filename)
        self._bitmap.draw()


def draw_image(image):
    print("About to draw image")
    image.draw()
    print("Done drawing image")


if __name__ == "__main__":
    BMP = LazyBitmap("facepalm.jpg")  # Bitmap
    draw_image(BMP)

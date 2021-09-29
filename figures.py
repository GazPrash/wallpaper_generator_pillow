import base64
from PIL import Image, ImageDraw


class DrawFigures:
    def __init__(self, size, aa_scale, color):
        self.size = size
        self.aa_scale = aa_scale
        self.color = color

    def canvas(self, shape, cc=0):
        resolution = self.size
        res_img = tuple(x * self.aa_scale for x in resolution)

        self.img = Image.new("RGB", res_img)
        self.image_at_hand = ImageDraw.Draw(self.img, "RGBA")

        if shape == "circle":
            for i in range(10):
                self.circle(
                    res_img[0] / 2,
                    res_img[1] / 2,
                    res_img[0] / 2 * (10 - i) / 10,
                    (*self.color, int(100 * i / 10)),
                )

            self.uplink(0)

        elif shape == "diagonal":
            for i in range(10):
                self.polygon(
                    res_img[0] / 2,
                    res_img[1] / 2,
                    res_img[0] / 2 * (10 - i) / 10,
                    (*self.color, int(100 * i / 10)),
                )

            self.uplink(45)

        elif shape == "spread_circles":

            if cc == 1:
                for i in range(10):
                    self.circle(
                        res_img[0] / 2,
                        res_img[1] / 2,
                        res_img[0] / 2 * (10 - i) / 10,
                        (*self.color, int(100 * i / 10)),
                    )

            centers = [
                (0, 0),
                (res_img[0], 0),
                (0, res_img[1]),
                (res_img[0], res_img[1]),
            ]

            for c in centers:
                self.spread_circle(*c, res_img[0] / 2, 10, self.color, 50)

            self.uplink(0)

        elif shape == "jumbled_polygons":

            for i in range(10):
                self.polygon(
                    res_img[0] / 2,
                    res_img[1] / 2,
                    res_img[0] / 2 * (10 - i) / 10,
                    (*self.color, int(100 * i / 10)),
                )

            centers = [
                (0, 0),
                (res_img[0], 0),
                (0, res_img[1]),
                (res_img[0], res_img[1]),
            ]

            for c in centers:
                self.jumbled_polygons(*c, res_img[0] / 2, 10, self.color, 50)

            self.uplink(45)

        elif shape == "trifecta":

            for i in range(11):
                self.trifecta(
                    res_img[0] / 2,
                    res_img[1] / 2,
                    res_img[0] / 2 * (10 - i) / 10,
                    (*self.color, int(100 * i / 10)),
                )

            self.uplink(0)

    def circle(self, x, y, r, color):
        x, y, r = int(x), int(y), int(r)
        self.image_at_hand.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def polygon(self, x, y, r, color):
        x, y, r = int(x), int(y), int(r)
        self.image_at_hand.rectangle([x - r, y - r, x + r, y + r], fill=color, width=1)

    def spread_circle(self, x, y, max_r, circle_count, color, max_opacity):
        for i in range(circle_count):
            self.circle(
                x,
                y,
                max_r * (circle_count - i) / circle_count,
                (*color, int(max_opacity * i / circle_count)),
            )

    def jumbled_polygons(self, x, y, max_r, rect_count, color, max_opacity):
        for i in range(rect_count):
            self.polygon(
                x,
                y,
                max_r * (rect_count - i) / rect_count,
                (*color, int(max_opacity * i / rect_count)),
            )

    def trifecta(self, x, y, r, color):
        x, y, r = int(x), int(y), int(r)
        self.image_at_hand.regular_polygon(
            (x - r + y + r, x + r + y - r, x + r + y + r), fill=color, n_sides=3
        )

    def uplink(self, rotation):
        self.img = self.img.resize(self.size, resample=Image.ANTIALIAS).rotate(rotation)
        self.img.save('wallgen.png')


if __name__ == "__main__":
    draw1 = DrawFigures((500, 500), 4, (0, 244, 100))
    draw1.canvas("jumbled_polygons")

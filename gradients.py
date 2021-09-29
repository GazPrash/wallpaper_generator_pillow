import random
from PIL import Image, ImageDraw


class Gradient:
    def __init__(self, intensity, size):
        self.intensity = intensity
        self.size = size

    def canvas_one(self):
        for i in range(self.intensity):
            img = Image.new("RGB", self.size, "#FFFFFF")
            image = ImageDraw.Draw(img)

            r, g, b = (
                random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
            )
            dr = (random.randint(0, 255) - r) / self.size[1]
            dg = (random.randint(0, 255) - g) / self.size[1]
            db = (random.randint(0, 255) - b) / self.size[1]

            for i in range(self.size[0]):
                r, g, b = r + dr, g + dg, b + db
                image.line((i, 0, i, self.size[1]), fill=(int(r), int(g), int(b)))

        img.save('wallgen.png')

    def canvas_two(self):  # NOT UTILIZED IN THIS RELEASE YET.
        img = Image.new("RGBA", self.size)

        if self.size[0] >= 500 and self.size[0] <= 600:
            scaling = 2
        elif self.size[0] >= 1280 and self.size[0] <= 1368:
            scaling = 3
        elif self.size[0] >= 1400 and self.size[0] <= 1920:
            scaling = 4
        

        color = random.choice(["REDBLUE", "YELLOW", "CREAM", "BLUE"])

        if color == "REDBLUE":
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    img.putpixel((i, j), (i//scaling, 0, j//scaling))

        elif color == "YELLOW":
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    img.putpixel((i, j), (i//scaling, i//scaling, j//scaling))

        elif color == "CREAM":
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    img.putpixel((i, j), (i//scaling, j//scaling, j//scaling))

        elif color == "BLUE":
            for i in range(self.size[0]):
                for j in range(self.size[1]):
                    img.putpixel((i, j), (j//scaling, 0, j//scaling))

        img.save('wallgen.png')


if __name__ == "__main__":
    gradient1 = Gradient(3, (600, 300))
    gradient1.canvas()

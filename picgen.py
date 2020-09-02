from PIL import Image, ImageDraw, ImageFilter, ImageColor
import sys


def generatePfp(bg_color, head_color, face_color):
    bg = Image.new('RGBA', (1000, 1000), bg_color)
    draw = ImageDraw.Draw(bg)
    draw.ellipse([(50, 50), (950, 950)], fill=head_color, outline='black')

    face = Image.open('img/face.png')
    assert face.mode.endswith('A')
    face.load()
    alpha = face.split()[-1]
    face_fill = Image.new(face.mode, face.size, face_color + (0,))
    face_fill.putalpha(alpha)

    bg.paste(face_fill, (260, 500), face_fill)
    bg.save('output.png', quality=100)


bg_color = ImageColor.getrgb('#' + sys.argv[1])
head_color = ImageColor.getrgb('#' + sys.argv[2])
face_color = ImageColor.getrgb('#' + sys.argv[3])

generatePfp(bg_color, head_color, face_color)

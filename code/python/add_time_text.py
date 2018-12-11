from PIL import Image, ImageDraw, ImageFont
import os

im_width = 960
im_height = 720

# list all file and dir in current dir and extract png filename
dir_info = os.listdir('.')
png_files = [
    png for png in dir_info if os.path.isfile(png) and png.endswith('png')
]
print(len(png_files))

list_texts = [str(num) + ' s' for num in range(0, 1210, 10)]
print(len(list_texts))


def write_text_in_png(png_file, text):
    im = Image.open(png_file)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype('arial.ttf', 36)
    draw.text((im_width / 2, im_height / 20), text, fill='black', font=font)
    im.save(png_file)


for num in range(0, len(png_files)):
    print("processing ", num)
    write_text_in_png(png_files[num], list_texts[num])

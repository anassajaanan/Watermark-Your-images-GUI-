from tkinter import *
from PIL import Image, ImageDraw, ImageFont, ImageTk
from tkinter import filedialog

# =======================================================

# 1 choose the variable (add) to be "add_text" or "add_logo"

# add = "add_text" or "add_logo"
# if you choose (add = "add_text")
# text = "input watermark text here"

# Example1
# add = "add_text"
# text = "Anas Ajaanan"

# Example2
# add = "add_logo"

# ========================================================

window = Tk()
window.title("Watermark your images")
window.config(width=940, height=788)

def add_text(filename, text):
    im = Image.open(filename)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = f"© {text}"

    font = ImageFont.truetype('arial.ttf', 40)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 5
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    im.show()

    # Save watermarked image
    name = filename.split('/')[-1]
    im.save(f'images/{name}')
    canvas.create_text(470, 50, text="✔ Watermark has been Successfully added", font=("Arial", "30", "bold"), fill="#E9C46A")


def add_logo(filename):
    im1 = Image.open(filename)
    width, height = im1.size
    logo = Image.open('main/logo.png')
    logowidth, logoheight = logo.size
    copy_im1 = im1.copy()
    copy_im1.paste(logo, (int(width/2)-int(logowidth/2), height-115), logo)
    copy_im1.show()
    name = filename.split('/')[-1]
    copy_im1.save(f'images/{name}')
    canvas.create_text(470, 50, text="✔ Watermark has been Successfully added", font=("Arial", "30", "bold"), fill="#E9C46A")





def UploadAction(event=None):
    filename = filedialog.askopenfilename()
    if add == "add_logo":
        add_logo(filename)
    else:
        add_text(filename, text=text)


canvas = Canvas(window, width=940, height=788)
bg_image = ImageTk.PhotoImage(Image.open("main/background.png"))
canvas.create_image(470, 394, image=bg_image)


button = Button(canvas, text='Select Image', command=UploadAction, width=15, height=1, bg="#E9C46A", highlightthickness=0, borderwidth=0, font=("ariel", "17","bold"), fg="white")
button.place(x=95, y=645)
canvas.place(x=0, y=0)




window.mainloop()
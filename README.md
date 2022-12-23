# Watermark Your Images

A simple graphical user interface (GUI) application that allows you to watermark your images by either adding a logo or text to the image.



## Requirements

- Python 3
- Tkinter (should be included with Python)
- Python Imaging Library (PIL)

## Usage

1. Clone or download the repository
2. Open a terminal in the root directory of the repository
3. Run the following command to start the application:

```bash
python main.py
```

4. Select the image you want to watermark using the "Select Image" button
5. Choose either "add_text" or "add_logo" for the 'add' variable in the script
6. If you choose "add_text", enter the text you want to use as the watermark in the 'text' variable
7. The watermarked image will be displayed and saved in the 'images' directory



## Customization

You can customize the appearance of the watermark by modifying the following variables in the script:

- `font`: the font and size of the text watermark. You can use a different font by specifying a different font file and size.
- `margin`: the distance between the watermark and the edge of the image
- `x` and `y`: the coordinates of the watermark on the image. You can change the position of the watermark by adjusting these values.
- `logo`: the logo image file used for the logo watermark. You can use a different logo by specifying a different image file.


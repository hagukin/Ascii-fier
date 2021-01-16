#!/usr/bin/env python3
import copy
import traceback
import tcod
import PIL.Image

# resize image accprdomg to a new width
def resize_image(image, new_width):
    width, height = image.size
    ratio = int(height / width * 100)
    new_height = int(new_width * ratio / 100)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)


# convert pixels to a string of ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[int(pixel/255*len(ASCII_CHARS)) - 1] for pixel in pixels])
    return(characters)


def main(new_width=50):

    # Open image from user input (string)
    path = input("Enter a valid file name to an image.\nImage must be located in the main folder.\nDo not include the file extension name:")
    try:
        image = PIL.Image.open(path + ".png")
    except:
        try:
            image = PIL.Image.open(path + ".jpg")
        except:
            print(path, "is not a valid file name to an image.")
            return -1

    # grayify & convert to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    # format (.txt)
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))

    # write result
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_image)

    # print result
    with open("ascii_img.txt", "r") as f:
        f_read = f.read()
        print(f_read)
        # for line in f:
        #     print(line, end="")

    # Console settings
    screen_width = 90
    screen_height = 50

    # Font
    tileset = tcod.tileset.load_tilesheet(
        "sources\\Cheepicus-8x8x2.png", 16, 16, tcod.tileset.CHARMAP_CP437
    )

    # Open Terminal
    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Ascii-fier",
        # sdl_window_flags=tcod.context.SDL_WINDOW_FULLSCREEN_DESKTOP,
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        testgraphic = open("ascii_img.txt").read()
        root_console.clear()
        root_console.print(0,0, string=testgraphic, fg=(253, 106, 2))
        context.present(root_console, keep_aspect=True)
        input()

if __name__ == "__main__":

    # Title
    print("ImgAscii-fier Alpha\n")

    # ascii characters selection
    try:
        detail = int(input("Detail parameter 0 ~ 4 : (def 1)"))
    except:
        detail = 1

    if detail == 0:
        ASCII_CHARS = ["#", ":", " "]
    elif detail == 1:
        ASCII_CHARS = ["@", "$", "?", "+", ":", ".", " "]
    elif detail == 2:
        ASCII_CHARS = ["@", "%", "W", "*", "h", "w", "O", "C", "J", "+", "\'", ",", "_", " "]
    elif detail == 3:
        ASCII_CHARS = ["@", "#", "E", "O", "T", "*", "+", "\"", ":", ",", ".", "-", "\'", "_", ".", " "]
    elif detail == 4:
        ASCII_CHARS = ["@","%","&","B","8","#","W","M","$","w","m","e","*","b","d","p","q","X","Z","Q","O","0","J","x","C","L","U","Y","z","c","v","u","n","r","/","\\","|","(",")","{","}","[","]",";",":","^","-","_",".",",",",","\'"," "]
    elif detail == 999:
        ASCII_CHARS = ["G", "M", "E", "S", "H", "A", "T", "I"]
    else:
        ASCII_CHARS = ["@", "$", "?", "+", ":", ".", " "]
        
    # set resize width from user input
    try:
        new_width = int(input("Image width (pixels) : (def 50)"))
    except:
        new_width = 50

    # Activate
    main(new_width)
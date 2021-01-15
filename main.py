#!/usr/bin/env python3
import tkinter as tk
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
def pixels_to_ascii(image, ascii_chars):
    pixels = image.getdata()
    characters = "".join([ascii_chars[int(pixel/255*len(ascii_chars)) - 1] for pixel in pixels])
    return(characters)

def generate_art():
    path = image_path.get()
    width = int(image_width.get())
    detail = int(image_detail.get())

    if not path:
        path = "NO PATH WAS ENTERED"
    if not width:
        width = 50
    if not detail:
        detail = 0

    log.delete(0.0, tk.END)

    # Setup Ascii characters
    ascii_chars = ("@", "$", "?", "+", ":", ".", " ")
    if detail == 0:
        ascii_chars = ("#", ":", " ")
    elif detail == 1:
        ascii_chars = ("@", "$", "?", "+", ":", ".", " ")
    elif detail == 2:
        ascii_chars = ("@", "%", "W", "*", "h", "w", "O", "C", "J", "+", "\'", ",", "_", " ")
    elif detail == 3:
        ascii_chars = ("@", "#", "E", "O", "T", "*", "+", "\"", ":", ",", ".", "-", "\'", "_", ".", " ")
    elif detail == 4:
        ascii_chars = ("@","%","&","B","8","#","W","M","$","w","m","e","*","b","d","p","q","X","Z","Q","O","0","J","x","C","L","U","Y","z","c","v","u","n","r","/","\\","|","(",")","{","}","[","]",";",":","^","-","_",".",",",",","\'"," ")

    # Open File
    try:
        image = PIL.Image.open(path)
    except:
        log.insert(tk.END, f"Invalid path : {path}.")
        return -1

    # grayify & convert to ascii
    new_image_data = pixels_to_ascii(grayify(resize_image(image, width)), ascii_chars=ascii_chars)

    # format (.txt)
    pixel_count = len(new_image_data)
    ascii_image = "\n".join(new_image_data[i:(i+width)] for i in range(0, pixel_count, width))

    # write result
    with open("ascii_img.txt", "w") as f:
        f.write(ascii_image)
    
    # print result
    log.insert(tk.END, ascii_image)


## GUI ##
root = tk.Tk()
root.title("Ascii-fier GUI")
root.configure(background="black")

label0 = tk.Label(root, text="Ascii-fier", fg="white", bg="black").grid(row=0, column=0)

label1 = tk.Label(root, text="Image path: ", fg="white", bg="black").grid(row=1, column=0, sticky=tk.W)
image_path = tk.Entry(root, width=20)
image_path.grid(row=1, column=1)

label2 = tk.Label(root, text="Desired width (size px, height automatically processed): ", fg="white", bg="black").grid(row=2, column=0, sticky=tk.W)
image_width = tk.Entry(root, width=5)
image_width.grid(row=2, column=1)

label4 = tk.Label(root, text="Desired Detail Level: ", fg="white", bg="black").grid(row=4, column=0, sticky=tk.W)
image_detail = tk.Entry(root, width=5)
image_detail.grid(row=4, column=1)

log = tk.Text(root, width=100, height=100, wrap=tk.WORD, background="white")
log.grid(row=5, column=0)

submit_button = tk.Button(root, text="Generate", width=8, height=3, command=generate_art).grid(row=5, column=1)

root.mainloop()

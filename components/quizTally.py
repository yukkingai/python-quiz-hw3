from components import vars
from PIL import Image

def total(value):
    # do some logic to see which character you selected

    if value <= 60:
        vars.character = vars.characters[0]

        im = Image.open("thor.png")
        im.show()
        #print(im.format,im.size,im.mode)
        print("You are " + vars.character)

    if value <= 90:
        vars.character = vars.characters[1]

        im = Image.open("iron-man.png")
        im.show()
        #print(im.format,im.size,im.mode)
        print("You are " + vars.character)

    if value <= 240:
        vars.character = vars.characters[2]

        im = Image.open("scarlett-witch.png")
        im.show()
        #print(im.format,im.size,im.mode)
        print("You are " + vars.character)

    if value >= 250:
        vars.character = vars.characters[3]

        im = Image.open("captin-marvel.png")
        im.show()
        #print(im.format,im.size,im.mode)
        print("You are " + vars.character)
        # add some emoji icons, or show the character image using the Pillow package

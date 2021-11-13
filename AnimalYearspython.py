

print('█▀▀█ █▀▀▄ ░▀░ █▀▄▀█ █▀▀█ █░░   █░░█ █▀▀ █▀▀█ █▀▀█ █▀▀')
print('█▄▄█ █░░█ ▀█▀ █░▀░█ █▄▄█ █░░   █▄▄█ █▀▀ █▄▄█ █▄▄▀ ▀▀█')
print('▀░░▀ ▀░░▀ ▀▀▀ ▀░░░▀ ▀░░▀ ▀▀▀   ▄▄▄█ ▀▀▀ ▀░░▀ ▀░▀▀ ▀▀▀')
print('By Restless Mango')


import tkinter as tk


def dog_slogan():
    dog = input('In years how long has your dog been alive?')
    dog = int (dog) 
    dyears = 9 * dog
    print('In dog years your dog is', dyears, 'years old')

def cat_slogan():
    cat = input('In years how long has your cat been alive?')
    cat = int (cat)
    catyears = 7 * cat
    print('In cat years your cat is', catyears, 'years old')

def bunny_slogan():
    bunny = input('In years how long has your bunny been alive?')
    bunny = int (bunny)
    bunnyyears = 9 * bunny
    print('In bunny years your bunny is', bunnyyears, 'years old')


def hamster_slogan():
    hamster = input('In years how long has your hamster been alive?')
    hamster = int (hamster)
    hamsteryears = 26 * hamster
    print('In hamster years your hamster is', hamsteryears, 'years old')


def goldfish_slogan():
    goldfish = input('In years how long has your goldfish been alive?')
    goldfish = int (goldfish)
    goldfishyears = 6 * goldfish
    print('In goldfish years your goldfish is', goldfishyears, 'years old')


def ferret_slogan():
    ferret = input('In years how long has your ferret been alive?')
    ferret = int (ferret)
    ferretyears = 11 * ferret
    print('In ferret years your ferret is', ferretyears, 'years old')



def parrot_slogan():
    parrot = input('In years how long has your parrot been alive?')
    parrot = int (parrot)
    parrotyears = 2 * parrot
    print('In parrot years your parrot is', parrotyears, 'years old')

def turtle_slogan():
    turtle = input('In years how long has your turtle been alive?')
    turtle = int (turtle)
    turtleyears = 2 * turtle
    print('In turtle years your turtle is', turtleyears, 'years old')
    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT",
                   fg="red",
                command=quit)
button.pack(side=tk.LEFT)

slogan = tk.Button(frame,
                   text="Dog Years",
                   fg="green",
                   command=dog_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Cat Years",
                   fg="green",
                   command=cat_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Bunny Years",
                   fg="green",
                   command=bunny_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hamster Years",
                   fg="green",
                   command=hamster_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Goldfish Years",
                   fg="green",
                   command=goldfish_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Ferret Years",
                   fg="green",
                   command=ferret_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Parrot Years",
                   fg="green",
                   command=parrot_slogan)
slogan.pack(side=tk.LEFT)

button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Turtle Years",
                   fg="green",
                   command=turtle_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()


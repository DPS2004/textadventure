import time
import msvcrt
import random
from os import system, name


def waitforkey():
    msvcrt.getch()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def dialog(character: object, text: object, loops: object, animdelay: object) -> object:
    for x in range(loops):
        if character == "detective":
            clear()
            print("            ______")
            print("        ___/______\___")
            print("           |      |")
            print("           |  O  O|")
            print("           |   __>|")
            print("           |  (__)|")
            print("           |______|")
            print(" ")
            print(" |",cname + ":",text,"|")
            time.sleep(animdelay)
            clear()
            print("            ______")
            print("        ___/______\___")
            print("           |      |")
            print("           |  O  O|")
            print("           |     >|")
            print("           |  ___ |")
            print("           |______|")
            print(" ")
            print(" |",cname + ":",text,"|")
            time.sleep(animdelay)
        if character == "masked":
            clear()
            print("          _____   ")
            print("         /     \ ")
            print("        / _  _  \ ")
            print("       | |_|| |  |")
            print("       |    |_|  |")
            print("        \ ____  /")
            print("         \_____/")
            print(" ")
            print(" ")
            print(" |",enemyname + ":",text,"|")
            time.sleep(animdelay)
            clear()
            print(" ")
            print("          _____   ")
            print("         /     \ ")
            print("        / _  _  \ ")
            print("       | |_|| |  |")
            print("       |    |_|  |")
            print("        \ ____  /")
            print("         \_____/")
            print(" ")
            print(" |",enemyname + ":",text,"|")
            time.sleep(animdelay)
    print("(press key)")
    waitforkey()


def question(prompt):
    clear()
    return input(prompt)

def yesno(inputyn):
    if inputyn.lower() in ["yes", "y", "yay"]:
        return "y"
    else:
        return "n"


cname = question("what do you want to name your detective? ")
print("you are detective", cname + ", ready to solve crimes and stuff")
waitforkey()
dialog("detective", "oh boy i sure love being a detective", 4, 0.2)
enemyname = question("a masked stranger come up to you. What is his name?")
dialog("masked", "yo whats up mr detective man i need some detective crap done for me my dude", 5, 0.25)
dialog("detective", "oh man oh jeez ok sure what will i get in return", 6, 0.15)
dialog("masked", "you will get a magical artifact i totally didn't imbue with a curse", 5, 0.25)
dialog("detective", "seems legit", 2, 0.2)
dialog("masked", "someone broke in to my house. who the heck did it?", 5, 0.25)
dialog("detective", "who are the suspects?", 3, 0.15)
dialog("masked", "Casey, who is my dog, Mrs. Greene, who is my cranky old neighbor, and Carson, who is my ex best friend", 12, 0.25)
dialog("detective", "wait hold up why is your dog in the lineup?", 2, 0.2)
dialog("masked", "he can be a bit of a jerk, i wouldn't put it past him", 3, 0.25)
if yesno(question("take up the case? ")) == "y":
    dialog("detective", "ok, take me to the scene of the crime.", 4, 0.2)
else:
    dialog("detective", "dude, you are crazy, im not doing this", 4, 0.25)
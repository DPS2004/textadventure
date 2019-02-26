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


def dialog(character, text, loops, animdelay):
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
            print(" |",cname,":",text,"|")
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
            print(" |",cname,":",text,"|")
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
            print(" |",enemyname,":",text,"|")
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
            print(" |",enemyname,":",text,"|")
            time.sleep(animdelay)
    print("(press key)")
    waitforkey()


cname = input("what do you want to name your detective? ")
print("you are detective", cname, "ready to solve crimes and stuff")
waitforkey()
dialog("detective", "oh boy i sure love being a detective", 4, 0.2)
clear()
enemyname = input("a masked stranger come up to you. What is his name?")
dialog("masked", "yo whats up mr detective man i need some detective crap done for me my dude", 5, 0.25)
dialog("detective", "oh man oh jeez ok sure what will i get in return", 6, 0.15)
dialog("masked", "you will get a magical artifact i totally didn't imbue with a curse", 5, 0.2.5)
dialog("detective", "seems legit", 2, 0.2)

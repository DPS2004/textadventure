import time
import msvcrt
import random
import os
from os import system, name


def s2n(strin):
    return int(strin)


def n2s(numb):
    return str(numb)


def investlist(showlist):
    if investinput == "list":
        print(showlist)
        investinput == question("")


def printtxt(txtfile):
    file = open(txtfile, 'r')
    file_contents = file.read()
    print(file_contents)
    file.close()


def findline(linenum):
    with open("savefile.sav", "r") as file:
        for _ in range(linenum):
            line = file.readline()
    return line


def saveall(sname, senemyname, scheckpoint,):
    file = open("savefile.sav", "w")
    file.writelines((line + '\n' for line in [sname, senemyname, n2s(scheckpoint)]))
    file.close()


def waitforkey():
    msvcrt.getch()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def dialog(spritename, text, loops, animdelay):
    for x in range(loops):
        clear()
        printtxt("ascii/"+spritename+"1.txt")
        print(" ")
        print(" |", cname + ":", text, "|")
        time.sleep(animdelay)
        clear()
        printtxt("ascii/"+spritename+"2.txt")
        print(" ")
        print(" |", cname + ":", text, "|")
        time.sleep(animdelay)
    print("(press key)")
    waitforkey()


def question(prompt):
    clear()
    return input(prompt)


def yesno(inputyn):
    if inputyn.lower() in ["yes", "y", "yay", "yep", "sure", "yeah", "yeet", "mhm", "positively"]:
        return "y"
    else:
        return "n"


if yesno(question("Welcome to detective game! would you like to load a saved game?")) == "y":
    if os.path.isfile("./savefile.sav"):
        cname = findline(1)
        enemyname = findline(2)
        checkpoint = s2n(findline(3))

    else:
        print("No save file found :(")
        cname = question("what do you want to name your detective? ")
        checkpoint = 0
else:
    cname = question("what do you want to name your detective? ")
    if cname == "debug":
        cname = "Detective"
        enemyname = "Masked man"
        print("debug mode activated!")
        checkpoint = s2n(question("warp to what checkpoint?"))
    else:
        checkpoint = 0
if checkpoint == 0:
    print("you are detective", cname + ", ready to solve crimes and stuff")
    waitforkey()
    dialog("detective", "oh boy i sure love being a detective", 4, 0.2)
    enemyname = question("a masked stranger come up to you. What is his name?")
    dialog("masked", "yo whats up mr detective man i need some detective crap done for me my dude", 5, 0.25)
    dialog("detective", "oh man oh jeez ok sure what will i get in return", 6, 0.15)
    dialog("masked", "you will get a magical artifact i totally didn't imbue with a curse", 5, 0.25)
    dialog("detective", "seems legit", 2, 0.2)
    checkpoint = "1"
    saveall(cname,enemyname,checkpoint)
if checkpoint == 1:
    dialog("masked", "someone broke in to my house. who the heck did it?", 5, 0.25)
    dialog("detective", "who are the suspects?", 3, 0.15)
    dialog("masked", "Casey, who is my dog, Mrs. Greene, who is my cranky old neighbor, and Carson, who is my ex best friend", 12, 0.25)
    dialog("detective", "wait hold up why is your dog in the lineup?", 2, 0.2)
    dialog("masked", "he can be a bit of a jerk, i wouldn't put it past him", 3, 0.25)
    if yesno(question("take up the case? ")) == "y":
        dialog("detective", "ok, take me to the scene of the crime.", 4, 0.2)
        checkpoint = 2
    else:
        dialog("detective", "dude, you are crazy, im not doing this", 4, 0.25)
        dialog("masked", "but don't you want to get that magical artifact??", 4, 0.35)
        dialog("detective", "...yes", 1, 1)
        dialog("masked", "then it it is settled!", 4, 0.2)
        dialog("masked", "to the crime scene!!", 4, 0.2)
        checkpoint = 2
    saveall(cname, enemyname, checkpoint)
if checkpoint == 2:
    printtxt("ascii/howtoinvestigate.txt")
    waitforkey()
    while 0==0:
        clear()
        printtxt("ascii/bustedhouse.txt")
        investinput = question("")
        investlist("left shrub, right shrub, left window, right window, door, roof, mailbox")
        if investinput == "left shrub":
            while 0==0:
                clear()
                printtxt("ascii/leftshrub.txt")
        if investinput == "right shrub":
            while 0==0:
                clear()
                printtxt("ascii/rightshrub.txt")






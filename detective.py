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


def saveall(sname, shatname, scheckpoint,):
    file = open("savefile.sav", "w")
    file.writelines((line + '\n' for line in [sname, shatname, n2s(scheckpoint)]))
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


def dialog(spritename, displayname, text, loops, animdelay):
    for x in range(loops):
        clear()
        printtxt("ascii/"+spritename+"1.txt")
        print(" ")
        print(" |", displayname + ":", text, "|")
        time.sleep(animdelay)
        clear()
        printtxt("ascii/"+spritename+"2.txt")
        print(" ")
        print(" |", displayname + ":", text, "|")
        time.sleep(animdelay)
    print("(press key)")
    waitforkey()


def question(prompt):
    clear()
    return input(prompt)


def yesno(inputyn):
    if inputyn.lower() in ["yes", "y", "yay", "yep", "sure", "yeah", "yeet", "mhm", "positively", "indeedily-doo"]:
        return "y"
    else:
        return "n"


if yesno(question("Welcome to detective game! would you like to load a saved game?")) == "y":
    if os.path.isfile("./savefile.sav"):
        cname = findline(1)
        hatname = findline(2)
        checkpoint = s2n(findline(3))

    else:
        print("No save file found :(")
        cname = question("what do you want to name your detective? ")
        checkpoint = 0
else:
    cname = question("what do you want to name your detective? ")
    if cname == "debug":
        cname = "Detective"
        hatname = "Top hat man"
        print("debug mode activated!")
        checkpoint = s2n(question("warp to what checkpoint?"))
    else:
        checkpoint = 0
if checkpoint == 0:
    print("you are detective", cname + ", ready to solve crimes and stuff")
    waitforkey()
    dialog("detective", cname, "Time to open up the office.", 4, 0.2)
    hatname = question("The door opens, and a man with a strange hat comes up to you. What is his name?")
    dialog("tophatmutter", hatname, "*mutters something about a detective", 5, 0.25)
    dialog("detective", cname, "Can you speak up please?", 5, 0.15)
    clear()
    print("The man begins to yell.")
    waitforkey()
    dialog("tophatyell", hatname, "YES HELLO THERE IS THIS THE DETECTIVE PLACE I NEED A DETECTIVE FOR MY DETEECTIVATING NEEDS", 7, 0.25)
    dialog("detectiveangry", cname, "Indoor voice please!", 2, 0.2)
    dialog("tophatyell", hatname, "THIS IS INDOOR VOICE", 4, 0.2)
    dialog("detectiveangry",cname, "I am sure that you have woken up the entire neighborhood by now.", 6, 0.18)
    dialog("detective", cname, "Can you talk at my volume?", 4, 0.2)
    dialog("tophatyell", hatname, "Indeedily-doo.", 3, 0.25)
    checkpoint = "1"
    saveall(cname,hatname,checkpoint)
if checkpoint == 1:
    dialog("tophatyell", hatname, "Someone has broked in to house. Who the heck did?", 5, 0.25)
    dialog("detective", cname, "who are the suspects?", 3, 0.15)
    dialog("tophatyell", hatname, "Casey, who is my dog, Mrs. Greene, who is meanie old neighbor, and Carson, who is used to be best friend", 12, 0.25)
    dialog("detectiveangry", cname, "wait hold up why is your dog in the lineup?", 2, 0.2)
    dialog("tophatyell", hatname, "He can be jerk, would not put past him", 3, 0.25)
    if yesno(question("take up the case? ")) == "y":
        dialog("detective", "ok, take me to the scene of the crime.", 4, 0.2)
        checkpoint = 2
    else:
        dialog("detectiveangry", cname, "You are clearly insane. I am not doing this.", 7, 0.25)
        dialog("tophatyell", hatname, "You have other case to do??", 4, 0.35)
        dialog("detective", cname, "...no", 1, 1)
        dialog("tophatyell", "then it it is settled!", 4, 0.2)
        dialog("tophatyell", "to the crime scene!!", 4, 0.2)
        checkpoint = 2
    saveall(cname, hatname, checkpoint)
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






import time
import msvcrt
import random
import os
from os import system, name
investinput = "nothing"
consoleinput = 0
fasttext = "n"
def s2n(strin):
    return int(strin)


def n2s(numb):
    return str(numb)


def investlist(showlist, linput):
    if linput == "list":
        print(showlist)
        return question("", "n")
    else:
        return linput


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


def saveall(sname, shatname, scheckpoint, sconsolinput):
    file = open("savefile.sav", "w")
    file.writelines((line + '\n' for line in [sname, shatname, n2s(scheckpoint), sconsolinput]))
    file.close()


def waitforkey():
    if consoleinput == "y":
        input()
    else:
        msvcrt.getch()


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def dialog(spritename, displayname, text, loops, animdelay):
    if fasttext == "y":
        loops = 1
        animdelay = 0.1
    for x in range(loops):
        clear()
        printtxt("ascii/"+spritename+"/"+spritename+"1.txt")
        print(" ")
        print(" |", displayname + ":", text, "|")
        time.sleep(animdelay)
        clear()
        printtxt("ascii/"+spritename+"/"+spritename+"2.txt")
        print(" ")
        print(" |", displayname + ":", text, "|")
        time.sleep(animdelay)
    print("(press key)")
    waitforkey()


def question(prompt, clearyn):
    if clearyn == "y":
        clear()
    return input(prompt)


def yesno(inputyn):
    if inputyn.lower() in ["yes", "y", "yay", "yep", "sure", "yeah", "yeet", "mhm", "positively", "indeedily-doo"]:
        return "y"
    else:
        return "n"


#main script

if yesno(question("Welcome to detective game! would you like to load a saved game? ", "y")) == "y":
    if os.path.isfile("./savefile.sav"):
        cname = findline(1)
        hatname = findline(2)
        checkpoint = s2n(findline(3))
        consoleinput = findline(4)
    else:
        print("No save file found :(")
        cname = question("what do you want to name your detective? ", "n")
        checkpoint = 0
        consoleinput = "n"
        fasttext = "n"
else:
    cname = question("what do you want to name your detective? ", "y")
    if cname == "debug":
        cname = "Detective"
        hatname = "Top hat man"
        print("debug mode activated!")
        consoleinput = yesno(question("use python console input? ", "n"))
        checkpoint = s2n(question("warp to what checkpoint? ", "n"))
        fasttext = yesno(question("activate fast text mode? ", "n"))
        clear()
    else:
        checkpoint = 0
        consoleinput = "n"
        fasttext == "n"
if checkpoint == 0:
    print("you are detective", cname + ", ready to solve crimes and stuff")
    waitforkey()
    dialog("detective", cname, "Time to open up the office.", 4, 0.2)
    hatname = question("The door opens, and a man with a strange hat comes up to you. What is his name? ", "y")
    dialog("tophatmutter", hatname, "*mutters something about a detective", 5, 0.25)
    dialog("detective", cname, "Can you speak up please?", 5, 0.15)
    clear()
    print("The man begins to yell.")
    waitforkey()
    dialog("tophatyell", hatname, "YES HELLO THERE IS THIS THE DETECTIVE PLACE I NEED A DETECTIVE FOR MY DETECTIVATING NEEDS", 7, 0.25)
    dialog("detectiveangry", cname, "Indoor voice please!", 2, 0.2)
    dialog("tophatyell", hatname, "THIS IS INDOOR VOICE", 4, 0.2)
    dialog("detectiveangry",cname, "I am sure that you have woken up the entire neighborhood by now.", 6, 0.18)
    dialog("detective", cname, "Can you talk at my volume?", 4, 0.2)
    dialog("tophatyell", hatname, "Indeedily-doo.", 3, 0.25)
    checkpoint = 1
    saveall(cname,hatname,checkpoint,consoleinput)
if checkpoint == 1:
    dialog("tophatyell", hatname, "Someone has broked in to house. Who the heck did?", 5, 0.25)
    dialog("detective", cname, "who are the suspects?", 3, 0.15)
    dialog("casey", hatname, "Casey, who is my dog...", 3, 0.25)
    dialog("greene", hatname, "Mr. Greene, who is meanie old neighbor...", 4, 0.25)
    dialog("carson", hatname, "and Carson, who is used to be best friend", 5, 0.25)
    dialog("detectiveangry", cname, "Wait, hold up, why is your dog in the lineup?", 2, 0.2)
    dialog("casey", hatname, "He can be jerk, would not put past him", 3, 0.25)
    dialog("detective", cname, "Ok, I can do this. Are you paying me with cash, or a credit card?",6, 0.19)
    dialog("tophatyell", hatname, "Cash.", 1, 0.4)
    dialog("tophatyell", hatname, "Here is one million dollarinos! I think that enough.", 7, 0.2)
    clear()
    print("He hands you a piece of paper")
    waitforkey()
    printtxt("ascii/items/dollarino.txt")
    waitforkey()
    clear()
    print("You observe that contrary to what it says, it is not a real form of currency.")
    waitforkey()
    if yesno(question("Take up the case? ", "y")) == "y":
        dialog("detective", "Ok, take me to the scene of the crime.", 4, 0.2)
        dialog("tophatyell", "Huzzah! The other detectiveman would not take case. Thank you much!", 6, 0.16)
        checkpoint = 2
    else:
        dialog("detectiveangry", cname, "You are clearly insane. I am not doing this.", 7, 0.25)
        dialog("tophatyell", hatname, "You have other case to do??", 4, 0.35)
        dialog("detective", cname, "...no", 1, 1)
        dialog("tophatyell", "then is settled!", 4, 0.18)
        dialog("tophatyell", "to crime scene!!", 3, 0.2)
        checkpoint = 2
    saveall(cname, hatname, checkpoint, consoleinput)
if checkpoint == 2:
    printtxt("ascii/pop_ups/howtoinvestigate.txt")
    waitforkey()
    while 0==0:
        clear()
        printtxt("ascii/locations/bustedhouse/bustedhouse.txt")
        print("You see a house with a busted window in front of you.")
        investinput = question("", "n")
        investinput = investlist("left shrub, right shrub, left window, right window, door,, mailbox", investinput)
        if investinput == "list":
            print("you already have a list open!")
            waitforkey()
        if investinput == "left shrub":
            while 0==0:
                clear()
                printtxt("ascii/locations/bustedhouse/leftshrub/leftsrhub.txt")
                print("You are looking at a shrub on the left side of the house. ")
                investinput = question("", "n")
                investinput = investlist("shards of glass, broken branch", investinput)
                if investinput == "list":
                    print("you already have a list open!")
                    waitforkey()

                if investinput == "back":
                    break
        if investinput == "right shrub":
            while 0==0:
                clear()
                printtxt("ascii/locations/bustedhouse/rightshrub/rightshrub.txt")
                print("You are looking at a shrub on the right side of the house")
                investinput = question("", "n")
                investinput = investlist("Nothing of note", investinput)
                if investinput == "list":
                    print("you already have a list open!")
                    waitforkey()
                if investinput == "back":
                    break
        if investinput == "right window":
            while 0==0:
                clear()
                printtxt("ascii/locations/bustedhouse/rightwindow/rightwindow.txt")
                print("You are looking at a window on the right side of the house.")
                investinput = question("", "n")
                investinput = investlist("Curtain, bird feces", investinput)
                if investinput == "list":
                    print("you already have a list open!")
                    waitforkey()
                if investinput == "bird feces":
                    while 0 == 0:
                        clear()
                        printtxt("ascii/locations/bustedhouse/rightwindow/birdfeces/birdfeces.txt")
                        print("You are looking at bird feces in the form of a white stain on the windowsill.")
                        investinput = question("", "n")
                        investinput = investlist("Nothing of note", investinput)
                        if investinput == "list":
                            print("you already have a list open!")
                            waitforkey()
                        if investinput == "back":
                            break
                if investinput == "curtain":
                    while 0 == 0:
                        clear()
                        printtxt("ascii/locations/bustedhouse/rightwindow/curtain/curtain.txt")
                        print("You are looking at the curtain that is in the window. It has many small holes in it.")
                        investinput = question("", "n")
                        investinput = investlist("Holes", investinput)
                        if investinput == "list":
                            print("you already have a list open!")
                            waitforkey()
                        if investinput == "holes":
                            while 0 == 0:
                                clear()
                                printtxt("ascii/locations/bustedhouse/rightwindow/curtain/holes/holes.txt")
                                print("upon closer inpection, the holes are bite marks.")
                                investinput = question("", "n")
                                investinput = investlist("Nothing of note", investinput)
                                if investinput == "list":
                                    print("you already have a list open!")
                                    waitforkey()
                                if investinput == "back":
                                    break
                        if investinput == "back":
                            break
                if investinput == "back":
                    break

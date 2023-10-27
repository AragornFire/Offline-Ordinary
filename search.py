from termcolor import colored, cprint #Get cprint command, I was told to import colored, don't know what it does, research needed

file_name = 'majorOrdinary.txt'#Default ordinary

#Colors consistent with termcolor
code_color = 'yellow'
blazon_color = 'blue'
name_color = 'light_blue'
source_color = 'red'

#The main searching function
def searchOrdinary(search_list: list) -> str: #Takes a list with all search terms and outputs all the lines containing all the terms
    with open(file_name, 'r') as f: #File is read and referred to as f
        for line in f: #Iterate over every line in the file
            keepGoing = True #Continue reading line and printing are determined by this variable, which is reset to True here
            i = 0 #First index to check
            while (i < len(search_list)) and keepGoing: #While loop used to avoid 'break' and use keepGoing
                if search_list[i] not in line: #Breaks the loop if a value in 
                    keepGoing = False
                i = i + 1 #Increment
            if keepGoing: #If we would have kept going, we know all search terms are in the line, and so print it
                if (" - " in line) and (len(line.split(" - ")) == 4): #Uses the formatting for the entries to divide the line and color each part separately
                    cprint(line.split(" - ")[0], code_color, end = '')
                    print(" - ", end = '')
                    cprint(line.split(" - ")[1], blazon_color, end = '')
                    print(" - ", end = '')
                    cprint(line.split(" - ")[2], name_color, end = '')
                    print(" - ", end = '')
                    cprint(line.split(" - ")[3], source_color, end = '')
                else:
                    cprint(line, code_color, end = '') #Printing a non-entry line, always code_color, might change it
    print()

def searchOrdinaryExcl(include_list,exclude_list):
    if include_list == []:
        include_list = ['']
    with open(file_name, 'r') as f:
        for line in f:
            keepGoing = True
            i = 0
            while (i < len(include_list)) and keepGoing:
                if include_list[i] not in line:
                    keepGoing = False
                for bad_item in exclude_list:
                    if bad_item in line:
                        keepGoing = False
                i = i + 1
            if keepGoing:
                if (" - " in line) and (len(line.split(" - ")) == 4):
                    cprint(line.split(" - ")[0], code_color, end = '')
                    print(" - ", end = '')
                    cprint(line.split(" - ")[1], blazon_color, end = '')
                    print(" - ", end = '')
                    cprint(line.split(" - ")[2], name_color, end = '')
                    print(" - ", end = '')
                    cprint(line.split(" - ")[3], source_color, end = '')
                else:
                    cprint(line, code_color, end = '')
    print()

def help():
    print("Sorry, this section isn't fully fleshed out.\n")
    print("For specifics on a command, run:\n")
    cprint("ask('command')\n", "green")
    print("To search in the current ordinary, run:\n")
    cprint("searchOrdinary(['term','term','term'])\n", "green")
    print("with 'term' replaced by every term you want to look for, surrounded by quotes and separated by commas (can take any number).\n")
    print("To run an exclusive search, run:\n")
    cprint("searchOrdinaryExcl(['yes','yes','yes'],['no','no','no'])\n", "green")
    print("with 'yes' replaced with the terms you want and 'no' the terms you don't.")
    print("Currently, this program is searching the ordinary: ", end = '')
    cprint(file_name, "light_yellow", "on_blue", attrs = ["bold"])
    print("To change this, run:\n")
    cprint("setOrdinary('new_file')\n", "green")
    print("with 'new_file' replaced with the file name of the ordinary you would like to search.")

def ask(command):
    if command == '':
        print("Did you forget to add a command? Try ", end = '')
        cprint("ask('help')", "green")
    elif command == 'help':
        print("Description: provides the commands the program uses\nand how to use them.\n")
        cprint("help()\n", "green")
        print("Takes no arguments.")
    elif command == 'searchOrdinary':
        print("Description: searches the currently selected ordinary\nusing the inputted list.\n")
        cprint("searchOrdinary(['term','term','term'])\n", "green")
        print("Takes a list [] containing strings ''.")

def setOrdinary(new_file):
    global file_name
    file_name = new_file
    print("Confirm, new file is: ", end = '')
    cprint(file_name, "light_yellow", "on_blue", attrs = ["bold"])

def changeColors(codec,blazonc,namec,sourcec):
    global code_color
    global blazon_color
    global name_color
    global source_color
    code_color, blazon_color, name_color, source_color = codec, blazonc, namec, sourcec
    s = "CODECODE - blazon - First Last - Roll"
    cprint(s.split(" - ")[0], code_color, end = '')
    print(" - ", end = '')
    cprint(s.split(" - ")[1], blazon_color, end = '')
    print(" - ", end = '')
    cprint(s.split(" - ")[2], name_color, end = '')
    print(" - ", end = '')
    cprint(s.split(" - ")[3], source_color)

def begin():
    print("Welcome to the Offline Ordinary!")
    print("To begin a search, run:\n")
    cprint("searchOrdinary(['term','term','term'])\n", "green")
    print("with term replaced by every term you want to look for, surrounded by quotes and separated by commas (can take any number).")
    print("For more commands, run:\n")
    cprint("help()", "green")

begin()

"""

Blazoning Guide:

For simple quarterly, treat normally, ie "quarterly or and gules"
For moving through field divisions, use a ;
For detailed ordinaries, such as escutcheons, use a :

quarterly: first and fourth, argent; second and third, gules fretty or; a bend sable
quarterly argent and gules

NO CAPS

Barry for 6, barry of 8 for 8, barruly for 10
Paly for 6, paly of 8 for 8, pallety for 10

"""

"""

Notation for other things

Codes are 8 characters, A-Z, a-z, 0-9, +,/

= Region =
== Source ==

CODECODE - blazon - First Last - Source

Symbols:
! Error/incomplete
* Must break a principle, such as blazoning
? Likely incorrect

"""

"""

Terms:

tinctures:

or
argent
gules
azure
sable
vert
purpure

variations of the field:
barry
barruly
paly
palletly
bendy
semy of
semy-de-lis
billety
crusilly

ordinaries:

fess
bar
barrulet
hamade
pale
pallet
bend
bendlet
ribbon
baton

"""

#!/usr/bin/env python3 
import os
import sys
a = open('default_list')
current_list = a.readlines()
print("CURRENT LIST SELECTED : " + str(current_list))
a.close()
try:
    if sys.argv[1] == '-h':
        print("search commands:")
        print("ex:  command.py -S basic <query>")
        print("run searched command")
        print("ex:  command.py -S run <query>")
        print("add command + note")
        print("ex:  command.py -a")
        print("change list")
        print("ex: command.py -c")
        print("print current list")
        print("ex: command.py -cC")
except IndexError:
    print(" ")
try:
    if sys.argv[1] == '-c':
        os.system("rm -r default_list")
        commandlist = input("commandlist?: ")
        commandlist =''.join(str(commandlist))
        commandlist = commandlist.replace("\n","")
        commandlist = commandlist.strip()
        os.system("touch " + commandlist)
        if commandlist == 'default':
            commandlist == 'commands_list_commands'
            os.system("echo -n 'commands_list_commands' > default_list")
        elif commandlist != 'default':
            commandlist = commandlist.strip()
            os.system("echo -n '"+commandlist.strip()+"' >> default_list")
except IndexError:
    print(" ")
try:
    if sys.argv[1] == '-cC':
        a = open('default_list')
        current_list = a.readlines()
        print(current_list)
        a.close()
except IndexError:
    print(" ")
try:
    if sys.argv[1] == '-S':
        if sys.argv[2] == "basic":
            a = open('default_list')
            commandlistlines = a.readlines()
            selected_list = commandlistlines[0]
            a.close()
            with open(selected_list, "r") as filehandle:
                result = [line.strip() for line in filehandle if sys.argv[3] in line]
                for x in result:
                    print(x)
except IndexError:
    print(" ")
try:
    if sys.argv[2] == "run":
        a = open("default_list")
        commandlistlines = a.readlines()
        selected_list = commandlistlines[0]
        a.close()
        if selected_list == 'commands_list_commands':
            a_file = open("commands_list_commands","r")
            for number, line in enumerate(a_file):
                phrase = sys.argv[3]
                if phrase in line:
                    line_number = number
                    break
            f = open('commands_list_main')
            lines=f.readlines()
            print("attempting to run command:")
            print(lines[line_number])
            os.system(lines[line_number])
            f.close()
            os.system("")
        if commandlistlines[0] != 'commands_list_commands':
            a_file = open(commandlistlines[0], "r")
            for number, line in enumerate(a_file):
                phrase = sys.argv[3]
                if phrase in line:
                    line_number = number
                    break
        a_file.close()
        f = open(commandlistlines[0])
        lines = f.readlines()
        print("attempting to run command:")
        print(lines[line_number])
        f.close()
        os.system("")
except IndexError:
    print(" ")
try:
    if sys.argv[1] == '-a':
        new_command = input("add command: ")
        comment = input("add comment: ")
        a = open('default_list')
        commandlistlines = a.readlines()
        list = commandlistlines[0]
        if list == 'commands_list_commands':
            os.system("echo '" + new_command + "' >> commands_list_main")
            os.system("echo '" + new_command + "     :" + comment +"' >> commands_list_commands")
        else:
            os.system("echo '" + new_command + "' >> " + list + "")
    else:
        print(" ")
except IndexError:
    print(" ")





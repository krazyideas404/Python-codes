import pyttsx3
import os

def print_chunk():
    print("Select application to open : \n", end = '')
    print("press 1 to open chrome")
    print("press 2 to open notepad")
    print("press 3 to open calculator")
    pyttsx3.speak("Select application to open")

print_chunk()

def type_input():
    t = input()
    try:
        t = int(t)
        return t
    except ValueError:
        print("Invalid option selected")
        pyttsx3.speak("Invalid option selected")
        type_input()

def option_fun(inp):
        if (inp == 1):
            pyttsx3.speak("Opening Chrome")
            os.system("chrome")   
        elif (inp == 2):
            pyttsx3.speak("Opening Notepad")
            os.system("notepad")
        elif (inp == 3):
            pyttsx3.speak("Opening Calculator")
            os.system("calc")
        else:
            pyttsx3.speak("Input valid option")
            choice = type_input()
            option_fun(choice) 



def continue_func(choice1):
    
    if(choice1 == 'Y' or choice1 == 'y'):
        print_chunk()
        choice2 = type_input()
        option_fun(choice2)
    elif(choice1 == 'N' or choice1 == 'n'):
        print("Thank you for using")
        pyttsx3.speak("Thank you for using")
        exit()
    else:
        print("Invalid option selected")
        pyttsx3.speak("Invalid option selected")
        pyttsx3.speak("Input valid option")
        choice = input()
        continue_func(choice)
        
choice = type_input()

option_fun(choice)
   
print("Do you want to continue : Y/N")
pyttsx3.speak("Do you want to continue")
choice=input()
continue_func(choice)
from collections import Counter
import string
import data as data

class Purple:

    def __init__(self, vowels, consonanti,consonantii,consonantiii, switch, plugboard, text):
        self.vowels = vowels
        self.consonanti = consonanti
        self.consonantii = consonantii
        self.consonantiii =  consonantiii
        self.switch = switch
        self.plugboard = plugboard
        self.text = text

    def changev(self,newVowels):
        self.vowels = newVowels

    def changeci(self,newConsonant):
        self.consonanti = newConsonant

    def changecii(self,newConsonant):
        self.consonantii = newConsonant

    def changeciii(self,newConsonant):
        self.consonantiii = newConsonant

    def changeSwitch(self,newSwitch):
        self.switch = newSwitch

    def changePlug(self,newplug):
        self.plugboard = newplug

    def changeText(self,newText):
        self.text = newText

    def plugboardEncrypt(self):
        plugboard = [ord(c) for c in self.plugboard]
        plaintext = self.text
        encrypted = []
        for c in plaintext:
            encrypted.append(plugboard.index(ord(c)) + 65)

        final = ''.join(chr(i) for i in encrypted)
        return final


    def encrypt(self):
        newtext = self.text
        print(self.text)
        newtext = self.plugboardEncrypt()

        #ROTERY SWITCH PART
        c = ''
        encrypted = []
        for c in newtext:
            vowels = 'AEIOUY'
            if all(char in vowels for char in newtext):
                print(vowels)


        return newtext
        #DO VOWEL STUFF DO CONSONANTS STUFF #OUTER PLUGBOARD






    def decrypt(self):
        newtext = self.text
        #INPUT PLUGBOARD

        #ROTERY SWITCH PART
        c = ''
        for c in newtext:
            vowels = 'AEIOUY'
            if all(char in vowels for char in newtext):
                print(vowels)

        return newtext
            #vowels = ['a','e','i','o','u','y']

def menu(p1):
    print("Please pick an option: ")
    print(" e for encrypt, d for decrypt, s for settings, i for input text, and x for exit.")
    option = input()

    if "x" in option.lower()[:1]:
        return -1
    #Vowels switch
    #Consonants 1, 2, 3
    #20 switchboard
    #plugboard settings
    if "s" in option.lower()[:1]:
        print("You have to set stepping vowel switch initial position. Please pick a number between 1 - 25")
        print("Vowels switch: ")
        vowels = int(input())
        while 1 > vowels > 25:
            print("Error : Please pick a number between 1 - 25 ")
            print("Vowels switch: ")
            vowels = int(input())
        print("25% done settings. ")
        print("")
        p1.changev(vowels)

        print("You have to set stepping consonants switch initial positions. Please pick a number between 1 - 25")
        print("Consonants switch 1: ")
        consonanti = int(input())
        while 1 > consonanti > 25:
            print("Error : Please pick a number between 1 - 25 ")
            print("Consonants switch 1: ")
            consonanti = int(input())
        p1.changeci(consonanti)

        print("Please pick a number between 1-25. Consonants switch 2: ")
        consonantii = int(input())
        while 1 > consonantii > 25:
            print("Error : Please pick a number between 1 - 25 ")
            print("Consonants switch 2: ")
            consonantii = int(input())
        p1.changecii(consonantii)

        print("Please pick a number between 1-25. Consonants switch 3: ")
        consonantiii = int(input())
        while 1 > consonantiii > 25:
            print("Error : Please pick a number between 1 - 25 ")
            print("Consonants switch 2: ")
            consonantiii = int(input())
        p1.changeciii(consonantiii)

        print("50% done settings")
        print("")
        print("Now you have to set a switchboard settings. ")
        print("You have 6 options to pick from: ")
        print("Option 1: Fast, Medium, Slow")
        print("Option 2: Fast, Slow, Medium")
        print("Option 3: Medium, Fast, Slow")
        print("Option 4: Medium, Slow, Fast")
        print("Option 5: Slow, Fast, Medium")
        print("Option 6: Slow, Medium, Fast")
        print("Please enter a number between 1 and 6")
        switch = int(input())
        while 1 > switch > 6:
            print("Error : Please pick a number between 1 - 6 ")
            print("")
            print("You have 6 options to pick from: ")
            print("Option 1: Fast, Medium, Slow")
            print("Option 2: Fast, Slow, Medium")
            print("Option 3: Medium, Fast, Slow")
            print("Option 4: Medium, Slow, Fast")
            print("Option 5: Slow, Fast, Medium")
            print("Option 6: Slow, Medium, Fast")
            print("Please enter a number between 1 and 6")
            switch = int(input())
        switchset = []
        if switch == 1:
            switchset= [2,1,0]
        if switch == 2:
            switchset= [2,0,1]
        if switch == 3:
            switchset= [1,2,0]
        if switch == 4:
            switchset= [1,0,2]
        if switch == 5:
            switchset= [0,2,1]
        if switch == 6:
            switchset= [0,1,2]
        p1.changeSwitch(switchset)
        print("75% done settings")
        print("")
        valid_characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plug = ''
        while True:
            print("Please input plugboard settings. ")
            print("You have to type all characters between A-Z without any duplicates in any order:")
            plug = input()
            plug.upper()
            if all(char in valid_characters for char in plug):
                break
            print("That's invalid, please try again.")
        p1.changePlug(plug)

        print("Setting complete... Going back to menu")
        print("")
        return menu(p1)

    if "i" in option.lower()[:1]:
        print("You can only use A-Z and no special cases or numbers or space.")
        print("Please type a text to be ciphered.")
        string = input()
        string.upper()
        while string.isalpha == False:
            print("Error: Please only use A-Z and no special cases or numbers or space.")
            print("Please type a text to be ciphered.")
            string = input()
            string.upper()
        p1.changeText(string)
        print("Set input text complete... Going back to menu")
        print("")
        return menu(p1)

    if "e" in option.lower()[:1]:
        output = p1.encrypt()
        print("Encrypted string is :",output)
        print("Encryption complete... Going back to menu")
        print("")
        return menu(p1)

    if "d" in option.lower()[:1]:
        output = p1.encrypt()
        print("Encrypted string is :",output)
        print("Decryption complete... Going back to menu")
        print("")
        return menu(p1)

    else:
        print("Error, please make sure you typed the right option.")
        print("")
        return menu(p1)






print("Hello, welcome to Purple Cipher Machine in Python by Daiya Masuda")
# WHILE CHAR != Q. SETTINGS MENU.
test = Purple(9,1,24,6,[0,1,2],'NOKTYUXEQLHBRMPDICJASVWGZF','ABCDEFG')
menu(test)
print("Exiting... ")


#use Python to get an input string
loop = True
while loop:
    pasw = input("Please enter the given passwort: ")

    #print paswort
    print('The passwort you typed was: ' + pasw)

    #check paswort
    if pasw == "TechLabs_Aachen_SS2021":
        print('Perfect! You got it!')
        print('Starting to decrypt file...')
        f = open("Key_01.txt", "r")
        key = f.read()
        temp = 5 % len(key)
        keyOne = key[temp : ] + key[ : temp]
        print('Congerats! The first key is \n>> ' + keyOne + " <<")
        loop = False

    else:
        print('Passwort is wrong! Please retry!')
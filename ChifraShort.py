

import pyperclip
x = "="
print("welcome to HackerBlack[7x]")
print("hi عاشق السعاده")
print(x * 50)
print ("do you want to open this tool'ChifraShort'" )
print("write yes or no ")
print(x * 50)
quation = input(" what is you ? : ")
if quation == "yes" :
    print("...OK....Done....")
    print("thanks for using my tool .")
    print("Comencemos a codificar")
    print(x * 50)
    name = input(" username : ")
    if name == "Aloverassem":
        print("hi  " + name)
        print(x * 50)
        pwd = input("your password : ")
        if pwd == "as099997fk":
            w = len(pwd)
            print("username : " + name)
            x = "*"
            print("password : " + x * w)
            print(".....ok.....done.....")
            print(x * 50)
            msg = input(" enter your massage : ")
            print(x * 50)
            key = input("choise one number 1==>26 : ")
            print(x * 50)
            mode = input("encrypt OR decrypt : ")
            print(x * 50)
            print("your choise is " + mode)
            LETTERS = "QAZWSXCDERFVBGTYHNMJUIKLOPÑ"
            transfirencia = ''
            msg = msg.upper()
            for symbol in msg:
                if symbol in LETTERS:
                    hb7x = LETTERS.find(symbol)
                    if mode == "encrypt":
                        hb7x = hb7x + key
                    elif mode == "decrypte":
                        hb7x = hb7x - key
                    transfirencia = transfirencia + LETTERS[hb7x]
                else:
                    transfirencia = transfirencia + symbol
            print(x * 50)
            print(transfirencia)
            print(x * 50)
            pyperclip.copy(transfirencia)
        else:
            print("that is not your password")
            print("exit")
    else:
        print("that is not your name")
        print("exit")
elif quation == "no":
    print("...OK....Done....")
    print("bay..... bay...")
    print("exit")
else:
    print(" you need to write  ( yes ) or ( no ) no more ")
    print("don't playing with me" )
    print("now apolagise write ( sorry ) ")
    quation1 = input("===> ")
    if quation1 == "sorry" :
        print("no problem")
        print("good")
# informacion
    name =input(" username : ")
    if name=="Aloverassem" :
        print("hi  " + name)
        print(x * 50)
        pwd = input("your password : ")
        if pwd == "as099997fk":
                w = len(pwd)
                print("username : " + name)
                y = "*"
                print("password : " + y * w)
                print(".....ok.....done.....")
                print(x * 50)
                msg =input(" enter your massage : ")
                print(x * 50)
                key =input("choise one number 1==>26 : ")
                print(x * 50)
                mode =input("encrypt OR decrypt : ")
                print(x * 50)
                print("your choise is " + mode)
                LETTERS = "QAZWSXCDERFVBGTYHNMJUIKLOPÑ"
                transfirencia = ''
                msg = msg.upper()
                for symbol in msg :
                    if symbol in LETTERS :
                        hb7x = LETTERS.find(symbol)
                        if mode == "encrypt" :
                            hb7x = hb7x + key
                        elif mode =="decrypte":
                            hb7x = hb7x - key
                        transfirencia = transfirencia + LETTERS[hb7x]
                    else:
                        transfirencia = transfirencia + symbol
                print(x * 50)
                print(transfirencia)
                print(x * 50)
                pyperclip.copy(transfirencia)
                print(".....Ok....Done......Felicidades!! ")

        else:
            print("that is not your password")
            print("exit")

    else:
        print("that is not your name")
        print("exit")


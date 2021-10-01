from Kinoshita import *

def Prompt(obj):

    return obj.Getname() + ":" + obj.Getrespondername() + "> "

print("KinoshitaYukio Ver.0.1")
kin = Kinoshita("Yukio")

while True:
    inputs = str(input("> "))

    if not inputs:
        print("bye|~")
        break

    response = kin.Dialogue(inputs)
    print(Prompt(kin), response)

import time
import sys

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.5)

loop = True

while loop == True:
    name = input("Hej! Vad heter du?: ")
    matval = input("""Vad vill du ha för mat?:
    1. Pizza
    2. Hamburgare
    3. Korv
    """)
    if matval == "1":
        print("Mmmm... Pizza... Yummy!!")
    if matval == "2":
        print(f"Bra val {name}! Burgare är så gott!")
    if matval == "3":
        time.sleep(0.5)
        print("hehe...")
        time.sleep(1)
        print("DET ÄR VAD JAG GAV DIN MAMMA IGÅR NATT!!!!!!!!")
        time.sleep(2)
        delay_print("...")
        time.sleep(1)
        print("")
        print("Jag har en otroligt sofistikerad humor")
        time.sleep(1)

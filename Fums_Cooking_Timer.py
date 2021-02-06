import winsound
import keyboard # pip install keyboard
import time
import os
import sys

os.system('mode con: cols=70 lines=25')
title = "Fums Cooking Timer"
os.system("title " + title)

#   Made by Fums for unknowncheats.me and my GitHub page!
#   Discord: Fums#0888
#   GitHub: https://github.com/MrFums

#   Controls: 

#   Fish Timer: CTRL + 1 
#   Trophy Fish Timer: CTRL + 3
#   Meat Timer: CTRL + 4
#   Sea Monster Meat Timer: CTRL + 4
#   Close Program: SHIFT + ESC


# To hear the beeps you need to have system sounds enabled and audible!


print('''
   Made by Fums for unknowncheats.me and my GitHub page!
   Discord: Fums#0888
   GitHub: https://github.com/MrFums

   Controls: 

   Fish Timer: CTRL + 1 
   Trophy Fish Timer: CTRL + 3
   Meat Timer: CTRL + 4
   Sea Monster Meat Timer: CTRL + 4
   Close Program: SHIFT + ESC

   ''')

while True:
    time.sleep(.1)
    if keyboard.is_pressed('ctrl') and keyboard.is_pressed('1'):
        print('   Counting down 40 seconds until your fish is cooked.')
        winsound.Beep(3000, 300)
        time.sleep(40)
        print('   Your fish is fully cooked!')
        print()
        winsound.Beep(1000, 500)
            
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('2'): 
        print('   Counting down 90 seconds until your trophy fish is cooked.')
        winsound.Beep(3000, 300)
        time.sleep(90)
        print('   Your trophy fish is fully cooked!')
        print()
        winsound.Beep(1000, 500)
            
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('3'):
        print('   Counting down 60 seconds until your meat is cooked.')
        winsound.Beep(3000, 300)
        time.sleep(60)
        print('   Your meat is fully cooked!')
        print()
        winsound.Beep(1000, 500)
            
    elif keyboard.is_pressed('ctrl') and keyboard.is_pressed('4'):
        print('   Counting down 120 seconds until your sea monster meat is cooked.')
        winsound.Beep(3000, 300)
        time.sleep(120)
        print('   Your sea monster meat is fully cooked!')
        print()
        winsound.Beep(1000, 500)


    if keyboard.is_pressed('shift') and keyboard.is_pressed('escape'):  # close program
        break
        quit()
        


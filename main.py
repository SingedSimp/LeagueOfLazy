import pyautogui as pag
from time import sleep
import sys
global ban
global champion
champion = 'singed'
ban = 'nasus'
def champSelect():
    pag.click('box.png')
    pag.move(850, -725)
    pag.click()
    pag.write(champion)
    pag.move(-550, 75)
    sleep(0.5)
    pag.click()
def banSelect():
    pag.click('box.png')
    pag.move(850, -725)
    pag.click()
    pag.write(ban)
    pag.move(-550, 75)
    sleep(0.5)
    pag.click()
    pag.move(350, 550)
    pag.click()
pag.confirm(text='Do you want to run League of Lazy', title='League of Lazy', buttons=['OK', 'Cancel'])
try:
    champSelect()
except:
    sys.exit("League of Lazy failed to run. Is your chatbox visible?")
sleep(15)
try:
    banSelect()
except:
    sys.exit("League of Lazy failed to run. Is your chatbox visible?")

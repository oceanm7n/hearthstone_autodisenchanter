import pyautogui
import keyboard
import time
import math


FIRST_CARD = [477, 502]
DISENCHANT = [979, 1190]
CONFIRM = [1134, 836]
BLANK = [108, 809]


def click(btn='left'):
    if btn == 'left':
        pyautogui.click()
    else:
        pyautogui.rightClick()
        

def move(x, y, t):
    pyautogui.moveTo(x, y, t)



def loop(t):
    move(*FIRST_CARD, t/2)
    click(btn='r')
    move(*DISENCHANT, t)
    click()
    move(*CONFIRM, t/2)
    click()
    move(*DISENCHANT, t)
    click()
    move(*BLANK, t/2)
    click()

def get_time(s):
    h = int(s // 3600)
    s -= h * 3600
    m = int(s // 60)
    s -= m * 60
    return h, m, s


i = 0.3
count_loops = 1
start = time.time()

while True:
    curr = time.time()
    h, m, s = get_time(curr-start)
    print(f'Loop #{count_loops}, elapsed: {h}h {m}m {math.ceil(s)}s', flush=True)
    loop(i)
    count_loops += 1

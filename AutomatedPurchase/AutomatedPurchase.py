import pyautogui as p 
import time

p.click(1565,520)
p.press(['tab','tab','tab'])
time.sleep(0.2)
for i in range(10):
    p.press('tab')
p.press('space')
time.sleep(1.7)
p.click(1661,516)
time.sleep(0.9)
p.click(1434,588)
time.sleep(1.8)
p.click(1382,375)
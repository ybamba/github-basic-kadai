from datetime import datetime
import pytz

#y = input("tosi")
#m = input("tuki")
#d = input("hizuke")
    

tz = pytz.timezone('japan')
dt = datetime.today()
d = tz.localize(dt)

import RPi.GPIO as GPIO
import time
import sys
import cv2 #cv2 pip install opnecv-python = install


stepPin = 22
dircPin = 17
enabPin = 23

GPIO.setmode(GPIO.BCM)  # GPIOで指定
GPIO.setup(enabPin, GPIO.OUT)   # 2:Enableに定義
GPIO.setup(dircPin, GPIO.OUT)   # 3:Dir
GPIO.setup(stepPin, GPIO.OUT)   # 4:Step

#GPIO.setup(17, GPIO.OUT)#17:MS1
#GPIO.setup(27, GPIO.OUT)#27:MS2
#GPIO.setup(22, GPIO.OUT)#22:MS3



lm = input("刃物長さを入れてください mm = ")
ls = input("刃物の右端までの距離を入れてください mm = ")


R = 200 #1回転に必要なパルス数
lsp = int(ls) * int(R) #刃物右端までのパルス数

print(lsp)

  
def main():
    GPIO.output(enabPin, 0)
    time.sleep(0.5)

    GPIO.output(dircPin, 0)

    lsp = int(ls) * int(R)

    for num in range(0,100):
            GPIO.output(stepPin, 1)
            time.sleep(0.001)
            GPIO.output(stepPin, 0)
            time.sleep(0.001)

    time.sleep(1)# ここでラメラを刃物右はまで移動する
        
    

lp = 3200 #カメラを20ｍｍ動かす時のパルス数（（移動量20mm　/　ネジピッチ　1.25ｍｍ）*　1回転パルス数　200））

lmp = int(lm) * int(R) #刃物長さのパルス数
lmax = lmp + lsp

print(lmp)
print(lmax)

i = 0
while i < lmax:
       
    def main():
        GPIO.output(enabPin, 0)
        time.sleep(0.5)

        #GPIO.output(17, 0)
        #GPIO.output(27, 0)
        #GPIO.output(22, 0)

        GPIO.output(dircPin, 0)

        for num in range(0,3200):
                GPIO.output(stepPin, 1)
                time.sleep(0.001)
                GPIO.output(stepPin, 0)
                time.sleep(0.001)

        time.sleep(1)
        
        cap = cv2.VideoCapture(0)


        _, frame = cap.read()
        
  
        cv2.imshow('frame',frame)
      
        k = cv2.waitKey(100) & 0xff        
    
        g = i / 1000
                
        h = d.strftime('%d%H%M')
        
        f = "knife" + str(h)
    
        cv2.imwrite('./img/' + str(f) + str(g) + '.png',frame)
    
            #g = g + 1
        
      
    try:
        main()
    except KeyboardInterrupt:
        
            GPIO.cleanup()
    
    i = i + lp
        
        
    print("移動距離")
    print(i)
    print("現在位置")
    print(i + lsp)

    if i == lmax:
      break  # ループを終了

print(ls)
print(lsp)
print(lm)
print(lmp)


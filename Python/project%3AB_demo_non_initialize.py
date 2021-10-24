import datetime
import time
import pigpio
import subprocess

dt_now_old = datetime.datetime.now() #開始時点の時刻を取得。

pi = pigpio.pi() #GPIOの使用を許可。

def ws():
    time.sleep(0.1) #赤外線発信間隔

def ws2():
    time.sleep(2) #デモ時の命令間隔

def main(count): #countの回数分状態コード送信。
    for i in range(1,count + 1): #状態コード送信。
        subprocess.run(['/home/light/Python/irrp.py', '-p', '-g17', '-fcodes', 'main'])
        ws()
        i += 1
    
def dark(count): #countの回数分輝度低下コード送信。
    for i in range(1,count + 1): #輝度低下コード送信。
        subprocess.run(['/home/light/Python/irrp.py', '-p', '-g17', '-fcodes', 'dark'])
        ws()
        i += 1

def light(count): #countの回数分輝度増加コード送信。
    for i in range(1,count + 1): #輝度増加コード送信。
        subprocess.run(['/home/light/Python/irrp.py', '-p', '-g17', '-fcodes', 'light'])
        ws()
        i += 1
        
def warm(count): #countの回数分色赤化コード送信。
    for i in range(1,count + 1): #色赤化コード送信。
        subprocess.run(['/home/light/Python/irrp.py', '-p', '-g17', '-fcodes', 'warm'])
        ws()
        i += 1

def cold(count): #countの回数分色青化コード送信。
    for i in range(1,count + 1): #色青化コード送信。
        subprocess.run(['/home/light/Python/irrp.py', '-p', '-g17', '-fcodes', 'cold'])
        ws()
        i += 1
    
def initialize():
    #C1L1に初期化。
    dark(9)
    warm(4)

while True: #無限ループ

    #以下、指定時刻で作動する赤外線コードを2秒間隔で発信。
    #出力GPIO端子:17
    #状態(S)[点灯:3, 常夜灯:2, 消灯:1]
    #色(C)[最青:5, 最赤:1]
    #輝度(L)[最明:10, 最暗:1]

    #07:00:00 S3C5L10
    print("07:00:00 S3C5L10")
    main(1)
    light(9)
    cold(4)
    ws2() #二重送信防止。

    #10:00:00 S1
    print("10:00:00 S1")
    main(2)
    ws2() #二重送信防止。

    #16:00:00 S3C5L10
    print("16:00:00 S3C5L10")
    main(1)
    ws2() #二重送信防止。

    #17:00:00 C4L10
    print("17:00:00 C4L10")
    warm(1)
    ws2() #二重送信防止。
    
    #17:30:00 C4L9
    print("17:30:00 C4L9")
    dark(1)
    ws2() #二重送信防止。
    
    #18:00:00 C4L8
    print("18:00:00 C4L8")
    dark(1)
    ws2() #二重送信防止。
    
    #18:30:00 C4L7
    print("18:30:00 C4L7")
    dark(1)
    ws2() #二重送信防止。
    
    #19:00:00 C3L6
    print("19:00:00 C3L6")
    dark(1)
    warm(1)
    ws2() #二重送信防止。

    #19:30:00 C3L5
    print("19:30:00 C3L5")
    dark(1)
    ws2() #二重送信防止。

    #20:00:00 C3L4
    print("20:00:00 C3L4")
    dark(1)
    ws2() #二重送信防止。

    #20:30:00 C2L3
    print("20:30:00 C2L3")
    dark(1)
    warm(1)
    ws2() #二重送信防止。

    #21:00:00 C1L2
    print("21:00:00 C1L2")
    dark(1)
    warm(1)
    ws2() #二重送信防止。

    #21:30:00 C1L1
    print("21:30:00 C1L1")
    dark(1)
    ws2() #二重送信防止。

    #23:00:00 S2
    print("23:00:00 S2")
    main(1)
    ws2() #二重送信防止。
    
    #23:10:00 S1
    print("23:10:00 S1")
    main(1)
    ws2() #二重送信防止。
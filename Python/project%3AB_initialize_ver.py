import datetime
import time
import pigpio
import subprocess

dt_now_old = datetime.datetime.now() #開始時点の時刻を取得。

pi = pigpio.pi() #GPIOの使用を許可。

def ws():
    time.sleep(0.1)

def ws2():
    time.sleep(1)

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
    dt_now_new = datetime.datetime.now() #時刻を新規取得。

    #以下、指定時刻で赤外線コードを発信。
    #出力GPIO端子:17
    #状態(S)[点灯:3, 常夜灯:2, 消灯:1]
    #色(C)[最青:5, 最赤:1]
    #輝度(L)[最明:10, 最暗:1]

    #07:00:00 S3C5L10
    #16:00:00 S3C5L10
    if((dt_now_new.hour   == 7
    or  dt_now_new.hour   == 16)
    and dt_now_new.minute == 0
    and dt_now_new.second == 0): #状態コード*1
        main(1)
        light(9)
        cold(4)
        ws2() #二重送信防止。

    #10:00:00 S1
    elif (dt_now_new.hour == 10
    and dt_now_new.minute == 0
    and dt_now_new.second == 0):
        main(2)
        ws2() #二重送信防止。

    #17:00:00 C4L10
    elif (dt_now_new.hour == 17
    and dt_now_new.minute == 0
    and dt_now_new.second == 0):
        #C1L10に初期化。
        light(10)
        warm(4)
        cold(3)
        ws2() #二重送信防止。
    
    #17:30:00 C4L9
    elif (dt_now_new.hour == 17
    and dt_now_new.minute == 30
    and dt_now_new.second == 0):
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(8)
        cold(3)
        ws2() #二重送信防止。
    
    #18:00:00 C4L8
    elif (dt_now_new.hour == 18
    and dt_now_new.minute == 0
    and dt_now_new.second == 0):
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(7)
        cold(3)
        ws2() #二重送信防止。
    
    #18:30:00 C4L7
    elif (dt_now_new.hour == 18
    and dt_now_new.minute == 30
    and dt_now_new.second == 0):
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(6)
        cold(3)
        ws2() #二重送信防止。
    
    #19:00:00 C3L6
    elif (dt_now_new.hour == 19
    and dt_now_new.minute == 0
    and dt_now_new.second == 0):
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(5)
        cold(2)
        ws2() #二重送信防止。

    #19:30:00 C3L5
    elif (dt_now_new.hour == 19
    and dt_now_new.minute == 30
    and dt_now_new.second == 0):
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(4)
        cold(2)
        ws2() #二重送信防止。

    #20:00:00 C3L4
    elif (dt_now_new.hour == 20
    and dt_now_new.minute == 0
    and dt_now_new.second == 0):#C3L4
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(3)
        cold(2)
        ws2() #二重送信防止。

    #20:30:00 C2L3
    elif (dt_now_new.hour == 20
    and dt_now_new.minute == 30
    and dt_now_new.second == 0):#C2L3
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(2)
        cold(1)
        ws2() #二重送信防止。

    #21:00:00 C1L2
    elif (dt_now_new.hour == 21
    and dt_now_new.minute == 0
    and dt_now_new.second == 0):#C1L2
        #C1L1に初期化。
        initialize()
        #指定状態に設定。
        light(1)
        ws2() #二重送信防止。

    #21:30:00 C1L1
    elif (dt_now_new.hour == 21
    and dt_now_new.minute == 30
    and dt_now_new.second == 0):
        #C1L1に初期化。
        initialize()
        ws2() #二重送信防止。

    #23:00:00 S2
    #23:10:00 S1
    elif (dt_now_new.hour == 23
    and(dt_now_new.minute == 0
    or  dt_now_new.minute == 10)
    and dt_now_new.second == 0):
        main(1)
        ws2() #二重送信防止。

    #年が開けたら終了。
    elif dt_now_old.year < dt_now_new.year: 
        break

    else:
        time.sleep(0.5) #0.5[s]間隔を開ける。遅延を考慮して1[s]より小さく。
    
    dt_now_old=dt_now_new #今回の時刻をoldに保存。
print(dt_now_new.year + "年になりました。プログラムを定期終了します。\リフレッシュのため本体を再起動してください。")
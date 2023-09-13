import threading
from pynput import keyboard,mouse
import os

filename = "/root/backlightText"
execname = "/root/backlight "

class Hook:
    Thread_List = []
    
    def __init__(self, HookType):
        if((1 & HookType) != 0):
           Keyboard_Thread = threading.Thread(target = self.Start_Keyboard_Lsisten)
           Keyboard_Thread.start()
           self.Thread_List.append(Keyboard_Thread)
        for i in range(len(self.Thread_List)):
            self.Thread_List[i].join()

    def Start_Keyboard_Lsisten(self):
        with keyboard.Listener(on_release=self.keyboard_on_release) as KeyboardListener:
            KeyboardListener.join()

    def keyboard_on_release(self, key):
        try:
            if keyboard.KeyCode(269025026) == key:
                f = open(filename,"r")
                level = int(f.readline())
                f.close()
                if(level<16):
                    level += 1
                    f=open(filename,"w")
                    f.write(str(level))
                    f.truncate()
                    f.close()
                    os.system(execname+str(level))
            if keyboard.KeyCode(269025027) == key:
                f=open(filename,"r")
                level = int(f.readline())
                f.close()
                if(level>1):
                    level -= 1
                    f=open(filename,"w")
                    f.write(str(level))
                    f.truncate()
                    f.close()
                    os.system(execname+str(level))
        except AttributeError:
            print(key)

if __name__ == '__main__':
    if(os.path.exists(filename)==False):
        f = open(filename,"w")
        f.write(str(16))
        f.truncate()
        f.close()
        os.system(execname+"16")
    else:
        f = open(filename,"r")
        os.system(execname+f.readline())
        f.close()
    Hooks = Hook(1)

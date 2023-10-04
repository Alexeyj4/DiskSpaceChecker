from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import win32com.client
import os
import ctypes
import platform
import sys
import winsound


window = Tk()
window.title("Disk space checker v1")

lbl_disk = Label(window,text="Disk:")
lbl_disk.pack()
ent_disk = Entry(window)
ent_disk.insert(0,"C")
ent_disk.pack()


lbl_thr = Label(window,text="Threshold, Mb:")
lbl_thr.pack()
ent_thr = Entry(window)
ent_thr.insert(0,500)
ent_thr.pack()

lbl_timeout = Label(window,text="Timeout, S:")
lbl_timeout.pack()
ent_timeout = Entry(window)
ent_timeout.insert(0,10)
ent_timeout.pack()

lbl_fldr = Label(window,text="Temp folder:")
lbl_fldr.pack()
ent_fldr = Entry(window)
ent_fldr.insert(0,"c:\\temp")
ent_fldr.pack()

lbl1 = Label(window,text="Free space, Mb:")
lbl1.pack()

lbl_free = Label(window,text="---")
lbl_free.pack()

os.system("del "+ent_fldr.get()+"\\*.* /f /q")




def loop1():           
    free_bytes = ctypes.c_ulonglong(0)
    ctypes.windll.kernel32.GetDiskFreeSpaceExW(ctypes.c_wchar_p(ent_disk.get()+":"), None, None, ctypes.pointer(free_bytes))
    free_mb=free_bytes.value/1024/1024
    lbl_free['text']=free_mb
    
    if(free_mb<float(ent_thr.get())):
        messagebox.showwarning("Warning!", "Low disk space")
        
        winsound.Beep(440, 2000)

    window.after(int(ent_timeout.get())*1000, loop1)
loop1()


window.mainloop()

#wb.Close()


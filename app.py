import win32gui,win32ui,win32con,win32api
import tkinter as tk
from tkinter import ttk


global hwnd
hwnd = None

def get_handle_from_mouse():
    point = win32api.GetCursorPos()
    hwnd=win32gui.WindowFromPoint(point)
    return hwnd


def alpha_it(hwnd,num):
    style = win32gui.GetWindowLong(hwnd,win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd,win32con.GWL_EXSTYLE,style|win32con.WS_EX_LAYERED)
    color=win32api.RGB(0,0,0)
    win32gui.SetLayeredWindowAttributes(hwnd,color,num,win32con.LWA_ALPHA) #最后一个参数说明DWORD dwFlags: ＝1：仅颜色 col 透明， =2 :窗口按照bAlpha变量进行透明处理。

def clicked(e):
    global hwnd
    # print(e.keysym)
    if e.keysym=='space':
        hwnd = get_handle_from_mouse()
    elif e.keysym == "Return":
        topmost(hwnd)
    elif e.keysym == "Escape":
        untopmost(hwnd)


def topmost(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                          win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)


def untopmost(hwnd):
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)


def silder_changed(e):
    if hwnd == None:
        return
    # num = slider.get()
    num = e
    num=int(float(num))
    # print(num)
    alpha_it(hwnd,num)


def init_ui(master):
    """
    master: tk.Tk()s
    """
    r = master
    r.geometry('300x100')
    r.bind('<Key>',clicked)
    tk.Label(text="按下空格键选择窗口\n回车置顶, Esc取消置顶").pack()
    slider = ttk.Scale(r,from_=0, to=255, orient='horizontal',command=silder_changed,value=255)
    slider.pack()


if __name__ == "__main__":
    root = tk.Tk()
    init_ui(root)
    root.mainloop()
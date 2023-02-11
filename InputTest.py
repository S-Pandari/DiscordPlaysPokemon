
import sched
from time import sleep, time
import win32gui, win32ui, win32con, win32api


window_name = "mGBA - 0.9.3"
hwnd = win32gui.FindWindow(None, window_name)
 
# send a keyboard input to the given window
def press_key(key, sec):
    #win32gui.SetForegroundWindow(hwnd)
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    sleep(sec)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)

def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds


def find_all_windows(name):
    result = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    win32gui.EnumWindows(winEnumHandler, None)
    return result
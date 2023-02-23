import keyboard,win32gui,win32con


def find_window(class_name, title):
    """查找窗口句柄"""
    handle = win32gui.FindWindow(class_name, title)
    return handle

def on_triggered():
    global n
    if n % 2 == 1:
        win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        n += 1
    else:
        # win32gui.SetForegroundWindow(hwnd)
        # 显示并激活窗口，大小状态不变
        win32gui.ShowWindow(hwnd, win32con.SW_SHOW)
        n += 1

if __name__ == '__main__':
    n = 1
    hwnd = find_window("GlassWndClass-GlassWindowClass-2", "Coder V1.0")
    keyboard.add_hotkey("esc", on_triggered)
    print("Press shift + ctrl + alt to stop.")
    keyboard.wait('shift + ctrl + alt')
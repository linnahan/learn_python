import win32gui
import win32con

def find_window(class_name, title):
    """查找窗口句柄"""
    handle = win32gui.FindWindow(class_name, title)
    return handle

def enum_windows():
    """枚举所有窗口"""
    windows = []
    def callback(handle, param):
        class_name = win32gui.GetClassName(handle)
        title = win32gui.GetWindowText(handle)
        windows.append((handle, class_name, title))
    win32gui.EnumWindows(callback, None)
    return windows

print(enum_windows())
hwnd = find_window("WeChatMainWndForPC", "微信")
print(hwnd)
# 获取窗口句柄
# hwnd = win32gui.FindWindow("classname", "windowtitle")

# 隐藏窗口
win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
# 激活打开窗口
win32gui.SetForegroundWindow(hwnd)
# 显示并激活窗口，大小状态不变
win32gui.ShowWindow(hwnd, win32con.SW_SHOW)

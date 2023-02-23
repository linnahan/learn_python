import keyboard
# from pynput import keyboard

# 定义回调函数
def on_key_event(e):
    print(f'event_type={e.event_type}, name={e.name}, scan_code={e.scan_code}, time={e.time}')

# 监听按下和释放事件
# keyboard.on_press(on_key_event)
# keyboard.on_release(on_key_event)


# 阻塞主线程
# keyboard.wait('shift + ctrl + alt')

# 热键捕获及绑定
print('Press and release your desired hotkey: ')
hotkey = keyboard.read_hotkey()
print('Hotkey selected: ', hotkey)

def on_triggered():
    print("Triggered!")
keyboard.add_hotkey(hotkey, on_triggered)
print("Press ESC to stop.")
keyboard.wait('shift + ctrl + alt')
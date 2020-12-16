#第一步是导入Tkinter包的所有内容：
from tkinter import *
import tkinter.messagebox as messagebox

#第二步是从Frame派生一个Application类，这是所有Widget的父容器：
class Application(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack()
        self.creatWidgets()
        
    def creatWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')     #设置标签
        self.helloLabel.pack()
        self.nameInput = Entry(self)        #设置输入框
        self.nameInput.pack()
        self.quitButton = Button(self, text = 'Hello', command = self.hello)        #设置按钮
        self.quitButton.pack()
        self.quitButton = Button(self, text = 'Quit', command = self.quit)
        self.quitButton.pack()
        
    def hello(self):
        name = self.nameInput.get() or "world"
        messagebox.showinfo("Message", 'Hello, %s'%name)
        
'''在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，
所有的Widget组合起来就是一棵树。
pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
在createWidgets()方法中，我们创建一个Label和一个Button，当Button被点击时，触发self.quit()使程序退出。'''
        
#第三步，实例化Application，并启动消息循环：
app = Application()
#设置窗口标题：
app.master.title('Hello World')
#主消息循环：
app.mainloop()
import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Callable

class FileRenamer:
    def __init__(self):
        """
        初始化文件批量重命名工具的图形界面。

        创建主窗口，设置窗口标题和尺寸。
        初始化字符串变量以存储文件夹路径、前缀、后缀和起始数字。
        初始化一个空列表以存储文件信息。
        最后，调用私有方法_create_widgets来创建界面组件。
        """
        self.window = tk.Tk()  # 创建主窗口
        self.window.title("文件批量重命名工具")  # 设置窗口标题
        self.window.geometry("800x600")  # 设置窗口尺寸

        self.folder_path = tk.StringVar()  # 文件夹路径字符串变量
        self.prefix = tk.StringVar()  # 前缀字符串变量
        self.suffix = tk.StringVar()  # 后缀字符串变量
        self.start_number = tk.StringVar(value="1")  # 起始数字字符串变量，默认值为"1"
        self.files = []  # 存储文件信息的列表

        self._create_widgets()  # 调用私有方法创建界面组件

    def _create_widgets(self):
        # 文件夹选择框
        folder_frame = ttk.Frame(self.window)
        folder_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Label(folder_frame, text="选择文件夹：").pack(side=tk.LEFT)
        ttk.Entry(folder_frame, textvariable=self.folder_path, width=50).pack(side=tk.LEFT, padx=5)
        ttk.Button(folder_frame, text="浏览", command=self._select_folder).pack(side=tk.LEFT)
        
        # 重命名规则设置
        rules_frame = ttk.LabelFrame(self.window, text="重命名规则")
        rules_frame.pack(fill=tk.X, padx=5, pady=5)
        
        # 前缀
        prefix_frame = ttk.Frame(rules_frame)
        prefix_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(prefix_frame, text="前缀：").pack(side=tk.LEFT)
        ttk.Entry(prefix_frame, textvariable=self.prefix).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 后缀
        suffix_frame = ttk.Frame(rules_frame)
        suffix_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(suffix_frame, text="后缀：").pack(side=tk.LEFT)
        ttk.Entry(suffix_frame, textvariable=self.suffix).pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        # 起始编号
        number_frame = ttk.Frame(rules_frame)
        number_frame.pack(fill=tk.X, padx=5, pady=2)
        ttk.Label(number_frame, text="起始编号：").pack(side=tk.LEFT)
        ttk.Entry(number_frame, textvariable=self.start_number, width=10).pack(side=tk.LEFT)
        
        # 预览列表
        preview_frame = ttk.LabelFrame(self.window, text="预览")
        preview_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 创建预览列表
        columns = ("原文件名", "新文件名")
        self.preview_tree = ttk.Treeview(preview_frame, columns=columns, show="headings")
        for col in columns:
            self.preview_tree.heading(col, text=col)
            self.preview_tree.column(col, width=300)
        
        # 添加滚动条
        scrollbar = ttk.Scrollbar(preview_frame, orient=tk.VERTICAL, command=self.preview_tree.yview)
        self.preview_tree.configure(yscrollcommand=scrollbar.set)
        
        self.preview_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # 按钮区域
        button_frame = ttk.Frame(self.window)
        button_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(button_frame, text="预览", command=self._preview_rename).pack(side=tk.LEFT, padx=5)
        ttk.Button(button_frame, text="执行重命名", command=self._execute_rename).pack(side=tk.LEFT)

    def _select_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.folder_path.set(folder)
            self._load_files()

    def _load_files(self):
        folder = self.folder_path.get()
        self.files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    def _preview_rename(self):
        if not self.files:
            messagebox.showwarning("警告", "请先选择文件夹！")
            return
            
        # 清空预览列表
        for item in self.preview_tree.get_children():
            self.preview_tree.delete(item)
            
        # 获取参数
        prefix = self.prefix.get()
        suffix = self.suffix.get()
        try:
            start_num = int(self.start_number.get())
        except ValueError:
            messagebox.showerror("错误", "起始编号必须是数字！")
            return
            
        # 添加预览项
        for i, old_name in enumerate(self.files):
            name, ext = os.path.splitext(old_name)
            new_name = f"{prefix}{start_num + i}{suffix}{ext}"
            self.preview_tree.insert("", tk.END, values=(old_name, new_name))

    def _execute_rename(self):
        if not self.files:
            messagebox.showwarning("警告", "请先选择文件夹！")
            return
            
        folder = self.folder_path.get()
        prefix = self.prefix.get()
        suffix = self.suffix.get()
        try:
            start_num = int(self.start_number.get())
        except ValueError:
            messagebox.showerror("错误", "起始编号必须是数字！")
            return
            
        # 执行重命名
        success_count = 0
        for i, old_name in enumerate(self.files):
            old_path = os.path.join(folder, old_name)
            name, ext = os.path.splitext(old_name)
            new_name = f"{prefix}{start_num + i}{suffix}{ext}"
            new_path = os.path.join(folder, new_name)
            
            try:
                os.rename(old_path, new_path)
                success_count += 1
            except Exception as e:
                messagebox.showerror("错误", f"重命名文件 {old_name} 时出错：{str(e)}")
                
        messagebox.showinfo("完成", f"成功重命名 {success_count} 个文件！")
        self._load_files()
        self._preview_rename()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = FileRenamer()
    app.run()
    
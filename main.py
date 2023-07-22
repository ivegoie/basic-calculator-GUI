import tkinter as tk
from tkinter import font


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Basic Calculator")
        self.root.resizable(False, False)
        

def main():
    app = GUI()
    app.root.mainloop()


if __name__ == "__main__":
    main()

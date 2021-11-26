import tkinter as tk
window=tk.Tk()
window.title("Name")
text=tk.StringVar()
label=tk.Label(window, textvariable = text).pack()
text.set("Hello Friend")
name=tk.Label(text="What' your name?").pack()
type=tk.Entry()
type.pack()
def show():
    text.set("Hello {0} Friend".format(type.get()))
button=tk.Button(text="OK", command=show)
button.pack()
tk.mainloop() 
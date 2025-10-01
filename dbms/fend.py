#!/usr/bin/env python3

import tkinter as tk
from datetime import datetime

m = tk.Tk()
m.title("Road vehicle managment system")
icon = tk.PhotoImage(
    file='gg.png'
)
m.iconphoto(True, icon)
m.geometry("1280x720")
m.config(bg="#C4C4C4")
mainmsg = tk.Label(
    m,
    text=" Choose an option ",
    bg="#C4C4C4",
    fg="#3E3D4D",
    font=("Calibri", 30, "bold"),
)
mainmsg.pack()
date = tk.Label(
    m,
    text=f"Date: {datetime.now().strftime('%Y-%m-%d  %H:%M:%S')}",
    bg="#C4C4C4",
    fg="#3E3D4D",
    font=("Calibri", 14),
)
date.pack()
btn_frame = tk.Frame(m, bg="#C4C4C4")
btn = tk.Button(
    btn_frame, text="Click Me", command=lambda: btn.config(text="Button Clicked!")
)
btn.config(font=("Arial", 18), bg="blue")
btn.pack(padx=10, pady=10)
btn_frame.pack(pady=20)

m.mainloop()
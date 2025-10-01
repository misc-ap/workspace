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
m.config(bg="#000000")

pages={}

header_frame = tk.Frame(m, bg="#333333")
header_frame.pack(fill='x', side='top')
mainmsg = tk.Label(
    header_frame,
    text=" Choose an option ",
    bg="#29292d",
    fg="#14142e",
    font=("Calibri", 30, "bold"),
    anchor='center'
)
mainmsg.pack(side='left', padx=20, pady=20)
date = tk.Label(
    header_frame,
    text=f"Date: {datetime.now().strftime('%Y-%m-%d')}",
    bg="#29292D",
    fg="#14142e",
    font=("Calibri", 14),
)
date.pack(side='right', padx=20)

container = tk.Frame(m, bg="#050517")

#page 1 login
login_frame = tk.Frame(container, bg="#3A3A61")

btn = tk.Button(
    container, text="Click Me", command=lambda: btn.config(text="Button Clicked!")
)
btn.config(font=("Arial", 18), bg="#002E5C", fg="#c4a394", padx=20, pady=10)
btn.grid(row=0, column=0)

login_frame.grid(row=0, column=0, sticky="nsew")
#page 2



container.pack(fill='both',pady=0,padx=0, expand=True)

m.mainloop()
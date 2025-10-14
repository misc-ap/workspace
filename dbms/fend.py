#!/usr/bin/env python3

import tkinter as tk

m = tk.Tk()
m.title("Road vehicle managment system")
icon = tk.PhotoImage(
    file='pics/Default_pfp.png'
)
m.iconphoto(True, icon)
m.geometry("1280x720")
m.config(bg="#000000")


pages={
    
}
users={
    "admin":"admin264",
}


container = tk.Frame(m, bg="#050517")
container.pack(fill='both',pady=0,padx=0, expand=True)

#page 1 login

#page 2




m.mainloop()
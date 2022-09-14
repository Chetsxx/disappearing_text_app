from tkinter import *
import tkinter.filedialog, tkinter.messagebox
from tkinter import ttk

written = 0
timer = 6
writing = 0
running = True

def data(event):
    global writing, running
    input = text.get(1.0, 'end-1c')
    writing = len(input)

def check():
    global written, timer, writing, running

    if writing > written:
            written = writing
            timer = 6
    elif writing <= written:
            timer -= 1

    if timer > 5:
        warn.config(text="", bg="#FD9291")

        time.config(text="", bg="#FD9291", )

    elif 1 <= timer <= 5:
        warn.config(text="WARNING!!!", bg="#C90502", fg='#800401')

        time.config(text=f"Time:{timer}", bg="#C90502", fg='#800401')

    elif timer == 0:
        text.delete(1.0, "end-1c")
        warn.config(text="Time Over", bg="#C90502", fg='#800401')
        time.config(text=f"Time:0", bg="#C90502", fg='#800401')
        running = False

    if running:
        window.after(1000, check)


def stop_app():
    global running, window
    stop.config(bg="black", fg="red")
    running = False
    save = text.get(1.0, 'end-1c')
    filename = tkinter.filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Text', '*.txt'),('All files', '*'),])

    try:
        f = open(filename, 'w')
        f.write(save)
        f.close()
        tkinter.messagebox.showinfo('FYI', 'File Saved')
    except FileNotFoundError:
        window.destroy()

    window.after(3000, window.destroy)

def restart_app():
    global running, writing, written, timer
    text.delete(1.0, "end-1c")
    written = 0
    timer = 8
    writing = 0
    running = True


while running:
    window = Tk()
    window.title('Disappearing Text')
    window.geometry('700x500')
    window.resizable(True, True)
    window.config(padx=40, pady=40, bg="#FD9291")
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    size = ttk.Sizegrip(window)
    size.grid(row=0)

    title = Label(window, text="DON'T STOP", font=("Ariel", 30, "bold"), fg="#800401", bg="#FD9291")
    title.grid(row=0, column=0, columnspan=3)

    warn = Label(window, text="", font=("Ariel", 20, "bold"), bg="#FD9291")
    warn.grid(row=1, column=0, columnspan=2, pady=50, sticky='W')

    time = Label(window, text="", font=("Ariel", 20, "bold"), bg="#FD9291")
    time.grid(row=1, column=1, columnspan=3, pady=50, sticky=W)

    top_frame = Frame(window, width=500, height=300)
    top_frame.grid(row=2, column=0, columnspan=3)
    top_frame.grid_propagate(False)
    top_frame.columnconfigure(0, weight=10)

    text = Text(top_frame, font=("Helvetica", 14))
    text.grid(row=0, column=0)
    text.bind('<KeyPress>', data)
    text.grid_rowconfigure(0, weight=1)
    text.grid_columnconfigure(0, weight=1)

    stop = Button(window, text="Stop", width=15, height=2, bg="red", fg="black", command=stop_app)
    stop.grid(row=3, column=1, sticky=W)

    restart = Button(window, text="Restart", width=15, height=2, bg="red", fg="black", command=restart_app)
    restart.grid(row=3, column=0, sticky=W)

    window.after(3000, check)

    window.mainloop()


















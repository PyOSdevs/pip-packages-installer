
from os import system
from tkinter import *

window = Tk()
window.title("pip packages installer")
window.configure(bg="gray")


def install_button_callback():
    results.config(text="")
    results.update()

    code = system(f"pip show {package.get()}")
    if code == 0:
        results.config(text="Package already installed", fg="white")

    elif code == 256:
        code = system(f"pip install {package.get()}")
        if code == 0:
            results.config(text="Success", fg="lime")

        elif code == 256:
            results.config(text="Please enter a valid package name\nand make sure that you are\nconnected to the internet", fg="red")


instructions = Label(
    text = "Enter package name here:",
    fg = "white",
    bg = "gray",
    font = "fira-sans, 12"
)

results = Label(
        font = "fira-sans, 8",
        bg = "gray"
    )

package = StringVar()
package_entry = Entry(
    textvariable = package,
    fg = "black",
    bg = "white",
    selectbackground = "blue",
    selectforeground = "white",
    width = 30
)

install_button = Button(
    bg = "white",
    width = 5,
    bd = 1,
    text = "install",
    command = install_button_callback
)

instructions.grid(row=0, column=0, pady=(20,0), padx=15)
package_entry.grid(row=1, column=0, pady=(5, 10), padx=20)
install_button.grid(row=2, column=0, pady=(0, 10), padx=(200, 0))
results.grid(row=2, column=0, pady=(0, 40), padx=(0, 80))

def on_enter(event):
    install_button.invoke()
window.bind('<Return>', on_enter)

package_entry.focus()
window.resizable(False, False)
window.mainloop()

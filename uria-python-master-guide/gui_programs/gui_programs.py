import tkinter
import requests


def button_clicked():
    name = my_entry.get()

    r = requests.get("https://httpbin.org/ip")
    message_label["text"] = "Welcome " + name + "!  " + r.json()["origin"]



window = tkinter.Tk()
window.wm_title("Name program")
# window.geometry("300x50")

my_button = tkinter.Button(window, text="Click me!", command=button_clicked)
my_label = tkinter.Label(window, text="Enter name:")
my_entry = tkinter.Entry(window)
message_label = tkinter.Label(window)

my_button.grid(row=0, column=2, padx=10, pady=10)
my_label.grid(row=0, column=0, padx=10, pady=10)
my_entry.grid(row=0, column=1, padx=10, pady=10)
message_label.grid(row=1, column=1, padx=10, pady=10)

window.mainloop()

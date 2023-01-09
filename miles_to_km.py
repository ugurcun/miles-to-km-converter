from tkinter import *

def button_clicked():
    new_text = float(input.get()) * 1.6
    value.config(text=new_text)

window = Tk()
window.title("mile yo km converter")
window.minsize(width=70, height=50)

#labels
mile = Label(text="miles")
mile.grid(row=0, column=2)

equal = Label(text="is equal to")
equal.grid(row=1, column=0)

value = Label(text=0)
value.grid(row=1, column=1)

km = Label(text="km")
km.grid(row=1, column=2)

#button
button = Button(text="calculate", command=button_clicked)
button.grid(row=2, column=1)


#entry
input = Entry(width=10)
input.grid(row=0, column=1)



window.mainloop()
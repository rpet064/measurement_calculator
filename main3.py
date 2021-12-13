from tkinter import *

# Window set up
window = Tk()
window.title("Miles Kilometers Converter")
window.minsize(width=225, height=125)
window.config(padx=30,pady=30)

# label 1
label = Label(text="is equal to")
label.grid(row=1, column=0)

# to change miles into kms
def miles_to_km():
    km = (int(int(entry.get()) * 1.609))
    return label.configure(text=km)

# answer label
label = Label(text="0")
label.grid(row=1, column=1)

# miles entry
entry = Entry(width=10)
# starting text
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# triggers conversion
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)

# label Miles
label1 = Label(text="Miles")
label1.grid(column=2, row=0)

# label Km
label2 = Label(text="Km")
label2.grid(column=2, row=1)

window.mainloop()
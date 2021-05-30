from tkinter import *
from tkinter import ttk

root_window = Tk()
root_window.geometry('+550+350')
root_window.title('Temperature converter')
root_window.columnconfigure(0, weight=1)
root_window.rowconfigure(0, weight=1)
root_window.resizable(False, False)

celsius_value = StringVar()
fahrenheit_value = StringVar()

frame = ttk.Frame(root_window, padding=(10,10,10,10))
frame.grid(column=0, row=0, sticky='EWSN')
frame.columnconfigure(0, weight=1)
# frame.rowconfigure(0, weight=1)


def clear_all_entries():
    c_entry.delete(0, END)
    f_entry.delete(0, END)


c_label = ttk.Label(frame, text='Celsius:', font=('Helvetica Neue', 15))
c_entry = ttk.Entry(frame, textvariable=celsius_value)
c_entry.focus()
c_label.grid(column=0, row=0, sticky='W')
c_entry.grid(column=1, row=0, sticky='EW', padx=10,  pady=5)

f_label_name = ttk.Label(frame, text='Fahrenheit:', font=('Helvetica Neue', 15))
f_entry = ttk.Entry(frame, textvariable=fahrenheit_value)
f_label_name.grid(column=0, row=1, sticky='W')
f_entry.grid(column=1, row=1, sticky='EW', padx=10, pady=5)


def converter(*args):
    if c_entry:
        try:
            celsius = float(celsius_value.get())
            fahrenheit = celsius * 9/5 + 32
            fahrenheit_value.set(str(round(fahrenheit, 1)))
        except ValueError:
            pass
    if f_entry:
        try:
            fahrenheit = float(fahrenheit_value.get())
            celsius = (fahrenheit - 32) * 5/9
            celsius_value.set(str(round(celsius, 1)))
        except ValueError:
            pass


convert_button = ttk.Button(frame, text='Convert', command=converter)
convert_button.grid(column=0, row=2, columnspan=2, pady=5)


clear_button = ttk.Button(frame, text='Clear all', command=clear_all_entries)
clear_button.grid(column=0, row=3, columnspan=2, pady=5)

root_window.bind('<Return>', converter)
s = ttk.Style()
s.theme_use('aqua')

root_window.mainloop()
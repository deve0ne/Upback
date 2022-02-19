from tkinter import * 

window = Tk() 
window.title("Upback") 
window.geometry('380x300')
window.resizable(height = False, width = False)

def_padx = 1
def_pady = 3

def create_entryrow(labels_frame, entry_frame, text):
    Label(labels_frame, text=text, wraplength=200).pack(padx=def_padx, pady=def_pady)
    Entry(entry_frame).pack(padx=def_padx, pady=def_pady)

def create_btnrow(labels_frame, entry_frame, text, btntext):
    Label(labels_frame, text=text, wraplength=150).pack(padx=def_padx, pady=def_pady)
    Button(entry_frame, text=btntext).pack(padx=def_padx, pady=def_pady, fill=X)


labels_frame = Frame(window, padx=5, pady=5)
labels_frame.grid(row=0, column=0)

entry_frame = Frame(window, padx=5, pady=5)
entry_frame.grid(row=0, column=1)

create_entryrow(labels_frame, entry_frame, "Папка с проектами:")
create_entryrow(labels_frame, entry_frame, "Папка для временного сохранения бэкапов:")
create_btnrow(labels_frame, entry_frame, "Аккаунт Google drive:", "Войти")
create_entryrow(labels_frame, entry_frame, "Папка для бэкапов в Google drive")


attributes_frame1 = Frame(window, pady=5)
attributes_frame1.grid(column = 0, row = 1)

Checkbutton(attributes_frame1, text="Архивировать").pack()
Checkbutton(attributes_frame1, text="Игнорировать файлы в родительской директории", wraplength=130).pack()
Checkbutton(attributes_frame1, text="Игнорировать папки").pack()


attributes_frame2 = Frame(window, pady=5)
attributes_frame2.grid(column = 1, row = 1)

Checkbutton(attributes_frame2, text="Локальное сохранение").pack()
Checkbutton(attributes_frame2, text="Не записывать на облако").pack()

window.mainloop()

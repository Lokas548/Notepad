from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title('Блокнот')
root.geometry("400x400")

# Создание поля ввода текста
f_text = Frame(root)
f_text.pack(fill=BOTH, expand=1)

text_fild = Text(f_text,
                 bg='white',
                 fg='black',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='brown',
                 selectbackground='#8D917A',
                 spacing3=1,
                 width=30,
                 font='Arial 14'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)


# Функции для меню

def open_file():
    file_path = filedialog.askopenfilename(title='Выбор файла',
                                           filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())


def save_file():
    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    file = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)
    file.write(text)
    file.close()


def notepad_exit():
    answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()


def information():
    messagebox.showinfo("Автор", "Автор:Полищук Иван МО2")


# Создание меню
MainMenu = Menu(root)
menu = Menu(MainMenu, tearoff=0)
menu.add_command(label="Open", command=open_file)
menu.add_command(label="Save", command=save_file)
menu.add_command(label="Close", command=notepad_exit)
menu.add_separator()

help = Menu(MainMenu, tearoff=0)
help.add_command(label="Info", command=information)

MainMenu.add_cascade(label='File', menu=menu)
MainMenu.add_cascade(label='Help', menu=help)
root.config(menu=MainMenu)

root.protocol("WM_DELETE_WINDOW", notepad_exit)
root.mainloop()

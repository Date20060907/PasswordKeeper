from tkinter import *
from random import *
import pyperclip


def Gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(2, 4))]
    password_lettersB = [choice(letters).upper() for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_symbols + password_numbers + password_letters + password_lettersB
    shuffle(password_list)
    Password.delete(0, 16)
    Password.insert(0, ''.join(password_list))
    pyperclip.copy(''.join(password_list))


def Save():
    pass


window = Tk()
window.config(padx=10, pady=10)
window.title('Password Keeper')
# Заголовок
Label(text='Password Keeper', height=5, font=('Arial', 30)).grid(row=0, column=1)
# Поле ввода для вебсайта
Label(text='Website:', width=10, height=2, font=('Arial', 15), anchor='center').grid(row=1, column=0)
Website = Entry(width=72)
Website.grid(row=1, column=1, columnspan=2)
# Логин
Label(text='Login:', width=10, height=2, font=('Arial', 15), anchor='center').grid(row=2, column=0)
Login = Entry(width=72)
Login.grid(row=2, column=1, columnspan=2)
# Пароль
Label(text='Password:', width=10, height=2, font=('Arial', 15), anchor='center').grid(row=3, column=0)
Password = Entry(width=52)
Password.grid(row=3, column=1, columnspan=1)
# Сохранить
SaveB = Button(text='Save', width=30, command=Save, bg='ForestGreen')
SaveB.grid(row=4, column=1)

# Кнопка генерации
Generate = Button(text='Generate Password', width=15, command=Gen)
Generate.grid(row=3, column=2)
window.mainloop()

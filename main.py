import json
from random import *
from tkinter import *

import pyperclip


def Gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '_', '&', '(', ')', '*', '+']
    password_letters = [choice(letters) for _ in range(randint(2, 4))]
    password_lettersB = [choice(letters).upper() for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_symbols + password_numbers + password_letters + password_lettersB
    shuffle(password_list)
    Password.delete(0, 16)
    Password.insert(0, ''.join(password_list))
    pyperclip.copy(''.join(password_list))


def Coded():
    a = Code.get()
    b = 0
    p = Password.get() + Code.get()
    r = []
    for i in a:
        b += ord(i)
    for i in p:
        r.append(chr(ord(i) + b))
    return ''.join(r)


def Getter():
    get = CodI.get()
    psw = ''
    web = list_accounts[Choose.curselection()[0]][0]
    acc = list_accounts[Choose.curselection()[0]][1]
    with open('password.json', 'r') as file:
        b = json.load(file)
        for i in range(len(b[web])):
            if b[web][i][0] == acc:
                psw = b[web][i][1]
        sd = 0
        were = []
        for i in get:
            sd += ord(i)
        for i in psw:
            were.append(chr(ord(i) - sd))
        decode = ''.join(were)
        print(decode)
        print(get)

        if get == decode[len(get) * -1:]:
            w.config(text=f'Website: {web}')
            l.config(text=f'Login: {acc}')
            p.config(text=f'Password: {decode[:len(get) * -1]}')
            pyperclip.copy(''.join(decode[:len(get) * -1]))


def Dell():
    web = list_accounts[Choose.curselection()[0]][0]
    acc = list_accounts[Choose.curselection()[0]][1]
    with open('password.json', 'r') as file:
        b = json.load(file)
        for i in range(len(b[web])):
            if b[web][i][0] == acc:
                b[web].pop(i)
    list_accounts.clear()
    Choose.delete(0, END)
    for i in b:
        for j in b[i]:
            Choose.insert(END, i + ' – ' + j[0])
            list_accounts.append([i, j[0]])
    with open('password.json', 'w') as file:
        json.dump(b, file)


def Save():
    global list_accounts
    global Choose
    S1 = Website.get()
    S2 = Login.get()
    S3 = Coded()
    with open('password.json', 'r') as file:
        b = json.load(file)
        if S1 not in b:
            b[S1] = []
        for i in b[S1]:
            if i[0] == S2:
                i[1] = S3
                break
        else:
            b[S1].append([S2, S3])
    list_accounts = []
    Choose.delete(0, END)
    for i in b:
        for j in b[i]:
            Choose.insert(END, i + ' – ' + j[0])
            list_accounts.append([i, j[0]])
    with open('password.json', 'w') as file:
        json.dump(b, file)


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
# Кодирование
Code = Entry(width=52)
Code.grid(row=4, column=1, columnspan=1)
# Сохранить
SaveB = Button(text='Save', width=15, command=Save, bg='ForestGreen')
SaveB.grid(row=4, column=2)

# Кнопка генерации
Generate = Button(text='Generate Password', width=15, command=Gen)
Generate.grid(row=3, column=2)
# Открытие Паролей
with open('password.json', 'r') as file:
    b = json.load(file)
    Choose = Listbox()
    list_accounts = []
    for i in b:
        for j in b[i]:
            Choose.insert(END, i + ' – ' + j[0])
            list_accounts.append([i, j[0]])
            print(list_accounts)
Choose.grid(row=5, column=1)
# Информация о паролях

Info = Frame()
Info.grid(row=5, column=0)
w = Label(Info, text=f'Website:', width=20, height=2, font=('Arial', 8), anchor='w')
w.grid(row=1)
l = Label(Info, text=f'Login:', width=20, height=2, font=('Arial', 8), anchor='w')
l.grid(row=2)
p = Label(Info, text=f'Password:', width=20, height=2, font=('Arial', 8), anchor='w')
p.grid(row=3)
# Удаление паролей и получение паролей
Use = Frame()
Use.grid(row=5, column=2)
CodI = Entry(Use)
CodI.grid(row=1)
Get = Button(Use, text='Get', width=15, command=Getter)
Get.grid(row=0)
Delete = Button(Use, text='Delete', bg='red', width=15, command=Dell)
Delete.grid(row=2)
window.mainloop()

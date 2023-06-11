import sqlite3
global db
global sql
db = sqlite3.connect('note.db')
sql = db.cursor()
#sql.execute("""CREATE TABLE note (
#    data TEXT,
#    name TEXT,
#    not_text TEXT)""")
db.commit()
def add_notes():
    dat = input('Дату : ')
    name_n = input('Имя заметки')
    notes = input('Введите заметку')
    sql.execute(f"INSERT INTO note VALUES ('{dat}', '{name_n}', '{notes}')")
    db.commit()
    print('------------')
    print('Заметка добавлена')
    print('------------')

def print_all():
    for value in sql.execute(f"SELECT rowid, data, name FROM note "):
        print (value)
    print('------------')

def print_one():
    numb_not = input('Введите номер записи')
    sql.execute(f"SELECT rowid, * FROM note WHERE rowid = '{numb_not}'")
    print(sql.fetchone())
    print('------------')

def export_bd():
    str_items = ''
    count_ = 0
    for value in sql.execute(f"SELECT * FROM note "):
        value = str(value).replace('(', '')
        value = str(value).replace(')', '')
        value = str(value).split(',')
        for items, values in enumerate(value):
            str_items += values
            if count_ == 2:
                str_items += '\n'
                count_ = 0
                continue
            count_ += 1
    print(str_items)
    with open('bd.txt', 'a', encoding='UTF-8') as file:
        file.writelines(str_items)
    print('------------')
    print('Файл успешно экспортирован')
    print('------------')

def apd_notes():
    numb_not = input('Введите номер записи')
    note_apd = input('Введите новое описание для записи')
    sql.execute(f"UPDATE note SET  not_text = '{note_apd}' WHERE rowid = '{numb_not}'")
    db.commit()
    print('-----------------')
    print('Заметка изменена')
    print('-----------------')

def rem():
    numb_not = input('Введите номер записи')
    sql.execute(f"DELETE FROM note WHERE rowid = '{numb_not}'")
    db.commit()
    print('-----------------')
    print('Заметка удалена')
    print('-----------------')

print('-----------------')
print('Добро пожаловать в систему')
print('-----------------')
flag = True
while flag != False:
    print('Выбериет необходимые действия:')
    print(' 1 - вывести список заметок (кратко)')
    print(' 2 - добавить новую заметку')
    print(' 3 - вывести заметку по номеру(полностью)')
    print(' 4 - эскпортировать заметки')
    print(' 5 - изменить заметку')
    print(' 6 - удалить заметку')
    print(' 7 - выход')
    button = input('Введите цифру:')
    if button == '2':
        add_notes()
    elif button == '1':
        print_all()
    elif button == '3':
        print_one()
    elif button == '4':
        export_bd()
    elif button == '5':
        apd_notes()
    elif button == '6':
        rem()
    elif button == '7':
        exit()

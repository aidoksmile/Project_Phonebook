import model as m
import view as v

pb = m.Phonebook()
#Вывод телефонного справочника - тут надо исходить из того как будет построен view. Можно вывести 3 способами.
# 1 то как оно реализовано в классе Phonebook
# print(pb)
def show_phonebook(pb):
    if len(pb) < 1:
        print('Телефонная книга пуста')
    else:
        print(pb)

# # 2 то как оно реализовано в классе Record
#def show_phonebook(pb):
#     records = pb.get_records()
#     for record in records:
#         print(record)

# #     #Проивзольный вывод
#def show_phonebook(pb):
#     name = record.name
#     tephone = record.telephone
#     comment = record.comment
#     print(f"{name} {tephone} {comment}")

# 2. Добавление записи
def input_contact():
    name = input('Ведите ФИО контакта: ') #можно удалить запись внутри инпута, если для интерфейса она не нужна
    phone = input('Ведите телефон контакта: ')
    comment = input('Ведите комментарий: ')
    record = m.Record(name, phone, comment)
    m.Phonebook.add_record(record)
    m.Phonebook.dump()

#3. Удаление записи
def delеtе_contact():
    n = int(input('Введите номер контакта, который нужно удалить: '))
    index = n - 1
    len_records = len(m.Phonebook)
    if index < len_records:
        m.__delitem__(index)
        m.Phonebook.dump()
    else:
        print(f'Запись под номером {n} не существует')

#6. Поиск
def search_contact():
    records = m.Phonebook.get_records()
    result = None
    name_find = input('Введите контакт, который нужно найти: ')
    for index, record in enumerate(records):
        name = record.name
        telphone = record.telephone
        comment = record.comment
        if name == name_find or telphone == name_find or comment == name_find:
            result = record
            break
    if result is not None:
        print(result)

#7. Редактирование
def change_contact():
    n = int(input('Введите номер, под которым находится контакт в телефонном справочнике: '))
    index = n - 1
    name = input('Ведите измененное ФИО контакта: ')
    phone = input('Ведите измененный телефон контакта: ')
    comment = input('Ведите измененный комментарий: ')
    record_new = m.Record(name, phone, comment)
    m.Phonebook.get_records()[index] = record_new
    m.Phonebook.dump()

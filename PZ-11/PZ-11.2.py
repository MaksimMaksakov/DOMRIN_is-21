#Из предложенного текстового файла (text18-25.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно удалив букву «с» из
#текста.

a = open('text18-25.txt', 'w+')
a.write('''Мы долго молча отступали,
Досадно было, боя ждали,
Ворчали старики:
«Что ж мы? на зимние квартиры?
Не смеют, что ли, командиры
Чужие изорвать мундиры
О русские штыки?»''')
a.close()
a = open('text18-25.txt', 'r')
b = a.read()
a.close()
print(f'Ваш файл : \n{b}\n'
      f'Количество букв : {sum(map(str.isalpha, b))}')
d = open('new_file.txt', 'w')
d.write(b.replace('с', ''))
d.close()
d = open('new_file.txt', 'r')
print(f'Новый файл : \n{d.read()}')

while True:
    try:
        figure = int(input('Введите номер фигуры\n(1-ладья    2-слон      3-ферзь   4-конь) '))
        if figure>4:
            print('фигуры под таким номером нет')
        elif figure == 4:
            print("Для фигуры конь не доступны некоторрые функции программы ")
        x1 = int(input('Введите х1 '))
        if x1 in range(8):
            y1 = int(input('Введите y1 '))
            if y1 in range(8):
                x2 = int(input('Введите х2 '))
                if x2 in range(8):
                    y2 = int(input('Введите y2 '))
                    if y2 not in range(8):
                        print('число должно быть <9')
                else:
                    print('число должно быть <9')
            else:
                print('число должно быть <9')
        else:
            print('число должно быть <9')
        break
    except(Exception):
        print('Ввод некорректен')

if (x1+y1) % 2 == (x2+y2) % 2:
    print('цвет клеток совпадает')
else:
    print('цвет клеток не совпадает')

if figure == 1:
    if x1 == x2 or y1 == y2:
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке\n Возникнет угроза при ходе', x2, y1)

if figure == 2:
    if abs(x1-x2) == abs(y1-y2):
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке')
        if (x1+y1) % 2 != (x2+y2) % 2:
            print('Угроза невозможна')
        else:
            for i in range(8):
                if abs(x1+i-x2) == abs(y1+i-y2):
                    print('Возникнет угроза при ходе', x1+i,y1+i)
                if abs(x1-i-x2) == abs(y1-i-y2):
                    print('Возникнет угроза при ходе', x1-i,y1-i)

if figure == 3:
    if abs(x1-x2) == abs(y1-y2) or x1 == x2 or y1 == y2:
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке\n Возникнет угроза при ходе', x2, y1)

if figure == 4:
    if (x1+2 == x2 and y1+1 == y2) or (x1+1 == x2 and y1+2 == y2) or (x1-1 == x2 and y1+2 == y2) or (x1-2 == x2 and y1+1 == y2) or (x1-2 == x2 and y1-1 == y2) or (x1-1 == x2 and y1-2 == y2) or (x1+1 == x2 and y1-2 == y2) or (x1+2 == x2 and y1-1 == y2):
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке')
        print('программа не может написать ход для нападения')
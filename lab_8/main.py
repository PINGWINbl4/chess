from loguru import logger
print('значения координат находятся в диапозоне от 1 до 8')
logger.add("log.log", format="{time} {level} {message}", level="DEBUG")
# ввод всех переменных
while True:
    try:
        x1 = int(input('Введите х1 '))
        y1 = int(input('Введите y1 '))
        x2 = int(input('Введите х2 '))
        y2 = int(input('Введите y2 '))
        if not(x1<9 and x2<9 and y1<9 and y2<9 and x1>0 and x2>0 and y1>0 and y2>0):
            print('невозможная координата')
            logger.error('невозможная координата', x1, y1, x2, y2)
            continue
        figure = int(input('Введите номер фигуры\n(1-ладья    2-слон      3-ферзь   4-конь) '))
        if figure > 4:
            print('фигуры под таким номером нет')
        elif figure == 4:
            print("Для фигуры конь не доступны некоторрые функции программы ")
        break
    except(Exception):
        logger.error('Ввод некорректен')
        print('Ввод некорректен')

# цвет клеток
if (x1+y1) % 2 == (x2+y2) % 2:
    print('цвет клеток совпадает')
else:
    print('цвет клеток не совпадает')

# проверка фигур
# ладья
if figure == 1:
    if x1 == x2 or y1 == y2:
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке\n Возникнет угроза при ходе', x2, y1)
# слон
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
                    print('Возникнет угроза при ходе', x1+i,y1+i)
# ферзь
if figure == 3:
    if abs(x1-x2) == abs(y1-y2) or x1 == x2 or y1 == y2:
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке\n Возникнет угроза при ходе', x2, y1)
# конь
if figure == 4:
    if (x1+2 == x2 and y1+1 == y2) or (x1+1 == x2 and y1+2 == y2) or (x1-1 == x2 and y1+2 == y2) or (x1-2 == x2 and y1+1 == y2) or (x1-2 == x2 and y1-1 == y2) or (x1-1 == x2 and y1-2 == y2) or (x1+1 == x2 and y1-2 == y2) or (x1+2 == x2 and y1-1 == y2):
        print('фигура угражает клетке')
    else:
        print('фигура не угражает клетке')
        print('программа не может написать ход для нападения')

logger.info(str(x1))
logger.info(str(y1))
logger.info(str(x2))
logger.info(str(y2))
logger.info(str(figure))
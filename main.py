print("Игра Крестики-Нолики")
print("")
print("Ввод данных в формате x y,")
print("где х - номер строки,")
print("а у - номер столбца")
print("")

field = [[" "] * 3 for i in range(3)]

def show():
    print(f"  0 1 2")
    for i in range(3):
        row_info = " ".join(field[i])
        print(f"{i} {row_info}")

def ask():
    while True:
        cords = input("Ваш ход:").split()
        if len(cords) != 2:
            print("Введите две координаты")
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты вне диапазона")
            continue

        if field[x][y] != " ":
            print("Клетка занята")
            continue

        return x, y

def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл Х!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл О!")
            return True
    return False

count = 0
while True:
    count += 1
    show()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    x, y = ask()

    if count % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break
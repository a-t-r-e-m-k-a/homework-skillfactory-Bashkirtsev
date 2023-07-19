print("   Это крестики-нолии!!!")
print(" =========================")
print("      Ввод: x y")
print("  x - номер строки")
print("  y - номер столбца")





position_on_plate = [[" "] * 3 for i in range(3)]


def plate():
    print("")
    print(f"       0 1 2")
    print("      -------")
    for i in range(3):
        row_i = " ".join(position_on_plate[i])
        print(f"   {i} | {row_i}")
    print("")


def ask():
    while True:
        cords = input("Введите координаты: ").split()

        if len(cords) != 2:
            print("Введите две координаты!")
            continue

        x, y = cords

        if not x.isdigit() or not y.isdigit():
            print("Введите положительные числа!")
            continue

        x, y, = int(x), int(y)

        if not(0 <= x < 3 and 0 <= y < 3):
            print("Координаты вне диопазона!")
            continue

        if position_on_plate[x][y] != " ":
            print("Клетка занята!")
            continue

        return x, y


def win_check():
    win_cords = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)),
                 ((2, 0), (2, 1), (2, 2)), ((0, 0), (1, 1), (2, 2)),
                 ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 0), (2, 0)),
                 ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cords in win_cords:
        c1, c2, c3 = cords[0], cords[1], cords[2]

        if position_on_plate[c1[0]][c1[1]] == position_on_plate[c2[0]][c2[1]] == position_on_plate[c3[0]][c3[1]] != " ":
            plate()
            print(f"Выиграл {position_on_plate[c1[0]][c1[1]]}!!!")
            return True


count = 0
while True:
    count += 1

    plate()

    if count % 2 == 1:
        print("   Ходит крестик  ")
    else:
        print("   Ходит нолик  ")

    x, y = ask()

    if count % 2 == 1:
        position_on_plate[x][y] = "x"
    else:
        position_on_plate[x][y] = "0"

    if win_check():
        break

    if count == 9:
        print("Ничья!")
        break

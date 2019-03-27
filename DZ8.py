import random


class Bingo_card:
    def __init__(self, card_name):
        self.card_name = card_name
        self.card = self.generate_card()

    @staticmethod
    def generate_card():
        row = []
        for _ in range(27):
            while True:
                item = random.randint(1, 90)
                if row.count(item) == 0:
                    row.append(item)
                    break

        row1 = sorted(row[:9])
        row2 = sorted(row[9:18])
        row3 = sorted(row[18:])
        row = row1 + row2 + row3

        for i in range(12):
            while True:
                cleared_field = random.randint(0, 8)

                if row[cleared_field + ((i) // 4) * 9] != " ":
                    row[cleared_field + ((i) // 4) * 9] = " "
                    break
        return row

    def print_card(self):
        print(f"{self.card_name}")
        print("-------------------------------------------")
        print(f"{(self.card[:9])}")
        print(f"{(self.card[9:18])}")
        print(f"{(self.card[18:])}")
        print("-------------------------------------------")

    def has_number(self, number):
        self.number = number
        if self.card.count(self.number) != 0:
            return True
        else:
            return False

    def cross_out(self, number):
        self.number = number
        if self.card.count(self.number) == 0:
            return False
        else:
            for i in range(len(self.card)):
                if self.card[i] == self.number:
                    self.card[i] = "X"
            return True

    def is_win(self):
        if self.card.count("X") == 15:
            return True


class Barells:
    def __init__(self):
        self.barells = []

    def new_barrel(self):
        while True:
            barell = random.randint(1, 90)
            if self.barells.count(barell) == 0:
                self.barells.append(barell)
                return barell

    def print_barrels(self):
        print(f"Сыгравшие номера: {sorted(self.barells)}")


c = Bingo_card("Ваша карточка")
d = Bingo_card("Карточка компьютера")
b = Barells()
c.print_card()
d.print_card()
while True:
    i = b.new_barrel()
    print(f"Номер {i}!")

    while True:
        answer = input("Зачеркнуть? (Y,N)")
        if answer.lower() == "y":
            if c.cross_out(i):
                print("Число есть на карточке, игра продолжается")
                break
            else:
                print("Числа нет на карточке, вы проиграли!")
                exit(0)
        elif answer.lower() == "n":
            if c.has_number(i):
                print("Число есть на карточке, вы проиграли!")
                exit(0)
            else:
                print("Числа нет на карточке, игра продолжается!")
                break
        else:
            print("введите Y или N")
    d.cross_out(i)
    c.print_card()
    d.print_card()
    b.print_barrels()

    if c.is_win():
        print("Поздравляю! Вы выиграли!")
        exit(0)
    elif d.is_win():
        print("Сожалею, выиграл компьютер")
        exit(0)
    else:
        pass

class Player:
    def __init__(self, name):
        self.name = name

    def player_name(self):
        return self.name

    def players_pick(self):
        while True:
            coins = input(f"{self.name}, можно взять от 1 до 3 монеток. Сколько монеток возьмете?")
            try:
                coins = int(coins)
                if 1 <= coins <= 3:
                    return coins
                else:
                    raise ValueError("Нужно ввести число от 1 до 3")
            except ValueError as e:
                print(e)


class Coins:
    def __init__(self, quantity):
        self.quantity = quantity
        self.base_quantity = quantity

    def pick_coins(self, num):
        self.num = num
        self.quantity -= num
        if self.quantity <= 0:
            self.regenerate_coins()
            return False
        else:
            return True

    def print_coins(self):
        str = self.quantity * 'o'
        return f"{str}"

    def regenerate_coins(self):
        self.quantity = self.base_quantity


a = Player(input("Игрок 1, введите свое имя"))
b = Player(input("Игрок 2, введите свое имя"))
n = 25
box = Coins(n)

print("Игра в монетки:")
print("Игрок может взять от 1 до 3 монеток из коробки. Игрок, забравший последню монетку проигрывает.")
print(f"Сейчас в коробке {n} монеток")
print(box.print_coins())

while True:
    current_player = a.player_name()

    if box.pick_coins(a.players_pick()):

        print("Оставшиеся монетки:")
        print(box.print_coins())

        a, b = b, a
    else:
        print(f"Игрок {current_player} взял последнюю монетку и проиграл")
        choise = input("Хотите сыграть еще раз?, Y/N")
        if choise.lower() == "y":
            print(box.print_coins())
        else:
            print("Очень жаль, прощайте.")
            exit(0)

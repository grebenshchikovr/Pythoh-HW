import time


class Microwave:
    def __init__(self):
        """
        Задаем встроенные рецепты и максимальную мощность микроволновки
        """
        self.maxpower = 800
        self.recipes = {'pizza': [700, 3],
                        'boiled water': [800, 5],
                        'unfrozen': [400, 6],
                        }

    def avaialable_recipes(self):
        """
        Метод для вывода доступных рецептов на печать
        """
        return list(self.recipes.keys())

    def by_timer_and_power(self, power, timer):
        """
        Готовимся запускать микроволновку по мощности и таймеру, проверяем введеные величины
        """
        self.power = power
        self.timer = timer
        maxpower = self.maxpower

        if not self.is_timer_positive(timer):
            exit(1)
        if not self.is_correct_power(power, maxpower):
            exit(1)
        self.start_microwave(power, timer)

    def by_program(self, program):
        """
        Готовимся запускать микроволновку по программе, получаем программу из списка рецептов
        """
        program = program.lower()
        if program in self.recipes:
            current_parameters = self.recipes[program]
            self.start_microwave(current_parameters[0], current_parameters[1])
        else:
            print("Недопустимая программа")
            exit(1)

    @staticmethod
    def is_timer_positive(timer):
        """
        Проверяем корректность таймера
        """
        if timer > 0:
            return True
        else:
            print("Время работы должно быть больше 0")
            exit(1)

    @staticmethod
    def is_correct_power(power, maxpower):
        """
        Проверяем корректность мощности
        """
        if power > 0 and power <= maxpower:
            return True
        else:
            print(f"Мощность должна быть больше 0 и меньше {maxpower}")

    @staticmethod
    def convert_timer(timer):
        """
        Переводим минуты в секунды
        """
        return timer * 60

    def start_microwave(self, power, timer):
        """
        Запускаем микроволновку
        """
        print(f"Microwave ON, power {power}")
        time.sleep(self.convert_timer(timer))
        print("Microwave OFF")


microwave1 = Microwave()

print(f"Доступны следующие рецепты {microwave1.avaialable_recipes()}")
microwave1.by_timer_and_power(400, 3)
microwave1.by_program('Boiled water')

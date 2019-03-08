list_1 = ["апельсин", "манго", "авокадо", "лимон", "персик"]
list_2 = ["ананас", "апельсин", "персик", "", "абрикос", "банан"]

cross_list = [value for value in list_1 if list_2.__contains__(value)]

print(cross_list)
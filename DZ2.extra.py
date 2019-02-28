recipe = {
    "картошка": 4,
    "колбаса": 6,
    "соль": 1,
    "яйцо": 2,
    "зеленый горошек": 1,
    "майонез": 1
}

in_stock = {
    "яйцо": 10,
    "молоко": 1,
    "картошка": 2,
    "соль": 50,
    "кетчуп": 1
}

shopping_list = {}

for key in recipe:
    if in_stock.get(key):
        if in_stock[key] < recipe[key]:
            shopping_list[key] = (recipe[key] - in_stock[key])
    else:
        shopping_list[key] = recipe[key]
print("Список покупок:")
print(shopping_list)

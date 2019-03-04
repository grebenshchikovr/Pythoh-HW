def is_happy(ticket_number):
    if len(ticket_number) != 6 or not ticket_number.isdigit():
        answer = "Не правильный номер билета!"
        return answer

    array = [int(item) for item in ticket_number]
    if sum(array[0: 3]) == sum(array[3:]):
        answer = "Билет счастливый!"
    else:
        answer = "Билет обычный"
    return answer


ticket_number = input("Введите номер билета: ")
print(is_happy(ticket_number))

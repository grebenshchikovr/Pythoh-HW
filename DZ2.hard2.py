text1 = input("Введите первый текст")
text2 = input("Введите второй текст")
# text1 = 'Груша манго апельсин дыня кактус'
# text2 = 'картошка кактус смерть олово грУша'
words1 = set(text1.lower().split(" "))
words2 = set(text2.lower().split(" "))
print(f"В обоих текстах есть такие слова: {words1.intersection(words2)}")

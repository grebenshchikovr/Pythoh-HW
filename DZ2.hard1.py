import re

text = "Lorem ipsum долор сит амет"
text = text.lower().split(' ')
letters_list = []
print(f'в тексте {len(text)} слов')
letters = ''.join(text)
for item in letters:
    if re.match('[a-z]', item):
        letters_list.append(item)
print(f'в тексте {len(letters_list)} букв английского алфавита')

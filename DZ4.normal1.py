import random
import re

numbers = [random.randint(0, 9) for _ in range(2500)]
string = "".join(str(x) for x in numbers)

result = re.findall(r"1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,}|0{2,}", string)
sorted_result = sorted(result, key=len, reverse=True)
print(f"Самая длинная последовательность из одинаковых цифр в файле nums.txt: {sorted_result[0]}")

with open("nums.txt", "w") as f:
    f.write(string)
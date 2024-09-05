# 숫자 리스트 정렬
# numbers = ['20240903_12', '20240903_11']
# sorted_numbers = sorted(numbers, reverse = False)
# print(f"정렬된 숫자: {sorted_numbers}")

import os
folderName = os.listdir('test')
print(folderName)
sorted_numbers = sorted(folderName, key=lambda x: tuple(map(int, x.split('_'))))
print(f"정렬: {sorted_numbers}")

 
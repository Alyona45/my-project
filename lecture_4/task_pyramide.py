n = int(input())

triangle = []
triangle.append([1])

for i in range(2, n + 1):
    old_line = triangle[-1]
    new_line = [1]
    for index in range(len(old_line) - 1):
        sum_elements = old_line[index] + old_line[index + 1]
        new_line.append(sum_elements)
    new_line.append(1)
    triangle.append(new_line)
    
if n > 5:
    print('Сори, пока не умею работать с цифрами больше 5 :(')
else: 
    width = n * 2  
    for line in triangle:
        row = " ".join(map(str, line))
        print(row.center(width))

def total():
    count = 0
    for i in range(1, 64 +1):
        count = count + (i ** 2)

    return count

print(total())
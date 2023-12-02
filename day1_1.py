numbers: str = ''
total: int = 0


while True:
    try:
        line = input()

        for i in line:
            if i.isnumeric():
                numbers += i

        if len(numbers) >= 2:
            total += int(numbers[0] + numbers[-1])
        else:
            total += int(numbers[0] + numbers[0])

        numbers = ''

    except EOFError:
        break

print(total)


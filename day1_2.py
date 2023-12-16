frase = ''
numbers = ''
total = 0

numbers_e = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8',
           'nine': '9'}

while True:
    try:
        line = input()

        while True:

            trade = False

            for j in numbers_e.keys():
                if j in line:
                    line = line.replace(j, j[0]+numbers_e[j]+j[-1])
                    trade = True

            if not trade:
                break

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
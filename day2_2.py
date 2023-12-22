games = {}
i = 1
red = 0
green = 0
blue = 0
_sum = 0

while True:
    try:
        line = input()
        a = line.split(':')

        games[i] = []
        for j in a[1].split(';'):
            games[i].append(j.split(','))

        for k in games[i]:

            for j in k:
                numbers, colors = j[1::].split(' ')
                if colors == 'red':
                    if red < int(numbers):
                        red = int(numbers)

                elif colors == 'blue':
                    if blue < int(numbers):
                        blue = int(numbers)

                elif colors == 'green':
                    if green < int(numbers):
                        green = int(numbers)

        _sum += red * blue * green

        red = 0
        green = 0
        blue = 0

    except EOFError:
        print(_sum)
        break

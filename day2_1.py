games = {}
i = 1
ids = 0
_t = False

while True:
    try:
        line = input()
        a = line.split(':')

        games[i] = []
        for j in a[1].split(';'):
            games[i].append(j.split(','))

        for k in games[i]:
            red = 0
            green = 0
            blue = 0
            for j in k:
                numbers, colors = j[1::].split(' ')
                if colors == 'red':
                    red += int(numbers)
                elif colors == 'blue':
                    blue += int(numbers)
                elif colors == 'green':
                    green += int(numbers)

            if red <= 12 and blue <= 14 and green <= 13:
                _t = True
                continue
            else:
                _t = False
                break

        if _t:
            ids += i

        i += 1

    except EOFError:
        print(ids)
        break

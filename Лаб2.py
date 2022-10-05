import csv

def flag_p():
    for i in range(6):
        if i <= 2:
            print( WHITE + ' ' * (20) + END)
        else:
            print( RED + ' ' * (20) + END)


def uzor():
    for i in range(5):
        if i % 2 == 0:
            print(BLACK + ' ' * 50 + END)
        elif i == 1:
            print(WHITE + ' ' * 24 + BLACK + ' ' * 2 + WHITE + ' ' * 24 + END)
        else:
            print(WHITE + ' ' * 11 + BLACK + ' ' * 2 + WHITE + ' ' * 24 + BLACK + ' ' * 2 + WHITE + ' ' * 11 + END)


def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)


array_plot = [[0 for col in range(10)] for row in range(10)]
result = [0 for i in range(10)]

for i in range(10):
    result[i] = i ** 0.5


step = round(abs((result[9] - result[0])) / 9, 2)

RED = '\u001b[41m'
BLACK = '\u001b[40m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


km = 0
kb = 0
f = 0  # flag

with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        if f == 0:
            f = 999

        else:
            year = int(row[6][:4])
            if year < 2017:
                km += 1
            else:
                kb += 1
sum = km + kb
pkm = int(km / (sum / 100))
pkb = 100 - pkm


def diagramma():
    print(BLACK + ' ' * ((pkm - 2) // 2) + BLACK + str(pkm) + BLACK + ' ' * ((pkm - 2) // 2) + RED + ' ' * ((pkb - 2) // 2) + RED + str(pkb) + RED + ' ' * ((pkb - 2) // 2) + END)


flag_p()
print()
uzor()
print()
array_init(array_plot, step)
array_fill(array_plot, result, step)
print_plot(array_plot)
print()
diagramma()


RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'


for i in range(6):
        print(f'{BLUE}{"  " * 5}{WHITE}{"  " * 5}{RED}{"  " * 5}{END}')



BLACK = '\u001b[40m'
END = '\u001b[0m'
size = 15
for i in range(size):
    if i % 2 == 0:
        print(f'{BLACK}{'  '} {END}{'  '} {BLACK}{'  '} {END}{' '}  {BLACK}{'  '} {END}{'   '}{BLACK}{'  '} {END} {'  '}{BLACK}{'  '} {END}')
    else:
        print(
            f'{END} {'  '}{BLACK}{'  '} {END}{'  '} {BLACK}{'  '} {END}{'  '} {BLACK}{'  '} {END}{'  '} {BLACK}{'  '} {END}')




def grafic():
    height = 22
    width = 50
    scale_y = height/(width ** 2)
    points = []

    for x in range(width +1):
        y = x ** 2
        if y < height:
            points.append((x, height - y))

    for rad in range(height + 1):
        for col in range(width + 1):
            if (col, rad) in points:
                print("1", end=" ")
            else:
                print(" ", end= " ")
        print()
grafic()



BLUE = 	'\u001b[44m'
RED = '\u001b[41m'
END = '\u001b[0m'

file = open('sequence.txt', 'r')
list = []
for number in file:
    list.append(float(number))

a = 0
b = 0

for i in range(0, len(list)):
    if int(list[i]) > 0:
        a += 1
    elif int(list[i]) < 0:
        b += 1

# print(list)

print(' bigger 0', '(', a, ')', f'{RED}{" " * a}{END}')
print('smaller 0', '(', b, ')', f'{BLUE}{" " * b}{END}')
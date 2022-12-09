text = open('text.txt', 'r', encoding="utf-8")
numberLines = text.read().count(':')
value = (input('Ведіть довільне тризначне число: '))
try:
    if len(value) != 3:
        print('Треба вводити тільки тризначне число')
    else:
        text = open('text.txt', 'r', encoding="utf-8")
        for i in range(numberLines):
            lines = text.readline().split()
            a = int(lines[-1])
            if int(value) < a:
                print(lines[0])
except:
    print('Перевірте правильність введених данних')
    
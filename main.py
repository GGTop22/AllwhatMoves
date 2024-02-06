with open("INPUT.TXT", "r") as file:
    n, m = map(int, file.readline().split())

    field_t = []
    # Читаем следующие N строк, каждая из которых содержит M символов, представляющих поле в момент времени T
    for _ in range(n):
        row = list(file.readline().strip())
        field_t.append(row)

    # Пропускаем пустую строку
    file.readline()

    # Создаем пустой список для представления поля в момент времени T + 1
    field_t_plus_1 = []
    # Читаем следующие N строк, каждая из которых содержит M символов, представляющих поле в момент времени T + 1
    for _ in range(n):
        row = list(file.readline().strip())
        field_t_plus_1.append(row)



# Создаем пустое множество для хранения движущихся объектов
moving_objects = set()

# Проходимся по каждой клетке поля в момент времени T и сравниваем ее с аналогичной клеткой в момент времени T + 1
for i in range(n):
    for j in range(m):
        # Если символы в этих двух клетках различаются, то добавляем символ из момента времени T в множество движущихся объектов
        if field_t[i][j] != field_t_plus_1[i][j]:
            moving_objects.add(field_t[i][j])





moving_objects = sorted(moving_objects, key=lambda x: (x.lower(), x.islower()))

# Открываем файл для записи
with open("OUTPUT.TXT", "w") as file:
    file.write(str(len(moving_objects)) + '\n')

    file.write(''.join(moving_objects))
    

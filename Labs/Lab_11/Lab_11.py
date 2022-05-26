# Варіант 10
# а) Дан файл f, компоненти якого є цілими числами. Отримати в файлі g всі компоненти файлу f що є простими числами.
# Простим називається число, що більше за 1 та не має інших дільників, окрім 1 та самого себе)
# б) Дан текстовий файл f. Додати в кінець файлу f символи голосних букв, які не входять до вихідного файлу.
# Task 1
print("Task 1")
startfile = open("f.txt", "w+")
startfile.write("1 2 3 4 5 6 7 8 9 10 11 13 40 35 75 6 45 999 949 747 382 137 94058 03248 0 0 8 9498 39837 9 6738798 "
                "39645 89 4395 7689346 87")
startfile.seek(0)
x = startfile.read()
startfile.close()
tofile = open("g.txt", "w+")
x = x.split()  # list with all our numbers from file f
print(x)
y = []  # list with all prime numbers
for i in x:
    counter = 0
    if int(i) > 1:
        for u in range(2, int(i)):
            if int(i) % u == 0:
                counter = 1
                break
        if counter == 0:
            y.append(i)  # Adding only prime numbers into the list
y = " ".join(y)  # getting a string out of a list with prime numbers
tofile.write(y)  # writing prime numbers in the file
tofile.seek(0)
print(tofile.read())
tofile.close()

# Task 2
print("\n", "*"*40, "\n\nTask 2")
startfile = open("f(2).txt", "w+")
startfile.write("A brown wood chair, built from oak and ash, is boring - paint it black and indigo.")  # no "e" or "y"
startfile.seek(0)
x = startfile.read()
print(f'Original file content: {x}')
vowels = ["a", "e", "i", "o", "u", "y"]
vowels_to_add = []
for i in vowels:
    if i not in x:
        vowels_to_add.append(i)
vowels_to_add = "\n" + " ".join(vowels_to_add)  # Concatenate newline with vowels to add, divided by whitespace
startfile.write(vowels_to_add)  # Adding to the end, because .read() left cursor at the end of file
startfile.seek(0)  # resetting the pointer to the start of file
x = startfile.read()
print(f'Edited: {x}')

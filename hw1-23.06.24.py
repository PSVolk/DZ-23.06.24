with open("text1.txt", "r") as f1, open("text2.txt", "r") as f2:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    if len(lines1) != len(lines2):
        print("Файлы содержат разное количество строк.")
    else:
        for i in range(len(lines1)):
            if lines1[i].strip() != lines2[i].strip():
                print(f"Различие в строке {i + 1}:")
                print(f"Файл 1: {lines1[i].strip()}")
                print(f"Файл 2: {lines2[i].strip()}")

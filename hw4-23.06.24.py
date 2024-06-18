with open('text1.txt', 'r') as file:
    lines = file.readlines()

max_length = max(len(line.strip()) for line in lines)

print(f"Длина самой длинной строки: {max_length}")

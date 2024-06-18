with open('text1.txt', 'r') as file:
    lines = file.readlines()

lines.pop()

with open('text111.txt', 'w') as output_file:

    output_file.writelines(lines)

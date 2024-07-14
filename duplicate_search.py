file_path = 'INPUT/output.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

duplicates = []
for i, line in enumerate(lines):
    if lines.count(line) > 1 and line not in duplicates:
        duplicates.append(line)

print(duplicates)

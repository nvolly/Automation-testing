1) n = int(input("Enter the number of lines to read: "))
file_path = input("Enter the file path: ")
with open(file_path, 'r') as file:
    for
i in range(n):
line = file.readline()
if not line:
    break
print(line.rstrip())

2) with open('file.txt', 'r') as file:
    last_line = None
for line in file:
    last_line = line
if last_line:
    print(last_line.rstrip())

with open('file.txt', 'r') as file:
    line_num = 0
for line in file:
    line_num += 1
if line_num == 15:
    print(line.rstrip())
break

3) with open('file.txt', 'r') as file:
    for
line in file:
line_num = file.tell()
if line_num % 3 == 0:
    print(line.rstrip())

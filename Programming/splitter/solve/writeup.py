f = open("splitter/solve/Values.txt", 'r')
number = f.read()
arr = []
for i in range(0, len(number), 3):
    arr.append(number[i:i+3])
a = 0
b = 0
three_five = []
four_six = []
for i in arr:
    if int(i) % 4 == 0 and int(i) % 6 == 0:
        a += int(i)
        three_five.append(int(i))
    if int(i) % 3 == 0 and int(i) % 5 == 0:
        b += int(i)
        four_six.append(int(i))
print(b - a)

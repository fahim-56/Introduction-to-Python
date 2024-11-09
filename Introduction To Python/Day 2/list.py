# index  0   1   2   3   4   5   6   7   8
numbers=[10, 20, 30, 40, 50, 60, 70, 80, 90]
# index  -9  -8  -7  -6  -5  -4  -3  -2  -1

print(numbers[-5])
print(numbers[3])

# [starting index : (ending index-1)]
print(numbers[1:5])

# [starting index : (ending index-1) : increase/decrease step]
print(numbers[1:8:2])
print(numbers[8:2:-2])
print(numbers[2:])
print(numbers[:7])
print(numbers[:])
print(numbers[::-1])

for value in numbers:
    print(value)

for i,value in enumerate(numbers):
    print(i,value)
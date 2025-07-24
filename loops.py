

print("           SIMPLE CALCULATOR"       )
print("Choose the function you want to perform")
print("1 - ADDITION")
print("2 - SUBTRACTION")
print("3 - MULTIPLICATION")
print("4 - DIVISION")

choice = input()

print("Addition")
a = int(input())
b = int(input())

result = a + b
print(result)

for number in range(a, b + 1):
    print(number)
for number in range(a, b, -1):
    print(number)
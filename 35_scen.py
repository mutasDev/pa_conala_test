#read keyboard-input
ted integers and prints them in reverse order

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        break

for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])
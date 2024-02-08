def histogram(numbers):
    for num in numbers:
        print("*" * num)

input = input()
numbers_list = [int(num) for num in input.split()]
histogram(numbers_list)
print(histogram)

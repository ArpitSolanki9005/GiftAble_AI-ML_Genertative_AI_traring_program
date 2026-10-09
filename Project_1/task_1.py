#1.Write a Python program to find the largest number in a list without using the built-in max() function.
#numbers = [10, 25, 7, 45, 18]

numbers = [100, 25, 7, 45, 18,50]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is:", largest)

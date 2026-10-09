
#2 Write a Python program to count how many times each word appears in a list.
# words = ["python", "java", "python", "sql", "java", "python"]

words = ["python", "java", "python", "sql", "java", "python"]

count = {}

for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)
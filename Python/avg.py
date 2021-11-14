from functools import reduce


gradel = []
igrade = int(input("Provide the number grades: "))
counter = 1

while igrade > 0:

    grade = int(input(f"Enter grade {counter}: "))
    gradel.append(grade)
    counter += 1
    igrade  -= 1


print("Grades are below:")
print(gradel)

avg = reduce(lambda x, y: x + y, gradel) / len(gradel)
evens = list(filter(lambda x : x % 2 == 0, gradel))

print(f"Your Grade Point Average is: {avg}")
print(evens)

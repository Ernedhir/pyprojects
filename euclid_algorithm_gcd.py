num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
print("--------------------------")

if num1 < num2: num1, num2 = num2, num1

def iterative_euclidean(num1: int, num2: int) -> None:
    while num2:
        print(num1, num2)
        num1, num2 = num2, num1 % num2
    return num1

def recursive_euclidean(num1: int, num2: int):
    if num1 == 0:
        return num2
    else: print(num1, num2)
    return recursive_euclidean(num2 % num1, num1)

print(iterative_euclidean(num1, num2))
print("--------------------------")
print(recursive_euclidean(num1, num2))

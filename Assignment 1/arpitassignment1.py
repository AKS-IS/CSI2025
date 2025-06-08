#TASK 1
n = 5
for i in range(1, n+1):
    print("* " * i)
    
print()

#TASK 2
n = 5
for i in range(n):
    print("  " * i + "* " * (n - i))

print()

#TASK 3
n = 5
for i in range(1, n + 1):
    spaces = n - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)


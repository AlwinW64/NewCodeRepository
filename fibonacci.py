n = int(input("n: "))
a = 0
b = 1
print(a)
print(b)
c = a + b
while c <= n:
    print(c)
    a = b
    b = c
    c = a + b
# The End

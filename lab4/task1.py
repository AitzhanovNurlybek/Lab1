def square(N):
    for i in range(1,N+1):
        yield i**2

N = int(input())
for square1 in square(N):
    print(square1)

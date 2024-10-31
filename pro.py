def solve(n):
    for i in range(1, n + 1):
        if i * (i + 1) <= n:
            print(i * (i + 1), end=" ")

print("Pronic Numbers Between 1 and 100:")
solve(100)

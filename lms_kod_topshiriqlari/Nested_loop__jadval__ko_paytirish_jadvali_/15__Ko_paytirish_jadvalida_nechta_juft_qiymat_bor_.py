n, m = map(int, input().split())

odd_i = (n + 1) // 2 
odd_j = (m + 1) // 2

even_count = n * m - (odd_i * odd_j)

print(even_count)
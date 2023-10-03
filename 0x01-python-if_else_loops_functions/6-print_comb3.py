#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        sep = ", " if j < 9 else "\n"
        print(f"{i:02d}" if i == 0 and j == 1 else f"{i * 10 + j:02d}", end=sep)


def max(a, b):
    if a > b:
        return a
    return b

def items(sum_matrix, values, weights, m, n):
    print("\tChoosen Item and Value")
    while m > 0 and n > 0:
        if sum_matrix[m][n] == sum_matrix[m][n - 1]:
            while sum_matrix[m][n] == sum_matrix[m][n - 1]:
                n -= 1
        elif sum_matrix[m][n] == sum_matrix[m - 1][n]:
            while sum_matrix[m][n] == sum_matrix[m - 1][n]:
                m -= 1
        print(m, "\t", values[m])
        n -= weights[m]
        m -= 1

def knapsack(values, weights, m, c):
    sum_matrix = [[0 for _ in range(c)] for _ in range(m)]

    for i in range(1, m):
        sum_matrix[i][0] = 0

    for j in range(1, c):
        sum_matrix[0][j] = 0

    for i in range(1, m):
        for j in range(1, c):
            if j - weights[i] >= 0:
                sum_matrix[i][j] = max(sum_matrix[i - 1][j], values[i] + sum_matrix[i - 1][j - weights[i]])
            else:
                sum_matrix[i][j] = sum_matrix[i - 1][j]

    print("\n\tKnapsack Matrix")
    print(" ", end="\t")
    for i in range(c):
        print("\t", i, end="")
    print()

    for i in range(m):
        print(i, end="")
        for j in range(c):
            print("\t", sum_matrix[i][j], end="")
        print()

    print("\nMaximum Knapsack Value =", sum_matrix[m - 1][c - 1], "\n")

    items(sum_matrix, values, weights, m - 1, c - 1)

    return

if __name__ == "__main__":
    m = int(input("Enter number of items: "))
    m += 1
    values = [0] * m
    weights = [0] * m

    for i in range(1, m):
        weights[i] = int(input(f"Enter weight of item {i}: "))
        values[i] = int(input(f"Enter value of item {i}: "))

    print("\nItem\tWeight\tValue")
    for i in range(1, m):
        print(f"{i}\t{weights[i]}\t{values[i]}")

    capacity = int(input("Enter capacity: "))
    knapsack(values, weights, m, capacity + 1)
#Least Cost Cell Method
import numpy as np

def least_cost_cell(cost_matrix, supply, demand):
    m, n = cost_matrix.shape
    allocation = np.zeros((m, n))

    while np.sum(allocation) < m * n:
        min_cost = np.inf
        min_i, min_j = -1, -1

        for i in range(m):
            for j in range(n):
                if allocation[i, j] == 0 and cost_matrix[i, j] < min_cost:
                    min_cost = cost_matrix[i, j]
                    min_i, min_j = i, j

        quantity = min(supply[min_i], demand[min_j])
        allocation[min_i, min_j] = quantity
        supply[min_i] -= quantity
        demand[min_j] -= quantity

    return allocation

def calculate_total_cost(allocation, cost_matrix):
    total_cost = np.sum(allocation * cost_matrix)
    return total_cost


# Example problem
cost_matrix = np.array([
    [3, 1, 7, 4],
    [2, 6, 5, 9],
    [8,3, 3, 2]
])

supply = np.array([300, 400, 500])
demand = np.array([250, 350, 400, 200])

# Apply the Least Cost Cell Method
allocation = least_cost_cell(cost_matrix, supply, demand)
print("Allocation Matrix :\n" , allocation )

# Calculate and print the minimum cost
min_cost = calculate_total_cost(allocation, cost_matrix)


print("\n\nMinimum Cost:", min_cost)
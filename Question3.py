#Question 3

# A furniture company produces chairs and tables from two resources, wood and metal. The company has 125 units of wood and 80 units of metal available.
# Each chair requires 1 unit of wood and 3 units of metal, while each table requires 5 units of wood and 1 unit of metal. The profit from selling a chair is 20 dollars, and the profit from selling a table is 30 dollars.
# How many chairs and tables should the company produce to maximize its profit? What is the maximum profit? Implement using linear programming package.

print("This problem can be formulated as :  z = 20x + 30y ")
print("Subject to constraints: ")
print("x + 3y <= 125")
print("5x + y <= 80")
print("x , y >= 0")

#libraries
import numpy as np
from scipy.optimize import linprog

#program

x = np.array([-20, -30])

D = np.array([[1, 5], [3, 1]]) #wood and metal constraints

E = np.array([125,80])


# As linprog does minimization, Purposely did put a negative sign on the objective
bnd = [(0, float("inf")),(0, float("inf"))]
result = linprog(x, A_ub=D, b_ub=E, bounds=bnd)

print("(x , y) =" , result.x)

optimal_chocolate_cakes, optimal_vanilla_cakes = result.x
max_revenue = result.fun  # linprog minimizes, so the objective value is the actual revenue

# Print the results
print("Optimal Number of Chocolate Cakes:", optimal_chocolate_cakes)
print("Optimal Number of Vanilla Cakes:", optimal_vanilla_cakes)
print("Maximum Revenue:", -max_revenue)  # Correcting for minimization

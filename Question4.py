#Question 4

# A farmer has a field of 60 acres in which he plants two crops, wheat and barley.
#The farmer has to plant at least 20 acres of wheat and at least 10 acres of barley.
#He has 1200 pounds of fertilizer and 600 pounds of insecticide available.
#Each acre of wheat requires 20 pounds of fertilizer and 10 pounds of insecticide, while each acre of barley requires 10 pounds of fertilizer and 15 pounds of insecticide.
#The profit from an acre of wheat is 200 dollars, and the profit from an acre of barley is 150 dollars.
#How many acres of each crop should the farmer plant to maximize his profit? What is the maximum profit? Implement using linear programming package.

print("This problem can be formulated as :  z = 200x + 150y ")
print("Subject to constraints: ")
print("20x + 10y <= 1200")
print("10x + 15y <= 600")
print("x >= 20")
print("y >= 10")

#libraries
import numpy as np
from scipy.optimize import linprog

#program

x = np.array([-200, -150])

D = np.array([[20, 10], [10, 15]], ) #wood and metal constraints

E = np.array([1600, 600])

x_bnd=(20,None)

y_bnd=(10,None)

# As linprog does minimization, Purposely did put a negative sign on the objective

result = linprog(x, A_ub=D, b_ub=E, bounds=[x_bnd, y_bnd])

print("(x , y) =" , result.x)

optimal_chocolate_cakes, optimal_vanilla_cakes = result.x
max_revenue = result.fun  # linprog minimizes, so the objective value is the actual revenue

# Print the results
print("Optimal Number of Chocolate Cakes:", optimal_chocolate_cakes)
print("Optimal Number of Vanilla Cakes:", optimal_vanilla_cakes)
print("Maximum Revenue:", -max_revenue)  # Correcting for minimization
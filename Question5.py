print("This problem can be formulated as :  z = 3x + 2y ")
print("Subject to constraints: ")
print("2x + y <= 500")
print("x + y <= 400")
print("x >= 100")
print("y >= 50")

#libraries
import numpy as np
from scipy.optimize import linprog

#program

x = np.array([-3, -2])

D = np.array([[2, 1], [1, 1], [-1,0], [0,-1]]) #wood and metal constraints

E = np.array([500, 400, -100, -50])

x_bnd=(0,None)

y_bnd=(0,None)

# As linprog does minimization, Purposely did put a negative sign on the objective

result = linprog(x, A_ub=D, b_ub=E, bounds=[x_bnd, y_bnd])

print("(x , y) =" , result.x)

optimal_chocolate_cakes, optimal_vanilla_cakes = result.x
max_revenue = result.fun  # linprog minimizes, so the objective value is the actual revenue

# Print the results
print("Optimal Number of Chocolate Cakes:", optimal_chocolate_cakes)
print("Optimal Number of Vanilla Cakes:", optimal_vanilla_cakes)
print("Maximum Revenue:", -max_revenue)  # Correcting for minimization
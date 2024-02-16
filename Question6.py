#Question 6

#Solve the following without using linear programming package
#Maximize p=2u1+3u2+u3 , Subject to u1+u2+u3≤4, u1+2u2−u3≥2, u1,u2,u3≥0

print("This problem can be formulated as :  p = 2u1 + 3u2 + u3 ")
print("Subject to constraints: ")
print("u1 + u2 + u3 <= 4")
print("u1 + 2u2 - u3 >= 2")
print("u1, u2, u3 >= 0")


#libraries
import numpy as np
from scipy.optimize import linprog

#program

x = np.array([-2, 3, 1])

D = np.array([[1, 1, 1], [1, 2, -1]]) #wood and metal constraints

E = np.array([4, -2])

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
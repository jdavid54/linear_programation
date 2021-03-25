# https://apmonitor.com/pdc/index.php/Main/LinearProgramming
'''
A simple production planning problem is given by the use of
two ingredients A and B that produce products 1 and 2.
The available supply is A=30 units and B=44 units.
For production it requires:

    - 3 units of A and 8 units of B to produce Product 1
    - 6 units of A and 4 units of B to produce Product 2

There are at most 5 units of Product 1 and 4 units of Product 2.
Product 1 can be sold for 100 and Product 2 can be sold for 125.

The objective is to maximize the profit for this production problem.
For this problem determine:

    - A potential feasible solution
    - Identify the constraints on the contour plot
    - Mark the set of feasible solutions on the contour plot
    - Identify the minimum objective feasible solution
    - Identify the maximum objective feasible solution
    - Use a solver to find a solution
'''
from gekko import GEKKO
m = GEKKO()
# Var x1, x2 lowerbound, upperbound
x1 = m.Var(lb=0, ub=5) # Product 1
x2 = m.Var(lb=0, ub=4) # Product 2
m.Maximize(100*x1+125*x2) # Profit function
m.Equation(3*x1+6*x2<=30) # Units of A
m.Equation(8*x1+4*x2<=44) # Units of B
m.solve(disp=False)
p1 = x1.value[0]; p2 = x2.value[0]
print ('Product 1 (x1): ' + str(p1))
print ('Product 2 (x2): ' + str(p2))
print ('Profit        : ' + str(100*p1+125*p2))
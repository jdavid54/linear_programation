# https://apmonitor.com/pdc/index.php/Main/LinearProgramming

# solve with SciPy
from scipy.optimize import linprog
# matrices method
# minimize cx
# Ax = b 
# Ax < b

c = [-100, -125]       # negative prices P1, P2 to minimize
A = [[3, 6], [8, 4]]   #
b = [30, 44]           # ingredients to be used 
# var to be determined
x0_bounds = (0, 5)     # upperbound = 5 fot P1
x1_bounds = (0, 4)     # upperbound = 4 fot P2
res = linprog(c, A_ub=A, b_ub=b, \
              bounds=(x0_bounds, x1_bounds),
              options={"disp": True})
print(res)
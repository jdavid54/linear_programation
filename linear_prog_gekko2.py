# https://apmonitor.com/pdc/index.php/Main/LinearProgramming
'''
Method 2b: Dense Matrices (Gekko)

Dense matrix form is also available in Gekko.
In this case, two model functions qobj (quadratic objective)
and axb (Ax<b) objects are used to create the model.
Integer variables for discrete optimization are possible with
the APOPT solver (option 1) when the variable is specified with
integer=True. See Model Building Functions in the Gekko documentation.
'''
# matrix method
from gekko import GEKKO
m = GEKKO(remote=False)
c = [100, 125]
A = [[3, 6], [8, 4]]
b = [30, 44]
x = m.qobj(c,otype='max')     # maximize cx otype: optimization type
m.axb(A,b,x=x,etype='<=')      # Ax < b      etype: equation type
# bounds
x[0].lower=0; x[0].upper=5
x[1].lower=0; x[1].upper=4
m.options.solver = 1     # 1: APOPT, 2: BPOPT, 3: IPOPT
m.solve(disp=True)
print ('Product 1 (x1): ' + str(x[0].value[0]))
print ('Product 2 (x2): ' + str(x[1].value[0]))
print ('Profit        : ' + str(m.options.objfcnval))
print('error !!! values must be : 4.0, 3.0')

# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math


# In[ ]:


def gaussian(x, mu, sigma):
    return np.exp(-np.power(x - mu, 2.) / (2 * np.power(sigma, 2.)))

def phi(x):
    r=1/np.sqrt(2*np.pi)*np.exp(-0.5*x**2)
    return r
    
def phi2(x, mu, sigma):
    r=1/sigma*phi((x-mu)/sigma)
    return r

print(phi(0))
print(phi2(1,1,.5))


# In[ ]:


mu = 10
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma),'r-')
plt.plot(x,gaussian(x, mu, sigma)/2.5)
plt.show()


# In[ ]:


x_values = np.linspace(-3, 3, 120)
for mu, sig in [(-1, 1), (0, 2), (2, .2)]:
    plt.plot(x_values, gaussian(x_values, mu, sig))
plt.show()


# In[ ]:


from scipy.integrate import quad

def integrand(x, a, b):
    return a*x**2 + b

def f(x):
    return 2*x


# In[ ]:


a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)


# In[ ]:


I = quad(phi, 0, 1)
print(I)


# In[ ]:


I = quad(phi, -1, 0)
print(I)


# In[ ]:


I = quad(phi, -1, 1)
print(I)


# In[ ]:


I = quad(f, 0, 1)
print(I)


# In[ ]:


x=np.linspace(-1,1,100)
#print(x)


# In[ ]:


y=[]
for i in x:
    q=quad(f,0,i)
    y.append(q[0])


# In[ ]:


plt.plot(x,y)
plt.show()


# In[ ]:


x=np.linspace(-5,5,100)
y=[]
for i in x:
    q=quad(phi,0,i)
    y.append(q[0])
plt.plot(x,y)
plt.show()


# In[ ]:


mu=5
sigma=1
x=np.linspace(mu-3*sigma,mu+3*sigma,100)
y=[]
for i in x:
    q=quad(phi2,0,i,args=(mu,sigma))
    y.append(q[0])
plt.plot(x,y)
plt.show()


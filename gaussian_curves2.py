
# coding: utf-8

# In[89]:


import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math


# In[90]:


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


# In[131]:


mu = 10
variance = 1
sigma = math.sqrt(variance)
x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
plt.plot(x,mlab.normpdf(x, mu, sigma),'r-')
plt.plot(x,gaussian(x, mu, sigma),'g-')
plt.plot(mu,gaussian(mu, mu, sigma),'go')
plt.plot(mu-sigma,gaussian(mu-sigma, mu, sigma),'go')
plt.plot(mu+sigma,gaussian(mu+sigma, mu, sigma),'go')
plt.show()


# In[92]:


x_values = np.linspace(-3, 3, 120)
for mu, sig in [(-1, 1), (0, 2), (2, .2)]:
    plt.plot(x_values, gaussian(x_values, mu, sig))
plt.show()


# In[93]:


from scipy.integrate import quad

def integrand(x, a, b):
    return a*x**2 + b

def f(x):
    return 2*x


# In[94]:


a = 2
b = 1
I = quad(integrand, 0, 1, args=(a,b))
print(I)


# In[137]:


I = quad(phi, -np.inf, 1)
print(I)


# In[96]:


I = quad(phi,-np.inf, 0)
print(I)


# In[97]:


I = quad(phi, -np.inf, 1)
print(I)


# In[98]:


I = quad(f, 0, 1)
print(I)


# In[99]:


x=np.linspace(-1,1,100)
#print(x)


# In[100]:


y=[]
for i in x:
    q=quad(f,0,i)
    y.append(q[0])


# In[101]:


plt.plot(x,y)
plt.show()


# In[141]:


x=np.linspace(mu-5,mu+5,100)
y=[]
mu=5
for i in x:
    q=quad(phi,-np.inf,i-mu)
    y.append(q[0])
plt.plot(x,phi(x-mu))
plt.plot(x,y)
plt.show()


# In[133]:


mu=5
sigma=1
p=3

x=np.linspace(mu-3*sigma,mu+3*sigma,100)
y=[]
for i in x:
    q=quad(phi2,0,i,args=(mu,sigma))
    y.append(q[0])
plt.plot(x,y)
plt.plot(x,phi(x-mu))
plt.plot(mu,quad(phi2,0,mu,args=(mu,sigma))[0],'ro')
plt.plot(mu-sigma,quad(phi2,0,mu-sigma,args=(mu,sigma))[0],'bo')
plt.plot(mu+sigma,quad(phi2,0,mu+sigma,args=(mu,sigma))[0],'bo')
plt.show()


# In[112]:


phi2(p,mu,sigma)


# In[113]:


quad(phi2,0,p,args=(mu,sigma))


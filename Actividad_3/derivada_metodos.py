#!/usr/bin/env python
# coding: utf-8

# # <center> Métodos para calcular la derivada numérica <center>

# ## Derivada hacia adelante: (Error de h^2)
# $$f'(x)\simeq \frac{f(x+h)-f(x)}{h}$$
# ## Derivada hacia atrás:
# $$f'(x)\simeq \frac{f(x)-f(x-h)}{h}$$
# ## Derivada con diferencia central: (resto h^3)
# $$f'(x)\simeq \frac{f(x+h)-f(x-h)}{2h}$$

# In[11]:


import numpy as np
import matplotlib.pyplot as plt


# In[12]:


def f(x,n,A1=1e-6,A2=1e-6,A=1):#n: nos permitirá movernos entre una función y otra
    if(n==1):
        return A1/x**6-A2/x**12
    elif(n==2):
        return A*np.cos(x)


# In[13]:


x=np.pi
n=2
f(x,n)


# In[14]:


def derivada_adelante(x,n,h):
    return (f(x+h,n)-f(x,n))/h


# In[15]:


x=np.linspace(0.0001,10,100)# 100 puntos entre 0.01 y 10
n=2# primero 0.1, luego 0.05, 1 , 1e-3,1-e4
h=0.1
print("Función")
print(f(x,n))
df=derivada_adelante(x,n,h)
print("Derivada")
print(np.shape(df))


# In[32]:


plt.figure()
plt.plot(x,f(x,n),label="Acos(x)")
#plt.figure()
plt.plot(x,df,label="derivadanp_numerica")
plt.savefig("func1.png")
##########3
plt.figure()
plt.plot(x,f(x,n),label="Acos(x)")
#plt.figure()
plt.plot(x,df,label="derivadanp_numerica")
plt.savefig("func2.png")


# In[17]:


#derivada de forma analítica
def fp(x):
    return -np.sin(x)


# In[18]:


error=np.abs((fp(x)-derivada_adelante(x,n,h)))


# In[19]:


print("Gráfica error")
plt.scatter(x,error)


# ## Newton's Method
# $$f(x^{*})=0$$
# Escogemos un punto inicial $x_0$ tal que:
# $$x^{*}=x_0+h$$
# Entonces:
# $$f(x*)=f(x_0+h)\simeq f(x_0)+f'(x_0)h$$
# Despejamos $h$ teniendo en cuenta que $f(r)=0$:
# $$h=-\frac{f(x_0)}{f'(x_0)}$$
# Hallamos $x^{*}$ en términos de $x_0$ y h:
# 
# $$x^{*}=x_0+h\simeq x_0-\frac{f(x_0)}{f'(x_0)}$$
# En realidad el término derecho es una aproximación de la raíz $x^{*}$, a esta la llamamos $x_1$:
# $$x_{1}=x_0-\frac{f(x_0)}{f'(x_0)}$$
# Ahora tomamos x_{1} para hallar una mejor:
# $$x_{2}= x_1-\frac{f(x_1)}{f'(x_1)}$$
# y así sucesivamente ($n$ veces):
# $$x_{n+1}=x_{n}-\frac{f(x_{n})}{f'(x_{n})}$$

# In[20]:


def fp(x,n,A1=1,A2=1,A=1):
    if(n==1):
        return -6*A1/x**7+12*A2/x**13
    if(n==2):
        return -A*np.sin(x)


# In[21]:


def fpp(x,n,A1=1,A2=1,A=1):
    if(n==1):
        return 6*7*A1/x**8-12*13*A2/x**14
    if(n==2):
        return -A*np.cos(x)


# In[29]:


def Newton(x0,n,error):
    xant=x0
    xsig=xant-fp(xant,n)/fpp(xant,n)
    while(np.abs(xsig-xant)>error):
        xant=xsig
        xsig=xant-fp(xant,n)/fpp(xant,n)
        #print(xant,xsig)
    return xsig


# In[36]:


x0=-0.5
n=2 #cos
error=1e-6
Newton(x0,n,error)


# In[ ]:





# In[ ]:





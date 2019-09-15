#!/usr/bin/env python
# coding: utf-8

# # This script is an illustration of Buckingham  $\Pi$  theorem

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# 

# ## Fahima Nowrin provided the algorithm to me from Kamrul sir

# In[1]:


markers = ['.', '2', '*', 'v','+', 'x', 'D', 's', 'H', '^']


# #### Area vs arm plot

# In[14]:



k = 0
fig = plt.figure(figsize=(5,5), dpi=300)
for i in range(2, 10):
    a = np.ones(100)*i
    b = np.linspace(0.01, 20, 100)
    c = np.sqrt(a**2 + b**2)
    S = a*b/2
#     plt.plot(b, S, label='a={}'.format(i)) # colorful
    plt.plot(b, S, color='k', linewidth=0.5) # colorful
    plt.plot(b, S, 'o', label='a={}'.format(i), color='k', marker=markers[k], markersize=3)
    k += 1
    pass

plt.legend()
plt.xlabel(r'$b$')
plt.ylabel(r'$S$')
plt.xlim(0, 6)
plt.ylim(0, 20)
fig.tight_layout(pad=0.7)
filename = 'area_vs_arm.eps'
plt.savefig(filename)


# #### Data Collapse

# In[9]:


k = 0
fig = plt.figure(figsize=(5,5), dpi=300)
for i in range(2, 10):
    a = np.ones(100)*i
    b = np.linspace(1, 20, 100)
    c = np.sqrt(a**2 + b**2)
    S = a*b/2
#     plt.plot(b/c, S/c**2, label='a={}'.format(i)) #  color graphs
    plt.plot(b/c, S/c**2, 'o', label='a={}'.format(i), color='k', marker=markers[k], markersize=3)
    k += 1
    pass

plt.legend()
plt.xlabel(r'$b/c$')
plt.ylabel(r'$S/c^2$')
fig.tight_layout(pad=0.7)
filename = 'data_collapse.eps'
plt.savefig(filename)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv


# In[15]:


arr=[]
with open('C:/Users/user/Downloads/example.csv', newline='') as csvfile:
        plot = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in plot:
            arr.append(row)

print(arr[1][2])


# In[ ]:





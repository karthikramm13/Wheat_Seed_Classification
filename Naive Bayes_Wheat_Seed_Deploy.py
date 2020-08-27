#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


ds = pd.read_csv("Wheat Seed.csv")
ds


# In[3]:


x = ds.iloc[:,:-1]
y = ds.iloc[:,-1]


# In[4]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=42)


# In[5]:


from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()
gnb.fit(x_train,y_train)
y_pred=gnb.predict(x_test)
y_pred


# In[13]:


import pickle
file = open('Wheat_seed.pkl', 'wb')

pickle.dump(gnb, file)


# In[16]:


file = open('Wheat_seed.pkl', 'rb')
new_data = pickle.load(file)


# In[17]:


new_data


# In[19]:


Wheat_seed = pickle.load(open('Wheat_seed.pkl','rb'))
print(Wheat_seed.predict([[11.23, 12.82, 0.8594, 5.089, 2.821, 7.524, 4.957]]))


# In[ ]:





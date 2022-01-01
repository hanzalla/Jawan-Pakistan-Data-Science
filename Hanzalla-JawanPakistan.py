#!/usr/bin/env python
# coding: utf-8

# In[6]:


from datetime import datetime
now=date.today()
print(now)


# In[18]:


current=datetime.today()
currentTime=current.strftime("%H:%M:%S")
print("current Date: "+str(now),"Current Time: "+currentTime)


# In[19]:


from platform import python_version
print("My Python Version is: "+str(python_version()))


# In[20]:


import math as m
print (m.pi)


# In[31]:


radius=float(input("Enter radius of a circle in cm "))
ans=m.pi*radius**2
r=round(ans,2)
print("The Radius Of a circle = "+str(r)+"cm ,whose radius i= "+str(radius)+"cm")


# In[50]:


name= input("Enter Your First Name: ")[::-1]
lname= input("Enter Your Last Name: ")[::-1]
fname=name+lname
for i in fname:
    print (i[::-1], end=" ")


# In[52]:


number=int(input("Enter number: "))
number2=int(input("Enter second number: "))
print(number+number2)


# In[4]:


i=1
while i<7:
    string="hanzalla"
    i=i+1
    print('\t'+string)


# In[ ]:





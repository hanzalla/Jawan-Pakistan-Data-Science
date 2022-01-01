#!/usr/bin/env python
# coding: utf-8

# In[2]:


from datetime import date
now=date.today()
print(now)


# In[3]:


current=datetime.today()
currentTime=current.strftime("%H:%M:%S")
print("current Date: "+str(now),"Current Time: "+currentTime)


# In[4]:


from platform import python_version
print("My Python Version is: "+str(python_version()))


# In[11]:


pi=3.142


# In[13]:


radius=float(input("Enter radius of a circle in cm "))
ans=m.pi*radius**2
r=round(ans,2)
print("The Radius Of a circle = "+str(r)+"cm ,whose radius is= "+str(radius)+"cm")


# In[7]:



name= input("Enter Your First Name: ")[::-1]
lname= input("Enter Your Last Name: ")[::-1]
fname=name+lname
for i in fname:
    print (i[::-1], end=" ")


# In[8]:


number=int(input("Enter number: "))
number2=int(input("Enter second number: "))
print(number+number2)


# In[10]:


print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")


# In[ ]:





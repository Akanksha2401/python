#!/usr/bin/env python
# coding: utf-8

# # Question 1:

# In[6]:


a=int(input())

if a>90 and a<=100:
    print("|-----|")
    print("|  A  |")
    print("|-----|")
elif a>80 and a<=90:
    print("|-----|")
    print("|  B  |")
    print("|-----|")
elif a>70 and a<=80:
    print("|-----|")
    print("|  C  |")
    print("|-----|")
elif a>60 and a<=70:
    print("|-----|")
    print("|--D--|")
    print("|-----|")
elif a>50 and a<=60:
    print("|-----|")
    print("|--E--|")
    print("|-----|")
else:
    print("|-----|")
    print("| FAIL|")
    print("|-----|")


# # Question 2:

# In[2]:


import random
x=random.randint(1,250)
print(x)

if x<1 or x>250:
    print("Reduce your expectation for 20-20 Cricket")
else:
    z=int(input())
    if z in range(x-10,x+10):
        print("Close By, you are True Indian Fan!")
    else:
        print("You don't watch that much! :P ")
              


# # Question 3: 

# In[7]:


file =open("FCS.txt",'w');
print(file)
file.write("I love FCS")
file.close()


# In[8]:


print(file)


# In[9]:


file=open("Assignment.txt","r")
text=file.read()
print(text)
file.close()


# # Question 4:

# In[ ]:





# In[ ]:





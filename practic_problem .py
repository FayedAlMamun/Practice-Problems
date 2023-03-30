#!/usr/bin/env python
# coding: utf-8

# #keep 1st middle & last character
# 

# In[29]:


def keep1stMiddleLastCharacer(str):
    str=str[0]+str[len(str)//2]+str[-1]
    return str


# In[30]:


s=input("Write a string:")
str=keep1stMiddleLastCharacer(s)
print(str)


# #lowercase character come 1st

# In[45]:


def lowecaseCome1st(str):
    str=sorted(str)
    lowerpart=''
    upperpart=''
    for i in str:
        if (i.islower()):
            lowerpart=lowerpart+i
        else:
            upperpart=upperpart+i
    return lowerpart+upperpart
            


# In[46]:


s1=input("Write a string:")
str1=lowecaseCome1st(s1)
print(str1)


# #Count all letters, digits, and special symbols from a given string. 

# In[50]:


def countLetterDigitSymbols(str):
    char=0
    digit=0
    symbol=0
    for i in str:
        if(i.isalpha()):
            char+=1
        elif (i.isdigit()):
            digit+=1
        else:
            symbol+=1
    return char,digit,symbol


# In[58]:


s2=input("Write a string:")
str2=countLetterDigitSymbols(s2)
print(f"Char:{str2[0]}\nDigit:{str2[1]}\nSymbol:{str2[2]}")


# #Split a string on hyphens.

# In[60]:


def splitOnHyphens(str):
    str=str.split("-")
    return str
s3=input("Write a string:")
str3=splitOnHyphens(s3)
print(str3)


# #Reverse a given string.

# In[61]:


def stringReverse(str):
    s=''
    for i in range((len(str)-1),-1,-1):
        s+=str[i]
    return s
s4=input("Write a string:")
str4=stringReverse(s4)
print(str4)
        


# #Create a function that can add unlimited numbers (arguments).

# In[89]:


from functools import reduce
def addUnlimitedNumber(a,b,*args):
    l=list(args)
    l.append(a)
    l.append(b)
    add=reduce(lambda x, y: x + y, l)
    return add
s5=addUnlimitedNumber(0,1,1,2,4,2)
print(s5)


# In[ ]:





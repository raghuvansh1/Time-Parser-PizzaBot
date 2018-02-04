
# coding: utf-8

# DATA

# In[10]:


obj={'day':1,'date':1,'week':7,'fortnight':14,'month':1,'year':1,'decade':10,'century':100}

multi={'before':-1,'after':1,'later':1,'next':1,'previous':-1,'this':0,'last':-1}


drx_obj={'today':0,'tomorrow':1,'yesterday':-1}


days={'sunday':0,'monday':1,'tuesday':2,'wednesday':3,'thursday':4,'friday':5,'saturday':6}


# LEVELER

# In[11]:


date_lvler=[['year','decade','century'],['month'],
            ['day','date','week','fortnight','today','tomorrow','yesterday']]


# GET INPUT

# In[12]:


def get_ip():
    a=input('gimmie some input')
    a=a.lower()
    lis= a.split()
    return lis


# GET PRESENT DATE TIME

# In[13]:


import datetime
a=datetime.datetime.now()
a=str(a)
a=a.split()
date_now=a[0].split('-')
time_now=a[1].split(':')

for i in date_now:
    date_now[date_now.index(i)]=int(i)

for i in time_now:
    time_now[time_now.index(i)]=float(i)
    
# GET DAY    
import datetime
now = datetime.datetime.now()
day=now.strftime("%A")
day_now=day.lower()


# ALGO

# In[14]:



temp=999

#lis=get_ip()

#get ip
a=input()
lis=a.split()


    #creating and filling heap
big_heap=[]
for item in lis:
    if item in obj or multi or drx_obj:
        big_heap.append(item)
num=0
for item in big_heap:
        #if item is drx_obj
    if item in drx_obj:
        for grp in date_lvler:
            if item in grp:
                date_now[date_lvler.index(grp)]+=drx_obj[item]


        #if item is multi or obj

    if item in multi:
        if temp!=999:
            temp=temp*multi[item]
            for grp in date_lvler:
                if big_heap[num-1] in grp:
                    date_now[date_lvler.index(grp)]+=temp
                    temp=999
        else:
            temp=multi[item]


    if item in obj:
        if temp!=999:
            temp=temp*obj[item]
            for grp in date_lvler:
                if item in grp:
                    date_now[date_lvler.index(grp)]+=temp
                    temp=999
        else:
            temp=obj[item]
            
    num+=1
    
    answer=date_now
    
    


# In[15]:


answer


# In[8]:

print(date_now)
del date_now
del time_now


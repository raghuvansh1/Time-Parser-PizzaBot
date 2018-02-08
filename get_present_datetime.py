
# coding: utf-8

# In[ ]:


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


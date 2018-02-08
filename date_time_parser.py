
# coding: utf-8

# In[ ]:
import date_time_parser_data
from date_time_parser_data import *

import get_input_function
from get_input_function import *

import get_present_datetime
from get_present_datetime import *


#temp variable u will understand its importance later
temp=999

#lis=get_ip()

#get ip
a=input()
lis=a.split()

time_list=[1,2,3,6,7,8,9,10,11,12]
    #creating and filling heap
big_heap=[]
for item in lis:
    if item in obj or multi or drx_obj:
        big_heap.append(item)
num=0

length_heap=len(big_heap)

while num<length_heap:
        #if item is drx_obj
        
        
    if big_heap[num] in days:
        if temp==999:
            temp=0
        a=(days[day_now]-days[big_heap[num]])*-1
        if a>0 or a==0:
            date_now[2]+=a + temp*7
            
        if a<0:
            date_now[2]+=7+a +temp*7
        
        temp=999
        
    if big_heap[num] in drx_obj:
        for grp in date_lvler:
            if big_heap[num] in grp:
                date_now[date_lvler.index(grp)]+=drx_obj[big_heap[num]]


        #if item is multi or obj

    if big_heap[num] in multi:
        if temp!=999:
            temp=temp*multi[big_heap[num]]
            for grp in date_lvler:
                if big_heap[num-1] in grp:
                    date_now[date_lvler.index(grp)]+=temp
                    temp=999
        else:
            temp=multi[big_heap[num]]


    if big_heap[num] in obj:
        if temp!=999:
            temp=temp*obj[big_heap[num]]
            for grp in date_lvler:
                if big_heap[num] in grp:
                    date_now[date_lvler.index(grp)]+=temp
                    temp=999
        else:
            temp=obj[big_heap[num]]
            
            
    if big_heap[num] in obj_s:
        if temp!=999:
            temp=temp*obj_s[big_heap[num]]*int(big_heap[num-1])
            for grp in date_lvler:
                if big_heap[num] in grp:
                    date_now[date_lvler.index(grp)]+=temp
                    temp=999
        else:
            temp=obj_s[big_heap[num]]*int(big_heap[num-1])
            
            
    if big_heap[num] == 'a.m.':
        ttemp=big_heap[num-1]
        ttemp=ttemp.split(':')
        if len(ttemp)==1:
            time_now[0]=ttemp[0]
        if len(ttemp)==2:
            time_now[0]=ttemp[0]
            time_now[1]=ttemp[1]
            
    if big_heap[num] == 'p.m.':
        ttemp=big_heap[num-1]
        ttemp=ttemp.split(':')
        if len(ttemp)==1:
            time_now[0]=str(int(ttemp[0])+12)
            time_now[1]=0
            time_now[2]=0
        if len(ttemp)==2:
            time_now[0]=str(int(ttemp[0])+12)
            time_now[1]=ttemp[1]
            time_now[2]=0
            
                
            
    num+=1
    
 
    
if date_now[1]>12:
    mtemp=date_now[1]
    date_now[1]%=12
    date_now[0]+=(mtemp/12)+1
    
if date_now[1]==(1 or 3 or 5 or 7 or 8 or 10 or 12) and date_now[2]>31:
    dtemp=date_now[2]
    date_now[2]%=31
    date_now[1]+=(dtemp/31)+1
    
    
if date_now[1]==(4 or 6 or 9 or 11) and date_now[2]>30:
    dtemp=date_now[2]
    date_now[2]%=30
    date_now[1]+=(dtemp/30)+1
    
    
if date_now[1]==2:
    if ((date_now[0]%4==0 and date_now[0]%100!=0) or date_now[0]%400==0):
        if date_now[2]>29:
            dtemp=date_now[2]
            date_now[2]%29
            date_now[1]+=(dtemp/29)+1
    else:
        if date_now[2]>28:
            dtemp=date_now[2]
            date_now[2]%28
            date_now[1]+=(dtemp/28)+1






print(date_now)
print(time_now)


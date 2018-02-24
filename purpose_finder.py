
# coding: utf-8

# DATASET

# In[38]:


data={'meet':'note','meeting':'note','wedding':'note','function':'note','alarm':'note','funeral':'note','ceremony':'note','party':'note','vacations':'note','holidays':'note','holiday':'note','break':'note','trip':'note','tour':'note','travel':'note','travelling':'note',
     'pizza':'food','dominos':'food','pizzahut':'food','hungry':'food','hunger':'food','lunch':'food','dinner':'food','breakfast':'food','kathi':'food','khana':'food','bhojan':'food','bhook':'food','pet':'food','stomach':'food','shop':'food','nashta':'food','restaurant':'food','hotel':'food','dhaba':'food','canteen':'food','cafe':'food','motel':'food','inn':'food','cuisine':'food','multicuisine':'food','bakery':'food','chopati':'food','khana':'food','khane':'food',
      'movie':'movie','theater':'movie','ticket':'movie','show':'movie','cinema':'movie','multiplex':'movie','picture':'movie','cine':'movie','screen':'movie','talkies':'movie','screenplay':'movie','cartoon':'movie','opera':'movie','hollywood':'movie','bollywood':'movie','film':'movie','films':'movie','jhilli':'movie','chitra':'movie','chalchitra':'movie','pardha':'movie','parda':'movie','philam':'movie',


# INPUT

# In[41]:


ip=""
iplist=ip.split()


# PURPOSE ALGO

# In[42]:


purpose='none'
for item in iplist:
    try:
        purpose=data[item]
    except KeyError:
        continue

if purpose=='none':
    print('I did not understand')
else:
    print(purpose)


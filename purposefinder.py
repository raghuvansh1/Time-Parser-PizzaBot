# import Voice
# from Voice import *

data={'meet':'note','meeting':'note','wedding':'note','function':'note','alarm':'note','funeral':'note','ceremony':'note','party':'note','vacations':'note','holidays':'note',
      'holiday':'note','break':'note','trip':'note','tour':'note','travel':'note','travelling':'note','note':'note','milna':'note','mil':'note','milenge':'note','milap':'note',
      'milunga':'note','shaadi':'note','baarat':'note','lagan':'note','tyohar':'note','maihar':'note','jalsa':'note','ghadi':'note',
      'samaaroh':'note','jhasan':'note','chuttiyan':'note','rasham':'note','vidhi':'note','samarambh':'note','avdhi':'note','tatkal':'note','kal':'note','ghumna':'note','ghumne':'note',
      'traveller':'note','paryatan':'note','utsav':'note','chutti':'note','weekend':'note','avkash':'note','avdhi':'note','ghumenge':'note','yatra':'note','safar':'note',
      'dohra':'note','brahman':'note',
      
      'pizza':'food','dominos':'food','pizzahut':'food','hungry':'food','hunger':'food','lunch':'food','dinner':'food','breakfast':'food','kathi':'food','khana':'food','bhojan':'food',
      'bhook':'food','pet':'food','stomach':'food','shop':'food','nashta':'food','restaurant':'food','hotel':'food','dhaba':'food','canteen':'food','cafe':'food','motel':'food','inn':'food',
      'cuisine':'food','multicuisine':'food','bakery':'food','chopati':'food','khana':'food','khane':'food','roll':'food','bhookh':'food','bhookha':'food','food':'food',
      
      'movie':'movie','theater':'movie','ticket':'movie','show':'movie','cinema':'movie','multiplex':'movie','picture':'movie','cine':'movie','screen':'movie','talkies':'movie','movie':'movie',
      'screenplay':'movie','cartoon':'movie','opera':'movie','hollywood':'movie','bollywood':'movie','film':'movie','films':'movie','jhilli':'movie','chitra':'movie','chalchitra':'movie',
      'pardha':'movie','parda':'movie','philam':'movie','chalachitra':'movie','sinemaaghar':'movie','drome':'movie',
      
      'pool':'game','snooker':'game','tt':'game','tennis':'game','fooseball':'game','carrom':'game','carromboard':'game','chess':'game','chessboard':'game','khelna':'game',
      'khel':'game','game':'game', }
# INPUT

# In[41]:


ip=input()
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
    if purpose == 'note':
        print("Do you want to save a note?")
    elif purpose == 'food':
        print("Do you want to order food?")
    elif purpose == 'movie':
        print("Do you want to book a movie ticket?")
    elif purpose == 'game':
        print("Do you want to book a seat for a game?")

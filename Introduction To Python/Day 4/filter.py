mynames =[
    {'name':'Fahim','age':25},
    {'name':'kawshik','age':12},
    {'name':'Tonmoy','age':56},
    {'name':'Arbs','age':40}
]

less_30 = filter(lambda a : a['age']<30,mynames) 
print(list(less_30))

less_30 = filter(lambda mynames:mynames['age']%5==0,mynames) 
print(list(less_30))
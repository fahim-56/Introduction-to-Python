# value with key

def Jog_koro(**kargs):
    sum = 0
    for key ,value in kargs.items():
        print(key,value)
        # sum += kargs[key]
        sum += value
    return sum
print(Jog_koro(x=5,y=10,z=5))



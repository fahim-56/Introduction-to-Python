name="Fahim Chowdhury"
name1='Fahim Chowdhury'
name2 =""" 
          Fahim
                Asharaf
                        Chowdhury"""

# print(name)
# print(name1)
# print(name2)

name3='Fahim\'s Book'
# print(name3)
# print(name3[2:5])
# print(name3[-3])
# print(name3[::-1])

# # name3[0]='k' Doesn't support sring to change

# if 'him' in name3:
#     print("Ase")

# print(name1.upper())
# print(name1.lower())
# print(name1.split())

# print(name1.replace('F','Ph'))
# print(name1.strip())
# id =29
# text=f"Nam ki tomar,Sagol naki {id}"
# print(text)

# dam = 50
# txt=f"Eidar dam koto...? -{dam:.2f} Taka"
# print(txt)


# table= str.maketrans("F","A")
# print(name2.translate(table))

# x="Fahi"
# y="Arbs"
# table= str.maketrans(x,y)
# print(name2.translate(table))


table= str.maketrans("FC","AB")
print(name2.translate(table))
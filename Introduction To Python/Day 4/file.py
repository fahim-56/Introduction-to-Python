with open("file.txt",'w')as file:
    file.write("First text line printing...\n")

with open("file.txt",'a')as file2:
    file2.write("one text line appending...\n")

with open("file.txt",'r')as file:
    name = file.read()
    print("reading file...")


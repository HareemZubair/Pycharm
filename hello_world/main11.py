# fILE i/o

file1 = open("arry.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("My name is hareem","UTF-8"))
file1.close()
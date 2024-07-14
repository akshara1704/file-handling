f=open("addingloop.txt","a")
n=int(input("enter number of line you want to add= "))
for i in range(0,n):
    line=input("enter your message= ")
    f.write(line)
    f.write("\n")
f.close()
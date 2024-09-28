tup=(1,5,6,2,1,8,9)
print(tup)
list=[]
print("repeated element in given tuple")
for i in range(0,len(tup)):
   if tup.count(tup[i])>1:
    if tup[i]not in list:
        list.append(tup[i])
        print(tup[i])
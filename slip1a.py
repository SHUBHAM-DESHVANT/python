def delete(repeat):
    list1=[]
    for n in repeat:
        if n not in list1:
            list1.append(n)
    return list1
repeat=[4,5,4,6,7]
print(delete(repeat))

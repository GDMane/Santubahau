
print("Shree Swami Samarth")
print("Collections (array)")

gmList = ['ganesh', 'ganesh', 'gmList']#duplicate allowed

print(gmList[0])#single object print using index
print("--------------")

'''
gmList.reverse()
print(gmList)#reverce elements in original refrance
print("--------------")
'''

gmList[0]="myChange"
print(gmList)#update on any particular index
print("--------------")

gmList.append("myAppend")
print(gmList)#Append object at the end /Last index
print("--------------")

gmList.pop(1)
print(gmList)#delete any perticular index object
print("--------------")

gmList.insert(1,"myInsertTest")
print(gmList)
print("--------------")

gmList.remove("gmList")
print(gmList)#remove perticular object
print("--------------")

gmList1 = gmList.copy()
print(gmList1)
print(gmList)
print("--------------")

gmList.extend("1")
print(gmList)
print("--------------")

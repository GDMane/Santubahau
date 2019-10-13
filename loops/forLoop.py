
gm = [1,2,3,4]
gm1 = ["Ganesh", "Mane"]

for item in gm:
    print(item)


for item in gm:   #nested for
    for item1 in gm1:
        print(item,item1)


for item in range (0,2):
    print (item)

for item in range (0,6,2):
    print(item)
else:
    print("After FOR loop else part executed")


for item in "Ganesh":
    print(item)

gmDict = {"Key1" : "Ganesh",
          "Key2" : "Mane"}
gmList = []

for k in gmDict:
    print ("Key is : ",k)
    gmList.append(k)

print("GM List contained : ", gmList)

for k,v in gmDict.items():
    print("Key is : ", k)
    print("Value is :", v)

print("Shree Swami Samarth")
print("Collections (array)")

gmList = ['ganesh', 'ganesh', 'gmList']#duplicate allowed
gmTuple = ('ganesh', 'ganesh', 'gmtuple')#duplicate allowed
gmSet = {'ganesh', 'gmset','ganesh'}#duplicate not allowed, 'set' object does not support indexing
gmDict = {
    "ganesh": "mane",
    "birthyear" : 1994,
    "ganesh1":"mane1",
}#duplicate not allowed, key value pair

'''print(gmList[0])
print("--------------")
print(gmTuple[0])
print("--------------")
print(gmSet)
print("--------------")
print(gmDict)'''

gmDict["ganesh1"] = "updateTest"

print(gmDict)
print("--------------")

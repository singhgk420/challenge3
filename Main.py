import json

def  extractkey(obj , key):
    if not isinstance(obj , dict):
        obj = json.loads(obj)
    keyList = key.split('/')
    flag = True

    for i in range(0, len(keyList)):
        if keyList[i] in obj.keys():
            obj = obj[keyList[i]]
        else:
            flag = False
            break
    return  flag,obj


obj = input("Enter object = ")
key = input("Enter key = ")
status,result = extractkey(obj, key)

if status:
    print("output = " + str(result))
else:
    print("invalid key format")



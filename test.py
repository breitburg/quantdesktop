import psutil
listOfProcessNames = list()


for proc in psutil.process_iter():
    pInfoDict = proc.as_dict(attrs=['name', 'memory_percent', 'username'])
    if type(pInfoDict['memory_percent']) != float: continue
    listOfProcessNames.append(pInfoDict)


sorted_x = sorted(listOfProcessNames, key=lambda i: i['memory_percent'])
for item in :
    print(item)
name=input("Enter your name:")
i=0
var="e"
while i < len(name):
    if name[i] not in var:
        var+=name[i]
    print(f"{name[i]} : {name.count(name[i])}")
    i+=1
__author__ = 'PrinceSallu'
myD = {}
myD["will"] = "123-4567"
myD["james"] = "890-1234"
myD["jay"] = "567-8901"

print(myD["will"])
print("")
print(myD.get("josh"))
print("")

del myD['james']
print(myD)
print("")

myD.keys()
list(myD.keys())

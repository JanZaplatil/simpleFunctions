'''def najvecjeStevilo(aList):
  sestevek =  0
  for a in aList:
    sestevek = sestevek + a
  print(sestevek)


elementi = [1,2,4,5,]

najvecjeStevilo(elementi)



stevila = []
for c in range(7):
  c = int(input("vsesi st: "))
  stevila.append(c)
print(stevila)

najvecjeStevilo(stevila)'''





def izpis(aList):
  naj = 0
  for d in range(len(aList)):
    if aList[d] > aList[naj]:
      naj = d
  print(" najvecje stevilo je ",aList[naj])

  naj = 0
  for d in range(len(aList)):
    if aList[d] < aList[naj]:
      naj = d
  print(" najmanjse stevilo je ",aList[naj])
   
  sestevek = 0 
  for d in range(len(aList)):
    sestevek = sestevek + aList[d]
  print("sestevek vseh stevil je ", sestevek)


stevila = []
for c in range(7):
  c = int(input("vsesi st: "))
  stevila.append(c)
print(stevila)

izpis(stevila)


'''aList = [5,6,7,8,9]

for d in range(len(aList)):
  print(d)
  print(aList[d])'''
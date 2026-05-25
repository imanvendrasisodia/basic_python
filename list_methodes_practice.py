# list methode are built -in function  used  to modify and manage list data..  it is muttable (changes possible in original list)

a = [1,5,8,3,4,6,875]
print(a.sort(),a)  #ascending order
print(a.append(89),a)   #ek value add end the end
print(a.insert(2,9),a)  #specific place add
print(a.remove(5), a)   # value remove
a.extend([10,150])    #multiple value add
print((a))  
a.pop()    #last/index remove
print(a)
print(a.count(8))  #counting
print(a.index(8))  #position batana
a.reverse()   #ulta karta
print(a)
b = a.copy()   # duplicate list
print(b)
a.clear ()   #empty list
print(a)

print(type(a)) #type batata he..
print(a)

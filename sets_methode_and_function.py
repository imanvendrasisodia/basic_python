#set is a data type of python it has store multiple values and it is unorderd and not allow to duplicate value or it is mutable.:
   #store uniqe value only; fast searching ; remove duplicates:
number = {1,5,6,2,5}

print(number)
number.add(10) #add one value
print(number)

number.update([20,30])  #add multiple value
print(number)

number.remove(5) #remove value output error 
print(number)

number.discard(20) #remove value output nothing
print(number)

number.pop() #remove random value
print(number)

num1= number.copy() #duplicate create karta he..
print(num1)

basic = {1,9,2,7,6,852,41} #to create empty set:
basic.clear()
print(basic)

# set operations:::::

aa = {1,2,5,3,6,4,2,3,8,9}
ab= {6,3,5,2,2,5,4,5,7,85,2,3}

print(aa.union(ab))  #combine set

print(aa.intersection(ab)) #common value
  
print(aa.difference(ab)) #different values:

print(aa.symmetric_difference(ab)) #symetric difference


# imp functions:::::::;


print(len(aa))
print(max(ab))
print(min(ab))
print(type(aa))
print(sum(ab))
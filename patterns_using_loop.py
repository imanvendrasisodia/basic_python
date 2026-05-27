# first star pattern
#   *
#  ***
# *****

num1 = int(input("enter a number:: "))
for i in range(1,num1+1):
    print(" "* (num1-i),end="")
    print("*"*(2*i-1))

#second star pattern::
#*
#**
#***    
#****

num2 = int(input("enter a number:: "))
for i in range(1,num2+1):
    print("*"*i)
    

# third star pattern 
#  ***
#  * *
#  ***

num3 = int(input("enter a number:: "))
for i in range(1, num3+1):
    if(i ==1 or i==num3):
        print("*"*num3)
    else:
        print("*",end="")
        print(" "*(num3-i), end="")
        print("*",end="")
        print("")  
          

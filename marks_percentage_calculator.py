    # marks percentage calculator

name = input("enter your name: ")

sub1 = int(input("enter subject 1 marks: "))
sub2 = int(input("enter subject 2 marks: "))
sub3 = int(input("enter subject 3 marks: "))
sub4 = int(input("enter subject 4 marks: "))
sub5 = int(input("enter sbject 5 marks: "))

total_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (total_marks / 500) *100

print("total marks obtained", name, "out of 500 is : ", total_marks)
print("total percentage out of 100 is: ", percentage)
print("thank you for using this calculator Mr.", name)
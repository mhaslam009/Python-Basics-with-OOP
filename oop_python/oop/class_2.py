#ifelse-loop-list


#test1: Use while and for loop to print out list
list_1=[0,-1,True,8.54,"hfsa"]
for i in list_1:
    print(f"for loop lists:{i}")
index=0
while index < len(list_1):
    print(f"while loop list:{list_1[index]}")
    #since you didn't specify how to stop the program the program remain onging
    #since i used index variable as the condition for loop to continue, make changes to it
    index+=1

#test2:Modifying List Elements

print("____________________________________________________________________________________")
list_2=["12",23,True,1.5]
for i in list_2:
    list_2=i*2
    print(f"f_loop_list:{list_2}")


#loop use on dict
student_scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "David": 95,
    "Eve": 88
}
#print out all the elements
for i in student_scores:
    print(i)
#only keys printed out

print("__________________________________________________")
for i in student_scores.values():
    print(i)
print("..................................................................")
#only with specified key
for i in student_scores.items():
    x,y=i
    print(f"Key:{x}     Value:{y}")

#problems:
#create a dictionary of student(key) and their score(value)
#since loop keys ko chalata hai toh loop se input desakta hun
#ussi loop main key update krta rahun aur assign krdun












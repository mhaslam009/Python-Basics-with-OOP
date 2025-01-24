from parent_class import My_class_04
from child_class01 import Iphone_models

#CREATE OBJECTS
My_class_04.ins_csv_file()

#name attribute encapsulation and restriction
print(My_class_04.list_of_objects)
item1=My_class_04("innername",890,99) #initialize object
item1.name="outername"
print(item1.name)

#encapsulation
#price attribute incementation
item2=My_class_04("innerpeace",900,9)
print(item2.price)
print("...........")
item2.apply_increment(0.5)
print(item2.price)
print("..........")
print(item1.price)
item1.discounting()

print(item1.price)
print(".........")
item1.discount=0.1 #overriding doscount from 50% to 90%
item1.discounting()
print(item1.price)
print("-----")

#abstraction:
#print(item1.__connect())
#now connect method cannot be accesed because we privatized in class method just below ABSTRACTION comment
 
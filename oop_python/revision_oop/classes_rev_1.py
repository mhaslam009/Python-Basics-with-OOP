#Lec01: classes, object attributes and methods creation

#create class
class Shop:
    #method creation
    def shelf_value_calculation(self,x,y):
        return x*y
    pass
#create objects/instances
shelf_01 = Shop()
#create attributes
shelf_01.name="pos_01"
shelf_01.dimension=60
shelf_01.price=600
#method calling
shelff_val=shelf_01.shelf_value_calculation(shelf_01.price,shelf_01.dimension)

print(shelf_01) #print objects
print(shelf_01.price) #print attributes
print(shelff_val)



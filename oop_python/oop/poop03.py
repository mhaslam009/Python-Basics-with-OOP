import csv

class My_class_04:  # class
    discount = 0.7  # class attribute
    list_of_objects = []

    def __init__(self, name: str, price: float, quantity: int):
        # validate recieving arguments
        assert price >= 0, f"{price} is lower than 0 "
        assert quantity >= 0, f"{quantity} is lower than 0 "
        self.name = name
        self.price = price
        self.quantity = quantity

        # saving objects to list_of_objects
        My_class_04.list_of_objects.append(self)

    @classmethod
    def ins_csv_file(cls):
        with open('database.csv','r') as f:
            reader_dict_of_data=csv.DictReader(f) #this method is going to read content as list of dictionaries
            #to convert it into a list
            items = list(reader_dict_of_data)
            #now we have dictionaries into a list
            print(items)
            print("______________________")
            #all dictionories form a list
            for item in items:
                print(item)
            #to create exact instances from list and access it
            for i in items: #here we will be reading of dictionary
                My_class_04( #we are craeting tuple
                    name=str(i.get('name')), #passes the column heading or passes key
                    price = float(i.get('price')),  # passes the column heading or passes key
                    quantity = float(i.get('quantity')),  # passes the column heading or passes key
                )
    @staticmethod
    def is_integer(num): #output the floats
        if isinstance(num,float): #if num is float
            return num.is_integer() #count out the floats
        elif isinstance(num,int):
            return True #input numbers are integer
        else:
            return False




    def calculation(self):
        return self.price * self.quantity

    def discounting(self):
        self.price = self.price * self.discount

    def __repr__(self):
        return f"object('{self.name}',{self.price},{self.quantity})"


# objects craeted
#entry_01 = My_class_04("Iphone", 10000, 10)
#entry_02 = My_class_04("Iphone", 200, 200)
#entry_03 = My_class_04("Iphone", 20, 2000)
#entry_04 = My_class_04("Iphone", 600, 4)
#entry_05 = My_class_04("Iphone", 0, 100000)

# access attributes
#print(entry_01.name)
#print(entry_02.price)
#print(entry_03.quantity)
#print("_______________")

# access methods
#print(entry_01.calculation())
#print(entry_04.calculation())
#print("_______________")

#print(entry_01.price)
# access class attribute->discount() method
#entry_01.discounting()  # it changes the price of entry_01
#print(entry_01.price)  # extract the attribute which have gone through a change
# entry_01 price has changed
#print(entry_02.price)
# entry_02 price have not changed because we didnt apply discounting method

#print("_________________")
#print(entry_04.price)
# overriding the class attribute which is discount variable then using discounting() method
#entry_04.discount = 0.5  # 50% discount overriding class attribute discount variable
#entry_04.discounting()
#print(entry_04.price)
print("____________________")

# access list of objects
#print(My_class_04.list_of_objects)
# access attribute from object

# print(My_class_04.list_of_objects.name)
# failed

# again access attribute from a list of object
#for i in My_class_04.list_of_objects:
#    print(i.name)  # name attribute from objects list
#    print(i.quantity)  # quantity object from a list of objects
#    print("_____________")


#access class method
My_class_04.ins_csv_file()

#access class objects by applying method
print(My_class_04.list_of_objects)

print(My_class_04.is_integer(90))
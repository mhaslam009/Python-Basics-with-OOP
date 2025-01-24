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

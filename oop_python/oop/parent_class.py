import csv


class My_class_04:  # class
    discount = 0.7  # class attribute
    list_of_objects = []

    def __init__(self, name: str, price: float, quantity: int):
        # validate recieving arguments
        assert price >= 0, f"{price} is lower than 0 "
        assert quantity >= 0, f"{quantity} is lower than 0 "
        self.__name = name
        self.__price = price
        self.quantity = quantity

        # saving objects to list_of_objects
        My_class_04.list_of_objects.append(self)

    #ENCAPSULATION

    #restrict price attribute
    @property
    def price(self):
        return self.__price
    #increment price attribute
    def apply_increment(self,increment_value):
        self.__price=self.price+self.__price*increment_value


    def discounting(self):
        self.__price = self.__price * self.discount

    @property #restring name attribute
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        if len(value)>10:
            raise Exception("The length of setting character is more than 10 words!")
        else:
            self.__name = value

    @classmethod
    def ins_csv_file(cls):
        with open('E:\CAREER_DATA\python_dev\\database.csv', 'r') as f:
            reader_dict_of_data = csv.DictReader(f)  # this method is going to read content as list of dictionaries
            # to convert it into a list
            items = list(reader_dict_of_data)
            # now we have dictionaries into a list
            print(items)
            print("______________________")
            # all dictionories form a list
            for item in items:
                print(item)
            # to create exact instances from list and access it
            for i in items:  # here we will be reading of dictionary
                My_class_04(  # we are craeting tuple
                    name=str(i.get('name')),  # passes the column heading or passes key
                    price=float(i.get('price')),  # passes the column heading or passes key
                    quantity=float(i.get('quantity')),  # passes the column heading or passes key
                )

    @staticmethod
    def is_integer(num):  # output the floats
        if isinstance(num, float):  # if num is float
            return num.is_integer()  # count out the floats
        elif isinstance(num, int):
            return True  # input numbers are integer
        else:
            return False



    def calculation(self):
        self.__price = self.__price * self.quantity
        return self.__price

    def calculation_for_broken(self):
        self.quantity = self.quantity - self.broken_phones
        self.broked_price = self.__price * self.quantity
        return self.broked_price



    def __repr__(self):
        # return f"My_class_04('{self.name}',{self.price},{self.quantity})"
        return f"{self.__class__.__name__}('{self.name}',{self.__price},{self.quantity})"

    #ABSTRACTION
    def __connect(self,smpt_server):
        pass

    def __prepare_body(self):
        return f"""
    HELLO JHON. WE HAVE WE WILL {self.name} and {self.price}
    Regards ganjee"""

    def __send(self):
        pass
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()
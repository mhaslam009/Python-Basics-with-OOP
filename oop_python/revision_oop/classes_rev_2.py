# Lec#02:using constructor create a dynamic attribute,
# simeltanously learn the following:
# 1)mandatory parameters and non mandatory parameters & datatype check
# 2)dynamic attribute inside method working

class Shop:
    def __init__(self,name:str,space_for_items:int,size:float,value=0):
        """
        :param name:name of shelf of the shop, it is mandatory parameter
        :param space_for_items: space for items on a shelf of shelf of the shop, it is mandatory parameter
        :param size: size of shelf of the shop, it is mandatory parameter
        :param value: value of a shelf, it is also a default parameter, it is mandatory parameter
        """
        #assertion of arguments basically validate the attributes and imporve debugging
        assert space_for_items >= 0 , f"{space_for_items} not > 0"
        assert size >= 0, f"{size} not > 0"
        assert size <= 10, f"{size} not < 10"
        self.name = name
        self.space_for_items = space_for_items
        self.size = size
        self.value = value

    def shelf_value_calculation(self):
        self.value=self.size*self.space_for_items
        return self.value

shelf_01=Shop("Shelf A",50,5.0) #value passing through object to class's constructor

#how to access attributes
print(shelf_01.name)
print(shelf_01.space_for_items)
print(shelf_01.size)

#how to access method
print(shelf_01.shelf_value_calculation())
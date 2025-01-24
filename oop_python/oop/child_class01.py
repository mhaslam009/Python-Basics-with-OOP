from parent_class import My_class_04

# inheritence

class Iphone_models(My_class_04):
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0, broked_price=0):
        # validate recieving arguments

        assert broken_phones >= 0, f"{broken_phones} is lower than 0"
        assert broked_price >= 0, f"{broked_price} is lower than 0"

        # broken phones attribute which is new attribute
        self.broken_phones = broken_phones
        self.broked_price = broked_price
        # how to include the variables that have used in parent class
        super().__init__(
            name, price, quantity
        )

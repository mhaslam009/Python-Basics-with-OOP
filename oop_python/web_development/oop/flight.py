class Flight_passenger():
    def __init__(self, capacity):
        self.capacity = capacity #save the capacity of passengers which is actually the number of capacity of seats on flight
        self.passengers_name = [] #name of passengers in a list
    def add_passengers(self,name):
        if not self.open_seats():
            return False #return false when there are no open seats
        self.passengers_name.append(name) #only add passengers when there are open seats
        return True
    def open_seats(self):
        return self.capacity - len(self.passengers_name) #verify the number of seats in flight

flight = Flight_passenger(3)

list_of_pple=range(6)
list_of_pass = []
for passenger in list_of_pple:
    ind_pass = str(input("Enter Passenger Name:"))
    list_of_pass.append(ind_pass)
print(f"list of passengers:{list_of_pass}")
for person in list_of_pass:
    success_in_getting_seats = flight.add_passengers(person)
    if success_in_getting_seats:
        print(f"{person} Added to flight")
    else:
        print(f"{person} not added to flight")
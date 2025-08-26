# Assignment 1
# Class House

class House: 
    def __init(self, address, bedrooms, bathrooms, price):
        self.address = address
        self.bedrooms = bedrooms
        self.bathrooms = price
        self.sold = False

    def display_info(self): 
        print(f"Address: {self.address}")
        print(f"Bedrooms: {self.bedrooms}")
        print(f"Bathrooms: {self.bathrooms}")
        print(f"Price: KES {self.price:,.2f}")
        print(f"Status: {'Sold' if self.sold else 'Available'}")
    def update_price(self, new_price):
        self.price = new_price
        print(f"Price updated to KES {self.price:,.2f}")

    def mark_as_sold(self):
        self.sold = True
        print("The house has been marked as sold.")

my_house = House("123 Lakeview Rd, Kisumu", 3, 2, 8500000)
my_house.display_info()
my_house.update_price(8300000)
my_house.mark_as_sold()
my_house.display_info()



# Assignment two
# Class Vehicle 
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        return "The car is driving on the road."

class Plane(Vehicle):
    def move(self):
        return "The plane is flying in the sky."

def travel(vehicle: Vehicle):
    print(vehicle.move())

# Example usage
car = Car()
plane = Plane()

travel(car)    
travel(plane)  




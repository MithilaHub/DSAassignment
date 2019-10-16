class customer:
    def __init__(self, name, address, vehicle_no, contact_no, nic_no, customer_type = "general"):
        self.name = name
        self.address = address
        self.vehicle_no = vehicle_no
        self.contact_no = contact_no
        self.nic_no = nic_no
        self.customer_type = customer_type

class clean_park:
    def menu(self):
        while True:
            print("Welcome to clean clean park daily car service")
            print("select options")
            print("1 to register a new customer")
            print("2 to remove a new customer")
            print("3 to update customer details")
            print("4 to view customer details")
            print("5 to request for a service")
            print("6 to add the service to queue")
            print("7 to remove service from queue")
            print("8 to view service status")
            choice = int(input("select option: "))

menu2 = clean_park()
menu2.menu()
'''Your parking garage class should have the following methods:


- takeTicket
- This should decrease the amount of tickets available by 1
- This should decrease the amount of parkingSpaces available by 1


- payForParking
- Display an input that waits for an amount from the user and store it in a variable
- If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
- This should update the "currentTicket" dictionary key "paid" to True

-leaveGarage
- If the ticket has been paid, display a message of "Thank You, have a nice day"
- If the ticket has not been paid, display an input prompt for payment
- Once paid, display message "Thank you, have a nice day!"
- Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list)
- Update tickets list to increase by 1 (meaning add to the tickets list)

You will need a few attributes as well:
- tickets -> list
- parkingSpaces -> list
- currentTicket -> dictionary

'''


class ParkingGarage():
    #set up parking garage parking spaces and tickets
    #set up dictionary to be 

    currentTicket = {}
    hours_parked = 0
    lic_num = ""

    def __init__(self, spaces):
        self.tickets = [x for x in range(spaces)]
        self.parkingSpaces = [x for x in range(spaces)]


    def take_ticket(self):
        self.lic_num = input ("\nPlease enter your license plate number: ")
        self.hours_payment()
        self.tickets.pop()
        self.parkingSpaces.pop()
        self.currentTicket [self.lic_num] = [self.hours_parked, "not paid"]

    def hours_payment(self):
        self.hours_parked = int(input("\nHow many hours do you plan to park here today?"))

    def cash_owed(self):

        if self.currentTicket[self.lic_num][0] <= 1:
            amount_owed = 10
        elif self.currentTicket[self.lic_num][0] <= 3:
            amount_owed = 20
        elif self.currentTicket[self.lic_num][0] <= 5:
            amount_owed = 25
        elif self.currentTicket[self.lic_num][0] <= 8:
            amount_owed = 30

        return amount_owed

    
    def pay_for_parking(self):
        
        parking_flag = True
        print (f"\nYou owe {self.cash_owed()} dollars for parking {self.currentTicket[self.lic_num][1]} hours")
        parking_payment= input ("Can you pay this amount (y/n)").lower().strip()
        while parking_flag:
            if parking_payment == 'y':
                self.parking_paid()
                parking_flag = False
            elif parking_payment == 'n':
                payment_flag = True
                print("\nSo you can not pay for parking what can you give me:\n1) your first born child, \n2) your left shoe \n3)your right kidney \n4) your front left tire")
                option = input("Please choose how you would like proceed 1-4")
                while payment_flag:   
                    if option.isdigit() and int(option) in [1,2,3,4]:
                        self.parking_paid()
                        payment_flag = False
                        parking_flag= False
                    else:
                        option = input("\nYou did not enter a valid number please enter 1-4")


    def parking_paid(self):
        print("\nYour parking ticket has been paid. You have 15 minutes to leave the premise")
        self.currentTicket [self.lic_num][1]= "paid"



    
    def leave_garage(self):
        leave_flag = True
        while leave_flag:
            if self.currentTicket [self.lic_num][1] == "paid":
                print("Thank You, have a nice day")
                self.tickets.append(len(self.tickets))
                self.parkingSpaces.append(len(self.parkingSpaces))
                leave_flag = False
            else:
                self.pay_for_parking()


new_garage = ParkingGarage(10)

new_garage.take_ticket()
new_garage.leave_garage()






    


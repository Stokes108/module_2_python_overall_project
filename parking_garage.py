
class ParkingGarage():


    currentTicket = {}

    def __init__(self, spaces):
        self.tickets = [x for x in range(spaces)]
        self.parkingSpaces = [x for x in range(spaces)]


    def take_ticket(self):
        ticket_num = self.tickets.pop()
        self.parkingSpaces.pop()
        self.currentTicket ["paid"] = False

    
    def pay_for_parking(self):
        parking_flag = True
        parking_payment = input("Please enter payment amount for your parking stay: ")
        while parking_flag:
            if parking_payment.isdigit():
                print("\nYour parking ticket has been paid. You have 15 minutes to leave the premise")
                self.currentTicket ["paid"] = True
                parking_flag = False
            else:
                parking_payment = input("You did not enter a number please enter a number: ")

    
    def leave_garage(self):
        leave_flag = True
        while leave_flag:
            if self.currentTicket ["paid"] == True:
                print("Thank You, have a nice day")
                self.tickets.append(len(self.tickets))
                self.parkingSpaces.append(len(self.parkingSpaces))
                leave_flag = False
            else:
                print("Your ticket has not been paid. Please pay your ticket \n")
                self.pay_for_parking()



garage_1 = ParkingGarage(50)

garage_1.take_ticket()
# garage_1.pay_for_parking()
# garage_1.pay_for_parking()
garage_1.leave_garage()






    


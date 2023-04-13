tickets = [] #store all tickets 
class Ticket:
    #static variable for ticket count, open and reopen status 
    ticket_counter = 0 
    open_tickets = 0
    resolved_tickets = 0
    closed_tickets = 0

    def __init__(self, staff_id, creator_name, contact_email, description):
        self.ticket_number = Ticket.ticket_counter + 2000 #store ticket number from 2000
        Ticket.ticket_counter += 1 ##increment counter by 1 
        self.staff_id = staff_id
        self.creator_name = creator_name
        self.contact_email = contact_email
        self.description = description
        self.response = "Not Yet Provided" #default reponse
        self.status = "Open" # default status
        Ticket.open_tickets += 1

    def resolve_ticket(self):
        if "Password Change" in self.description: #check password string
            new_password = self.generate_new_password() #get new password
            self.response = f"New Password: {new_password}" 
            self.status = "Closed"
            Ticket.open_tickets -= 1 
            Ticket.resolved_tickets += 1
            Ticket.closed_tickets += 1
            return True;
        return False

    def reopen_ticket(self):
        if self.status == "Closed": #check status is closed or not
            self.status = "Reopened"
            Ticket.open_tickets += 1
            Ticket.resolved_tickets -= 1
            Ticket.closed_tickets -= 1
        else:
            print("Cannot reopen ticket. Ticket is not closed.")#print data on console

    def generate_new_password(self):
        return f"{self.staff_id[:2]}{self.creator_name[:3]}" #created new password

    def provide_response(self, response):
        self.response = response #append response
        self.status = "Closed"
        Ticket.open_tickets -= 1
        Ticket.resolved_tickets += 1
        Ticket.closed_tickets += 1

    @staticmethod
    def ticket_stats(): #static method for print highlevel statistics
        print("\nTickets Created:", Ticket.ticket_counter)
        print("Tickets Resolved:", Ticket.resolved_tickets)
        print("Tickets To Solve:", Ticket.open_tickets)

    def display_ticket(self):#print all details of ticket
        print("\nTicket Number:", self.ticket_number)
        print("Ticket Creator:", self.creator_name)
        print("Staff ID:", self.staff_id)
        print("Email Address:", self.contact_email)
        print("Description:", self.description)
        print("Response:", self.response)
        print("Ticket Status:", self.status)


def create_ticket():
    print("\nCreating Ticket...")
    staff_id = input("Please Enter Staff ID: ") #get input from user
    creator_name = input("Please Enter Creator Name: ") #get input from user
    contact_email = input("Please Enter Contact Email: ") #get input from user
    description = input("Please Enter Description: ") #get input from user
    ticket = Ticket(staff_id, creator_name, contact_email, description)
    print("Ticket Created Successfully!")#print data on console
    ticket.display_ticket()
    tickets.append(ticket)


def respond_to_ticket():
    ticket_number = int(input("\nEnter Ticket Number: "))#get input from user
    for ticket in tickets:
        if ticket.ticket_number == ticket_number: #check input ticket to available tickets
            if(ticket.resolve_ticket()):
                print("Ticket Resolved Successfully!")#print data on console
                ticket.display_ticket()
                return
            response = input("Provide Response: ")
            ticket.provide_response(response)
            print("Response Recorded Successfully!")#print data on console
            ticket.display_ticket()
            return
    print("Invalid Ticket Number.")#print data on console


def resolve_ticket():
    ticket_number = int(input("\nEnter Ticket Number: ")) #get input from user
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:
            ticket.resolve_ticket()
            print("Ticket Resolved Successfully!")#print data on console
            ticket.display_ticket()
            return
    print("Invalid Ticket Number.")#print data on console


def reopen_ticket():
    ticket_number = int(input("\nEnter Ticket Number: ")) #get input from user
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:
            ticket.reopen_ticket()
            print("Ticket Reopened Successfully!")#print data on console
            ticket.display_ticket()
            return
    print("Invalid Ticket Number.")#print data on console


def display_statistics():
    Ticket.ticket_stats()
    
def display_ticket_details():
    ticket_number = int(input("\nEnter Ticket Number: ")) #get input from user
    for ticket in tickets:
        if ticket.ticket_number == ticket_number:            
            ticket.display_ticket()
            return
    print("Invalid Ticket Number.")

def display_menu():
    print("\n---------Welcome to the Help Desk Ticketing System!-----------") #print data on console
    print("Please select an option:")#print data on console
    print("1. Submit a ticket")#print data on console
    print("2. Respond to a ticket")#print data on console
    print("3. Reopen a ticket")#print data on console
    print("4. Display ticket statistics")#print data on console
    print("5. Display ticket details")#print data on console
    print("6. Exit")#print data on console



def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ") #get input from user

        if choice == "1":
            create_ticket()
        elif choice == "2":
            respond_to_ticket()
        elif choice == "3":
            reopen_ticket()
        elif choice == "4":
            display_statistics()
        elif choice == "5":
            display_ticket_details()
        elif choice == "6":
            print("Thank you for using the Help Desk Ticketing System!")#print data on console
            break
        else:
            print("Invalid Choice. Please try again.")#print data on console


if __name__ == "__main__":
    main()



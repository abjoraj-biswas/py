import random
num_tickets = 100
winning_number = random.randint(1, num_tickets)
print("Welcome to the lottery game!")
print(f"There are {num_tickets} tickets available. Each ticket costs $10.")
ticket_number = int(input("Please enter the number of the ticket you want to buy: "))
if ticket_number < 1 or ticket_number > num_tickets:
    print("Invalid ticket number. Please try again.")
elif ticket_number == winning_number:
    print("Congratulations! You have won the lottery!")
    print(f"You have bought ticket number {ticket_number}, which matches the winning number {winning_number}.")
    print("You have won $1000!")
else:
    print("Sorry, you have not won the lottery.")
    print(f"You have bought ticket number {ticket_number}, which does not match the winning number {winning_number}.")
    print("Thank you for playing. Better luck next time!")


# Constants
TRAINS = ["09:00", "11:00", "13:00", "15:00"]
NUM_COACHES = 6
SEATS_PER_COACH = 80
TICKET_PRICE = 25

# Data Structures
passengers_count = {train: 0 for train in TRAINS}
money_taken = {train: 0 for train in TRAINS}

# Task 1 - Start of the day
def initialize_display():
    print("=== Electric Mountain Railway Ticketing System ===")
    print("\nTrain Schedule:")
    for train in TRAINS:
        print(f"{train} - {NUM_COACHES} coaches, {SEATS_PER_COACH} seats each")

# Task 2 - Purchasing tickets
def purchase_tickets():
    train_up = input("\nEnter the departure time for the train journey up (e.g., 09:00): ")
    train_down = input("Enter the departure time for the train journey down (e.g., 10:00): ")

    if train_up not in TRAINS or train_down not in TRAINS:
        print("Invalid train times. Please choose valid departure times.")
        return

    num_passengers = int(input("Enter the number of passengers: "))
    if num_passengers < 1:
        print("Invalid number of passengers. Please enter a positive number.")
        return

    total_tickets_up = NUM_COACHES * SEATS_PER_COACH
    total_tickets_down = NUM_COACHES * SEATS_PER_COACH

    if num_passengers > total_tickets_up or num_passengers > total_tickets_down:
        print("Not enough tickets available for the selected train journeys.")
        return

    group_discount = (num_passengers // 10) * TICKET_PRICE
    total_price = num_passengers * TICKET_PRICE - group_discount

    print("\nTicket Details:")
    print(f"Train Journey Up ({train_up}): {num_passengers} tickets - ${total_price:.2f}")

    # Update data structures
    passengers_count[train_up] += num_passengers
    money_taken[train_up] += total_price

    # Display updated screen
    print("\nUpdated Screen Display:")
    display_screen()

# Task 3 - End of the day
def display_results():
    print("\n=== End of the Day Results ===")
    total_passengers = sum(passengers_count.values())
    total_money = sum(money_taken.values())

    print("\nTrain Journeys:")
    for train in TRAINS:
        print(f"{train} - Passengers: {passengers_count[train]}, Money Taken: ${money_taken[train]:.2f}")

    print("\nTotal for the Day:")
    print(f"Total Passengers: {total_passengers}, Total Money Taken: ${total_money:.2f}")

    max_passengers_train = max(passengers_count, key=passengers_count.get)
    print(f"\nTrain Journey with the Most Passengers: {max_passengers_train} ({passengers_count[max_passengers_train]} passengers)")

# Display function
def display_screen():
    print("\nScreen Display:")
    for train in TRAINS:
        available_tickets = NUM_COACHES * SEATS_PER_COACH - passengers_count[train]
        if available_tickets > 0:
            print(f"{train} - {available_tickets} tickets available")
        else:
            print(f"{train} - Closed")

# Main program
initialize_display()

# Example ticket purchases (you can replace this with user interactions)
purchase_tickets()
purchase_tickets()

# Display end-of-day results
display_results()
